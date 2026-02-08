# Spec: Local GitBook Preview Server

## Problem

GitBook.com has no local preview. The old `gitbook-cli` is deprecated and doesn't support modern GitBook syntax (`{% tabs %}`, `{% hint %}`, etc.). We need a way to preview chapter content locally before pushing.

## Solution

A single Python script `scripts/local_preview.py` that serves the book locally with proper rendering of all GitBook-specific syntax.

- **One dependency**: `markdown` library (pip install markdown)
- **Code highlighting**: CDN-loaded `highlight.js` (github theme)
- **Mermaid diagrams**: CDN-loaded `mermaid.js`
- **All CSS/JS/HTML embedded in the script** — no external template files

## What It Needs to Handle

The project uses 1,452 GitBook tag instances across 37 files:

| Syntax | Count | Description |
|--------|-------|-------------|
| `{% tabs %}` / `{% endtabs %}` | 115 | Tab groups (language tabs for Python/Java/C++) |
| `{% tab title="..." %}` / `{% endtab %}` | 339 | Individual tabs within groups |
| `{% hint style="info\|warning\|danger\|success" %}` / `{% endhint %}` | 218 | Colored callout blocks |
| ` ```mermaid ` | 11 | Flowchart diagrams |
| Standard markdown | — | Headings, tables, fenced code blocks, links |

**Critical nesting**: Hints appear INSIDE tabs (e.g., Ch 0). The preprocessor must handle this.

## Architecture

```
Request → Route URL to .md file
        → Read .md from disk (always fresh, no caching)
        → Protect code blocks (replace with placeholders)
        → Preprocess: hints → tabs → mermaid (in that order)
        → Restore code blocks
        → Convert markdown → HTML
        → Fix relative links
        → Wrap in HTML template (sidebar + content)
        → Serve response
```

## Key Functions

| Function | Purpose |
|----------|---------|
| `parse_summary()` | Parse `SUMMARY.md` → sidebar nav structure |
| `build_sidebar_html()` | Generate sidebar HTML with active page highlight |
| `protect_code_blocks()` / `restore_code_blocks()` | Prevent false tag matches inside code fences |
| `preprocess_hints()` | `{% hint style="X" %}...{% endhint %}` → `<div class="hint hint-X">` |
| `preprocess_tabs()` | `{% tabs %}...{% endtabs %}` → tabbed HTML with unique IDs |
| `preprocess_mermaid()` | ` ```mermaid ` → `<pre class="mermaid">` |
| `fix_links()` | Resolve relative markdown links to server paths |
| `render_page()` | Full pipeline: read → preprocess → markdown → template |
| `PreviewHandler` | HTTP request handler (extends `BaseHTTPRequestHandler`) |

## Processing Order (matters for nesting)

1. **Hints first** — since hints nest inside tabs, converting them to `<div>`s first means tab processing doesn't need to handle raw hint tags
2. **Tabs second** — converts tab groups to HTML structure with unique IDs (`tab-{group}-{index}`)
3. **Mermaid third** — before markdown engine wraps them in `<code>` tags

## Preprocessing Details

### Code Block Protection

Before any tag processing, extract all fenced code blocks and replace with placeholders. This prevents false matches inside code examples:

```python
def protect_code_blocks(text):
    blocks = []
    def replacer(match):
        blocks.append(match.group(0))
        return f'\x00CODE_BLOCK_{len(blocks)-1}\x00'
    protected = re.sub(r'```.*?```', replacer, text, flags=re.DOTALL)
    return protected, blocks
```

### Hint Preprocessing

Line-by-line scanner (not single regex with DOTALL) because hints can nest inside tabs:

```
{% hint style="info" %}          →  <div class="hint hint-info">
Content here                         <div class="hint-content">
{% endhint %}                        Content here
                                     </div></div>
```

**Regex patterns:**
```python
HINT_OPEN = re.compile(r'\{%\s*hint\s+style="(\w+)"\s*%\}')
HINT_CLOSE = re.compile(r'\{%\s*endhint\s*%\}')
```

### Tabs Preprocessing

Process tab groups from outside-in. Each `{% tabs %}...{% endtabs %}` block becomes:

