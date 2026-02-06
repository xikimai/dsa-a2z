#!/bin/bash
# ==============================================================================
# DSA Workbook — Content Validator
# ==============================================================================
# Checks SUMMARY.md links and GitBook tag balance.
# Run before pushing to catch issues locally.
#
# Usage:
#   ./scripts/validate_content.sh
# ==============================================================================

set -e

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT_DIR"

GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

errors=0

# ── 1. SUMMARY.md link check ──────────────────────────────────────────

echo "Checking SUMMARY.md links..."
# Extract paths from markdown links: [text](path) → path
# Uses portable grep + sed (no GNU-only flags)
while IFS= read -r link; do
    if [[ ! -f "$link" ]]; then
        echo -e "  ${RED}MISSING${NC}: $link"
        errors=$((errors + 1))
    fi
done < <(grep -oE '\]\([^)]+\)' SUMMARY.md | sed 's/^](//' | sed 's/)$//')

if [[ $errors -eq 0 ]]; then
    echo -e "  ${GREEN}All links valid${NC}"
fi

# ── 2. GitBook tag balance ────────────────────────────────────────────

echo ""
echo "Checking GitBook tag balance..."
tag_errors=0

count_pattern() {
    # Portable grep -c that always returns a clean number
    # grep -c outputs "0" on no match but exits 1; || true prevents set -e failure
    grep -c "$1" "$2" 2>/dev/null || true
}

while IFS= read -r file; do
    tabs_open=$(count_pattern '{% tabs %}' "$file")
    tabs_close=$(count_pattern '{% endtabs %}' "$file")
    tab_open=$(count_pattern '{% tab ' "$file")
    tab_close=$(count_pattern '{% endtab %}' "$file")
    hint_open=$(count_pattern '{% hint' "$file")
    hint_close=$(count_pattern '{% endhint %}' "$file")

    if [[ $tabs_open -ne $tabs_close ]]; then
        echo -e "  ${RED}UNBALANCED${NC} {% tabs %} in $file (open=$tabs_open, close=$tabs_close)"
        tag_errors=$((tag_errors + 1))
    fi
    if [[ $tab_open -ne $tab_close ]]; then
        echo -e "  ${RED}UNBALANCED${NC} {% tab %} in $file (open=$tab_open, close=$tab_close)"
        tag_errors=$((tag_errors + 1))
    fi
    if [[ $hint_open -ne $hint_close ]]; then
        echo -e "  ${RED}UNBALANCED${NC} {% hint %} in $file (open=$hint_open, close=$hint_close)"
        tag_errors=$((tag_errors + 1))
    fi
done < <(find . -name '*.md' -not -path './.git/*' -not -path './.pytest_cache/*' -not -path './.claude/*' -not -name 'CLAUDE.md' -not -name 'striver-a2z.md')

errors=$((errors + tag_errors))
if [[ $tag_errors -eq 0 ]]; then
    echo -e "  ${GREEN}All tags balanced${NC}"
fi

# ── Result ────────────────────────────────────────────────────────────

echo ""
if [[ $errors -gt 0 ]]; then
    echo -e "${RED}$errors error(s) found${NC}"
    exit 1
else
    echo -e "${GREEN}All content checks passed${NC}"
fi
