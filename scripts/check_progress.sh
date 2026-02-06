#!/bin/bash
# ==============================================================================
# DSA Olympiad Workbook — Progress Checker
# ==============================================================================
# Counts passing tests across all chapters to show overall progress.
# Usage: ./scripts/check_progress.sh
# ==============================================================================

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"

GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m'

echo "============================================="
echo "  DSA Workbook — Progress Report"
echo "============================================="
echo ""

total_pass=0
total_fail=0
total_skip=0

for chapter_dir in "$ROOT_DIR"/code/python/ch*/; do
    if [ -d "$chapter_dir" ]; then
        chapter=$(basename "$chapter_dir")
        test_dir="$chapter_dir/tests"

        if [ -d "$test_dir" ] && ls "$test_dir"/*.py &>/dev/null 2>&1; then
            # Run pytest and capture counts
            output=$(python3 -m pytest "$test_dir" --tb=no -q 2>&1)
            passed=$(echo "$output" | grep -oE '[0-9]+ passed' | grep -oE '[0-9]+' || echo 0)
            failed=$(echo "$output" | grep -oE '[0-9]+ failed' | grep -oE '[0-9]+' || echo 0)

            passed=${passed:-0}
            failed=${failed:-0}

            total_pass=$((total_pass + passed))
            total_fail=$((total_fail + failed))

            if [ "$failed" -gt 0 ]; then
                echo -e "  ${YELLOW}$chapter${NC}: ${GREEN}$passed passed${NC}, ${RED}$failed failed${NC}"
            elif [ "$passed" -gt 0 ]; then
                echo -e "  ${GREEN}$chapter${NC}: ${GREEN}$passed passed${NC}"
            else
                echo -e "  ${CYAN}$chapter${NC}: no tests yet"
                total_skip=$((total_skip + 1))
            fi
        else
            echo -e "  ${CYAN}$chapter${NC}: no tests yet"
            total_skip=$((total_skip + 1))
        fi
    fi
done

echo ""
echo "---------------------------------------------"
echo -e "  Total: ${GREEN}$total_pass passed${NC}, ${RED}$total_fail failed${NC}, ${CYAN}$total_skip skipped${NC}"
echo "---------------------------------------------"