```html
<div class="tabs-container">
  <div class="tab-buttons">
    <button class="tab-btn active" data-tab="tab-0-0">Python</button>
    <button class="tab-btn" data-tab="tab-0-1">Java</button>
    <button class="tab-btn" data-tab="tab-0-2">C++</button>
  </div>
  <div class="tab-content active" id="tab-0-0">
    (markdown content)
  </div>
  <div class="tab-content" id="tab-0-1">
    (markdown content)
  </div>
  <div class="tab-content" id="tab-0-2">
    (markdown content)
  </div>
</div>
```

**Regex patterns:**
```python
TABS_OPEN = re.compile(r'\{%\s*tabs\s*%\}')
TABS_CLOSE = re.compile(r'\{%\s*endtabs\s*%\}')
TAB_OPEN = re.compile(r'\{%\s*tab\s+title="([^"]+)"\s*%\}')
TAB_CLOSE = re.compile(r'\{%\s*endtab\s*%\}')
```

### Mermaid Preprocessing

```python
MERMAID_BLOCK = re.compile(r'```mermaid\n(.*?)\n```', re.DOTALL)
# Replace with: <pre class="mermaid">{content}</pre>
```

## HTTP Server Design

stdlib `http.server.HTTPServer` + `BaseHTTPRequestHandler`. Single-threaded is fine for dev.

| URL Pattern | Handler |
|---|---|
| `/` | Redirect to `/README.md` |
| `/*.md` | Render markdown file |
| `/static/style.css` | Serve embedded CSS |
| `/static/script.js` | Serve embedded JS |
| Everything else | 404 |

## SUMMARY.md Parser

The sidebar navigation is built from `SUMMARY.md`:

```markdown
## Section Title
* [Chapter Title](relative/path/to/README.md)
```

Parser produces:
```python
@dataclass
class NavItem:
    title: str
    path: str  # relative to repo root

@dataclass
class NavSection:
    title: str
    items: list[NavItem]
```

## CSS Design

All embedded in the script as a constant string.

- **Layout**: Fixed 280px sidebar + scrolling main content (max-width 800px)
- **Font**: System font stack, 1.6 line-height
- **Sidebar**: `#f8f9fa` background, active item highlighted blue
- **Hints**:
  - `info`: blue left border, `#e8f0fe` background
  - `warning`: yellow left border, `#fef7e0` background
  - `danger`: red left border, `#fce8e6` background
  - `success`: green left border, `#e6f4ea` background
- **Tabs**: Horizontal button bar, active tab has blue bottom border, content panels show/hide
- **Code blocks**: Styled by highlight.js github theme

## JavaScript (Minimal)

Two behaviors, embedded in script:

1. **Tab switching**: Click handler on `.tab-btn` toggles `active` class on buttons and content panels within the same `.tabs-container`
2. **Sidebar highlight**: On load, add `active` class to sidebar link matching `window.location.pathname`

## Usage

```bash
pip install markdown
python scripts/local_preview.py              # http://localhost:8000
python scripts/local_preview.py --port 3000  # custom port
```

## Edge Cases

1. **Hints inside tabs** (Ch 0): Process hints FIRST, then tabs
2. **Mermaid inside tabs** (Ch 4): Mermaid.js init runs after page load, finds `<pre class="mermaid">` in all panels. May need re-init on tab switch
3. **Code blocks with `%` chars**: Protected by placeholder extraction before tag processing
4. **Stub chapters** (Ch 10+): Just heading + hint block — works naturally
5. **Relative links**: `[Johari](johari.md)` in `part-1/ch-02/README.md` resolves to `/part-1/ch-02/johari.md`

## Files to Create

| File | Lines (est.) | Description |
|------|-------------|-------------|
| `scripts/local_preview.py` | ~350 | The preview server |

No other files modified.

## Verification

1. `python scripts/local_preview.py`
2. Open `http://localhost:8000` — landing page with sidebar navigation
3. Ch 2 (richest content): language tabs, all 4 hint styles, mermaid diagrams, code highlighting, relative links
4. Ch 0: hints nested inside tabs render correctly
5. Ch 10+ (stub): "Coming Soon" hint renders
6. 404: request non-existent path returns error page

## Conventions to Follow

Match existing scripts in `scripts/`:
- `#!/usr/bin/env python3` shebang
- Module docstring with usage
- `ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))` for path resolution
- Stdlib-first, minimal external dependencies
