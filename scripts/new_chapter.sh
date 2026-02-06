#!/bin/bash
# ==============================================================================
# DSA Olympiad Workbook — New Chapter Scaffolder
# ==============================================================================
# Creates the directory structure for a new chapter from templates.
# Usage: ./scripts/new_chapter.sh <part-dir> <chapter-dir> <chapter-title>
# Example: ./scripts/new_chapter.sh part-2-the-bronze-forge ch-07-number-wizardry "Number Wizardry"
# ==============================================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"
TEMPLATE_DIR="$ROOT_DIR/templates"

if [ $# -lt 3 ]; then
    echo "Usage: $0 <part-dir> <chapter-dir> <chapter-title>"
    echo ""
    echo "Example:"
    echo "  $0 part-2-the-bronze-forge ch-07-number-wizardry \"Number Wizardry\""
    exit 1
fi

PART_DIR="$1"
CHAPTER_DIR="$2"
CHAPTER_TITLE="$3"

# Extract chapter number from dir name (e.g., ch-07-... -> ch07)
CHAPTER_NUM=$(echo "$CHAPTER_DIR" | grep -oE 'ch-[0-9]+' | sed 's/-//')

BOOK_DIR="$ROOT_DIR/$PART_DIR/$CHAPTER_DIR"
CODE_PYTHON="$ROOT_DIR/code/python/$CHAPTER_NUM"
CODE_JAVA="$ROOT_DIR/code/java/$CHAPTER_NUM"
CODE_CPP="$ROOT_DIR/code/cpp/$CHAPTER_NUM"

echo "Creating chapter: $CHAPTER_TITLE"
echo "  Book content: $BOOK_DIR"
echo "  Code:         $CODE_PYTHON, $CODE_JAVA, $CODE_CPP"
echo ""

# --- Create book content directory ---
mkdir -p "$BOOK_DIR"

# Copy and customize README template
if [ -f "$TEMPLATE_DIR/README.md.template" ]; then
    sed "s/{{CHAPTER_TITLE}}/$CHAPTER_TITLE/g" "$TEMPLATE_DIR/README.md.template" > "$BOOK_DIR/README.md"
    echo "  [OK] README.md created"
else
    echo "# Chapter: $CHAPTER_TITLE" > "$BOOK_DIR/README.md"
    echo "  [OK] README.md created (no template found, using minimal)"
fi

# Copy Johari template
if [ -f "$TEMPLATE_DIR/johari.md.template" ]; then
    sed "s/{{CHAPTER_TITLE}}/$CHAPTER_TITLE/g" "$TEMPLATE_DIR/johari.md.template" > "$BOOK_DIR/johari.md"
    echo "  [OK] johari.md created"
else
    echo "# Johari Window: $CHAPTER_TITLE" > "$BOOK_DIR/johari.md"
    echo "  [OK] johari.md created (no template found, using minimal)"
fi

# --- Create code directories for all three languages ---
for lang_dir in "$CODE_PYTHON" "$CODE_JAVA" "$CODE_CPP"; do
    mkdir -p "$lang_dir/learn"
    mkdir -p "$lang_dir/practice"
    mkdir -p "$lang_dir/tests"
    mkdir -p "$lang_dir/solutions"
    # Add .gitkeep to empty dirs
    for subdir in learn practice tests solutions; do
        touch "$lang_dir/$subdir/.gitkeep"
    done
done

# Add __init__.py files for Python so imports work with pytest
touch "$CODE_PYTHON/__init__.py"
for subdir in learn practice tests solutions; do
    touch "$CODE_PYTHON/$subdir/__init__.py"
done
echo "  [OK] Code directories created (python, java, cpp)"

echo ""
echo "Done! Next steps:"
echo "  1. Edit $BOOK_DIR/README.md with chapter content"
echo "  2. Add problem files to code/python/$CHAPTER_NUM/practice/"
echo "  3. Add test files to code/python/$CHAPTER_NUM/tests/"
echo "  4. Repeat for java and cpp"
