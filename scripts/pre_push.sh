#!/bin/bash
# ==============================================================================
# DSA Workbook — Pre-Push Check
# ==============================================================================
# Runs all validations + tests locally before pushing.
# Mirrors what CI does so you catch issues before they hit GitHub.
#
# Usage:
#   ./scripts/pre_push.sh           # Run everything
#   ./scripts/pre_push.sh --quick   # Content validation only (skip tests)
# ==============================================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"

GREEN='\033[0;32m'
RED='\033[0;31m'
CYAN='\033[0;36m'
NC='\033[0m'

QUICK=false
if [[ "$1" == "--quick" ]]; then
    QUICK=true
fi

echo "============================================="
echo "  Pre-Push Check"
echo "============================================="
echo ""

# ── 1. Content validation ────────────────────────────────────────────

echo -e "${CYAN}[1/4] Validating content...${NC}"
"$SCRIPT_DIR/validate_content.sh"
echo ""

if [[ "$QUICK" == true ]]; then
    echo -e "${GREEN}Quick check passed!${NC}"
    exit 0
fi

# ── 2. Python tests ──────────────────────────────────────────────────

# Inject solutions into practice files so tests validate solutions, not skeletons.
# Backs up originals and restores them when done (even on failure).
echo "  Injecting solutions into practice files..."
BACKUP_DIR=$(mktemp -d)
injected_files=()
for sol_file in "$ROOT_DIR"/code/python/ch*/solutions/*_sol.py; do
    [ -f "$sol_file" ] || continue
    sol_name=$(basename "$sol_file" .py)
    type_nn="${sol_name%_sol}"
    chapter_dir=$(dirname "$(dirname "$sol_file")")
    practice_file=$(find "$chapter_dir/practice" -name "${type_nn}_*.py" ! -name '__init__.py' 2>/dev/null | head -1)
    if [[ -n "$practice_file" ]]; then
        # Back up original practice file
        backup_path="$BACKUP_DIR/$(echo "$practice_file" | tr '/' '_')"
        cp "$practice_file" "$backup_path"
        injected_files+=("$practice_file|$backup_path")
        # Overlay solution
        cp "$sol_file" "$practice_file"
    fi
done

restore_practice() {
    for entry in "${injected_files[@]}"; do
        practice_file="${entry%%|*}"
        backup_path="${entry##*|}"
        cp "$backup_path" "$practice_file" 2>/dev/null || true
    done
    rm -rf "$BACKUP_DIR" 2>/dev/null || true
}
trap restore_practice EXIT

echo -e "${CYAN}[2/4] Running Python tests...${NC}"
py_found=0
py_failed=0
for test_dir in "$ROOT_DIR"/code/python/ch*/tests; do
    [ -d "$test_dir" ] || continue
    ls "$test_dir"/*.py >/dev/null 2>&1 || continue

    chapter=$(basename "$(dirname "$test_dir")")
    py_found=$((py_found + 1))
    if ! python3 -m pytest "$test_dir" -q --tb=line 2>&1; then
        py_failed=$((py_failed + 1))
    fi
done
echo "  Python: $py_found chapter(s) tested, $py_failed failure(s)"
echo ""

# ── 3. Java tests ────────────────────────────────────────────────────

echo -e "${CYAN}[3/4] Running Java tests...${NC}"
java_found=0
java_failed=0
for test_dir in "$ROOT_DIR"/code/java/ch*/tests; do
    [ -d "$test_dir" ] || continue
    ls "$test_dir"/*.java >/dev/null 2>&1 || continue

    chapter_dir=$(dirname "$test_dir")
    chapter=$(basename "$chapter_dir")
    java_found=$((java_found + 1))

    # Compile from code/java/ so package declarations work
    if ! find "$chapter_dir" -name '*.java' -exec javac {} + 2>/dev/null; then
        echo -e "  ${RED}COMPILE ERROR${NC}: $chapter"
        java_failed=$((java_failed + 1))
        continue
    fi

    # Run each test class
    for test_file in "$test_dir"/*.java; do
        class_name=$(basename "$test_file" .java)
        if ! java -ea -cp "$ROOT_DIR/code/java" "$chapter.tests.$class_name" 2>&1; then
            java_failed=$((java_failed + 1))
        fi
    done
done
echo "  Java: $java_found chapter(s) tested, $java_failed failure(s)"
echo ""

# ── 4. C++ tests ─────────────────────────────────────────────────────

echo -e "${CYAN}[4/4] Running C++ tests...${NC}"
cpp_found=0
cpp_failed=0
for test_dir in "$ROOT_DIR"/code/cpp/ch*/tests; do
    [ -d "$test_dir" ] || continue
    ls "$test_dir"/*.cpp >/dev/null 2>&1 || continue

    chapter=$(basename "$(dirname "$test_dir")")
    cpp_found=$((cpp_found + 1))

    for test_file in "$test_dir"/*.cpp; do
        name=$(basename "$test_file" .cpp)
        out="/tmp/dsa_test_${name}"
        if ! g++ -std=c++17 -Wall -Wextra -O2 -o "$out" "$test_file" 2>/dev/null; then
            echo -e "  ${RED}COMPILE ERROR${NC}: $name"
            cpp_failed=$((cpp_failed + 1))
            continue
        fi
        if ! "$out" >/dev/null 2>&1; then
            echo -e "  ${RED}FAIL${NC}: $name"
            cpp_failed=$((cpp_failed + 1))
        fi
        rm -f "$out"
    done
done
echo "  C++: $cpp_found chapter(s) tested, $cpp_failed failure(s)"
echo ""

# ── Summary ───────────────────────────────────────────────────────────

total_failed=$((py_failed + java_failed + cpp_failed))
echo "============================================="
if [[ $total_failed -gt 0 ]]; then
    echo -e "  ${RED}$total_failed failure(s) — fix before pushing${NC}"
    echo "============================================="
    exit 1
else
    echo -e "  ${GREEN}All checks passed — safe to push!${NC}"
    echo "============================================="
fi
