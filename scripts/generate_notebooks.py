#!/usr/bin/env python3
"""
Generate Colab notebooks from practice file skeletons and test files.

Creates one .ipynb per practice file in code/python/ch02-ch06.
Each notebook has: problem description, skeleton code, test cells.

Usage:
    python scripts/generate_notebooks.py
"""

import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOTEBOOKS_DIR = os.path.join(ROOT, "code", "notebooks")
PYTHON_DIR = os.path.join(ROOT, "code", "python")

CHAPTERS = ["ch02", "ch03", "ch04", "ch05", "ch06"]

REPO_URL = "https://github.com/xikimai/dsa-a2z"
COLAB_BASE = "https://colab.research.google.com/github/xikimai/dsa-a2z/blob/main"


def make_notebook(cells):
    """Create a minimal .ipynb notebook structure."""
    nb_cells = []
    for cell_type, source in cells:
        cell = {
            "cell_type": cell_type,
            "metadata": {},
            "source": source.split("\n") if isinstance(source, str) else source,
        }
        if cell_type == "code":
            cell["execution_count"] = None
            cell["outputs"] = []
        nb_cells.append(cell)

    return {
        "nbformat": 4,
        "nbformat_minor": 5,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {
                "name": "python",
                "version": "3.11.0",
            },
        },
        "cells": nb_cells,
    }


def split_lines(text):
    """Split text into notebook-style line list (each line ends with \\n except last)."""
    lines = text.split("\n")
    result = []
    for i, line in enumerate(lines):
        if i < len(lines) - 1:
            result.append(line + "\n")
        else:
            if line:  # Don't add empty trailing line
                result.append(line)
    return result


def extract_docstring(filepath):
    """Extract the module-level docstring from a Python file."""
    with open(filepath) as f:
        content = f.read()

    match = re.match(r'^"""(.*?)"""', content, re.DOTALL)
    if match:
        return match.group(1).strip()

    match = re.match(r"^'''(.*?)'''", content, re.DOTALL)
    if match:
        return match.group(1).strip()

    return ""


def extract_functions(filepath):
    """Extract function signatures and their docstrings from a practice file."""
    with open(filepath) as f:
        content = f.read()

    # Get everything after the docstring up to the "Do not change" line
    # Remove the module docstring
    content_no_doc = re.sub(r'^""".*?"""', "", content, count=1, flags=re.DOTALL)
    content_no_doc = re.sub(r"^'''.*?'''", "", content_no_doc, count=1, flags=re.DOTALL)

    # Remove the main block
    main_idx = content_no_doc.find("if __name__")
    if main_idx != -1:
        content_no_doc = content_no_doc[:main_idx]

    # Remove "Do not change" comment line
    content_no_doc = re.sub(
        r"#\s*──.*Do not change.*──.*\n?", "", content_no_doc
    )

    return content_no_doc.strip()


def extract_test_asserts(test_filepath):
    """Extract assert statements from a test file."""
    if not os.path.exists(test_filepath):
        return []

    with open(test_filepath) as f:
        content = f.read()

    # Extract all assert lines
    asserts = []
    for line in content.split("\n"):
        stripped = line.strip()
        if stripped.startswith("assert "):
            # Clean up the assert — remove the import prefix
            asserts.append(stripped)

    return asserts


def find_test_file(chapter, practice_filename):
    """Find the matching test file for a practice file."""
    # Practice file: warmup_01_greeting.py -> test_warmup_01.py
    base = os.path.splitext(practice_filename)[0]
    parts = base.split("_")
    # type_nn format: warmup_01, practice_03, challenge_02
    if len(parts) >= 2:
        test_name = f"test_{parts[0]}_{parts[1]}.py"
        test_path = os.path.join(PYTHON_DIR, chapter, "tests", test_name)
        if os.path.exists(test_path):
            return test_path
    return None


def generate_notebook_for_file(chapter, practice_file):
    """Generate a single .ipynb notebook for a practice file."""
    practice_path = os.path.join(PYTHON_DIR, chapter, "practice", practice_file)
    base_name = os.path.splitext(practice_file)[0]

    # Extract problem description
    docstring = extract_docstring(practice_path)

    # Extract function skeleton
    functions = extract_functions(practice_path)

    # Find and extract test cases
    test_path = find_test_file(chapter, practice_file)
    test_asserts = extract_test_asserts(test_path) if test_path else []

    # Build notebook title
    title_parts = base_name.replace("_", " ").title()
    chapter_num = chapter.replace("ch", "")

    # Cell 1: Header + problem description
    header_md = f"# {title_parts}\n"
    header_md += f"\n**Chapter {chapter_num}** | "
    header_md += f"[View in GitHub]({REPO_URL}/blob/main/code/python/{chapter}/practice/{practice_file})\n"
    header_md += f"\n---\n\n"
    # Format the docstring as markdown
    header_md += docstring

    # Cell 2: Instructions
    instructions_md = "## Your Solution\n\n"
    instructions_md += "Implement the function(s) below. Replace `pass` with your code."

    # Cell 3: Skeleton code
    skeleton_code = functions if functions else "def solve():\n    pass  # TODO: your code here"

    # Cell 4: Test cases header
    test_header_md = "## Test Your Solution\n\n"
    test_header_md += "Run the cell below to check your work. All asserts should pass silently."

    # Cell 5: Test code
    if test_asserts:
        test_code = "# Run these tests to check your solution\n"
        test_code += "\n".join(test_asserts)
        test_code += '\n\nprint("All tests passed!")'
    else:
        test_code = "# No automated tests available — test manually\n"
        test_code += 'print("Add your own test cases here")'

    cells = [
        ("markdown", header_md),
        ("markdown", instructions_md),
        ("code", skeleton_code),
        ("markdown", test_header_md),
        ("code", test_code),
    ]

    return make_notebook(cells)


def main():
    created = 0

    for chapter in CHAPTERS:
        practice_dir = os.path.join(PYTHON_DIR, chapter, "practice")
        if not os.path.isdir(practice_dir):
            print(f"  Skipping {chapter} — no practice dir")
            continue

        out_dir = os.path.join(NOTEBOOKS_DIR, chapter)
        os.makedirs(out_dir, exist_ok=True)

        practice_files = sorted(
            f
            for f in os.listdir(practice_dir)
            if f.endswith(".py") and f != "__init__.py"
        )

        for pf in practice_files:
            nb = generate_notebook_for_file(chapter, pf)
            nb_name = os.path.splitext(pf)[0] + ".ipynb"
            nb_path = os.path.join(out_dir, nb_name)

            with open(nb_path, "w") as f:
                json.dump(nb, f, indent=1)

            created += 1
            print(f"  Created: code/notebooks/{chapter}/{nb_name}")

    print(f"\nTotal: {created} notebooks created")


if __name__ == "__main__":
    main()
