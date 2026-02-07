#!/usr/bin/env python3
"""
Add "Open in Colab" badge sections to chapter READMEs.

Inserts a Colab section after each chapter's Practice Problems table,
listing all available notebooks for that chapter.

Usage:
    python scripts/add_colab_badges.py
"""

import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOTEBOOKS_DIR = os.path.join(ROOT, "code", "notebooks")
COLAB_BASE = "https://colab.research.google.com/github/xikimai/dsa-a2z/blob/main"
BADGE_URL = "https://colab.research.google.com/assets/colab-badge.svg"

# Map chapter codes to their README paths
CHAPTERS = {
    "ch02": "part-1-learning-to-speak-code/ch-02-first-programs/README.md",
    "ch03": "part-1-learning-to-speak-code/ch-03-decisions-and-loops/README.md",
    "ch04": "part-1-learning-to-speak-code/ch-04-functions/README.md",
    "ch05": "part-1-learning-to-speak-code/ch-05-collections/README.md",
    "ch06": "part-1-learning-to-speak-code/ch-06-how-fast-is-your-code/README.md",
}


def notebook_display_name(filename):
    """Convert warmup_01_greeting.ipynb to 'W1: Greeting'."""
    base = os.path.splitext(filename)[0]
    parts = base.split("_", 2)
    if len(parts) < 3:
        return base.replace("_", " ").title()

    tier = parts[0]
    num = parts[1].lstrip("0") or "0"
    name = parts[2].replace("_", " ").title()

    prefix_map = {"warmup": "W", "practice": "P", "challenge": "C"}
    prefix = prefix_map.get(tier, tier[0].upper())

    return f"{prefix}{num}: {name}"


def generate_colab_section(chapter):
    """Generate the Colab hint block for a chapter."""
    nb_dir = os.path.join(NOTEBOOKS_DIR, chapter)
    if not os.path.isdir(nb_dir):
        return None

    notebooks = sorted(f for f in os.listdir(nb_dir) if f.endswith(".ipynb"))
    if not notebooks:
        return None

    lines = []
    lines.append("")
    lines.append("{% hint style=\"info\" %}")
    lines.append("**Try in Google Colab!** Solve these problems in your browser — no setup needed.")
    lines.append("")

    for nb in notebooks:
        display = notebook_display_name(nb)
        url = f"{COLAB_BASE}/code/notebooks/{chapter}/{nb}"
        lines.append(f"[{display}]({url}) | ", )

    # Remove trailing " | " from last entry
    if lines:
        lines[-1] = lines[-1].rstrip(" | ")

    lines.append("")
    lines.append("{% endhint %}")
    lines.append("")

    return "\n".join(lines)


def insert_colab_section(readme_path, colab_section):
    """Insert the Colab section after the Practice Problems bash block."""
    with open(readme_path) as f:
        content = f.read()

    # Check if already added
    if "Try in Google Colab" in content:
        print(f"  Already has Colab section, skipping")
        return False

    # Find the bash block after Practice Problems table
    # Pattern: the ``` block with pytest commands, followed by ---
    # We insert BEFORE the ---
    pattern = r"(```bash\n# Run tests for a specific problem.*?```\n)\n(---)"
    match = re.search(pattern, content, re.DOTALL)

    if match:
        insert_point = match.end(1)
        content = content[:insert_point] + "\n" + colab_section + content[insert_point:]
    else:
        # Fallback: try to find just after "## Practice Problems" section ends
        # Look for the next "---" after Practice Problems
        pp_match = re.search(r"## Practice Problems.*?\n(---)", content, re.DOTALL)
        if pp_match:
            insert_point = pp_match.start(1)
            content = content[:insert_point] + colab_section + "\n" + content[insert_point:]
        else:
            print(f"  Could not find insertion point!")
            return False

    with open(readme_path, "w") as f:
        f.write(content)

    return True


def main():
    updated = 0

    for chapter, readme_rel in CHAPTERS.items():
        readme_path = os.path.join(ROOT, readme_rel)
        if not os.path.exists(readme_path):
            print(f"  {chapter}: README not found at {readme_rel}")
            continue

        colab_section = generate_colab_section(chapter)
        if not colab_section:
            print(f"  {chapter}: No notebooks found")
            continue

        print(f"  {chapter}: Adding Colab section to {readme_rel}")
        if insert_colab_section(readme_path, colab_section):
            updated += 1

    print(f"\nUpdated {updated} chapter READMEs with Colab badges")


if __name__ == "__main__":
    main()
