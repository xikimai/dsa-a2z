#!/bin/bash
# ==============================================================================
# DSA Olympiad Workbook — Test Runner
# ==============================================================================
# Usage:
#   ./scripts/run_tests.sh ch01 python     # Run Python tests for Chapter 1
#   ./scripts/run_tests.sh ch01 java       # Run Java tests for Chapter 1
#   ./scripts/run_tests.sh ch01 cpp        # Run C++ tests for Chapter 1
#   ./scripts/run_tests.sh ch01 all        # Run all languages for Chapter 1
# ==============================================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"

GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m'

if [ $# -lt 2 ]; then
    echo "Usage: $0 <chapter> <language>"
    echo ""
    echo "  chapter:  ch00, ch01, ch02, ... ch30"
    echo "  language: python, java, cpp, all"
    echo ""
    echo "Examples:"
    echo "  $0 ch01 python"
    echo "  $0 ch07 all"
    exit 1
fi

CHAPTER="$1"
LANG="$2"

run_python_tests() {
    local test_dir="$ROOT_DIR/code/python/$CHAPTER/tests"
    if [ -d "$test_dir" ]; then
        echo -e "${CYAN}--- Python Tests ($CHAPTER) ---${NC}"
        python3 -m pytest "$test_dir" -v --tb=short
    else
        echo -e "${YELLOW}[SKIP]${NC} No Python tests found at $test_dir"
    fi
}

run_java_tests() {
    local test_dir="$ROOT_DIR/code/java/$CHAPTER/tests"
    if [ -d "$test_dir" ]; then
        echo -e "${CYAN}--- Java Tests ($CHAPTER) ---${NC}"
        local lib_dir="$ROOT_DIR/code/java/lib"
        local src_dir="$ROOT_DIR/code/java/$CHAPTER"
        # Compile all Java files in the chapter
        find "$src_dir" -name "*.java" | xargs javac -cp "$src_dir:$lib_dir/*" 2>/dev/null
        # Run JUnit tests
        if [ -f "$lib_dir/junit-platform-console-standalone.jar" ]; then
            java -jar "$lib_dir/junit-platform-console-standalone.jar" \
                --class-path "$src_dir" \
                --scan-class-path "$src_dir/tests"
        else
            echo -e "${YELLOW}[INFO]${NC} JUnit standalone jar not found. Compile and run tests manually."
            echo "  javac $src_dir/tests/*.java && java -cp $src_dir $CHAPTER.tests.TestWarmup01"
        fi
    else
        echo -e "${YELLOW}[SKIP]${NC} No Java tests found at $test_dir"
    fi
}

run_cpp_tests() {
    local test_dir="$ROOT_DIR/code/cpp/$CHAPTER/tests"
    if [ -d "$test_dir" ]; then
        echo -e "${CYAN}--- C++ Tests ($CHAPTER) ---${NC}"
        for test_file in "$test_dir"/*.cpp; do
            if [ -f "$test_file" ]; then
                local name=$(basename "$test_file" .cpp)
                local out="/tmp/dsa_test_${CHAPTER}_${name}"
                echo -n "  Compiling $name... "
                if g++ -std=c++17 -I"$ROOT_DIR/code/cpp/$CHAPTER" -o "$out" "$test_file" 2>&1; then
                    echo -n "Running... "
                    if "$out" 2>&1; then
                        echo -e "${GREEN}PASS${NC}"
                    else
                        echo -e "${RED}FAIL${NC}"
                    fi
                    rm -f "$out"
                else
                    echo -e "${RED}COMPILE ERROR${NC}"
                fi
            fi
        done
    else
        echo -e "${YELLOW}[SKIP]${NC} No C++ tests found at $test_dir"
    fi
}

echo "============================================="
echo "  DSA Workbook — Test Runner"
echo "  Chapter: $CHAPTER | Language: $LANG"
echo "============================================="
echo ""

case "$LANG" in
    python) run_python_tests ;;
    java)   run_java_tests ;;
    cpp)    run_cpp_tests ;;
    all)
        run_python_tests
        echo ""
        run_java_tests
        echo ""
        run_cpp_tests
        ;;
    *)
        echo -e "${RED}Unknown language: $LANG${NC}"
        echo "Use: python, java, cpp, or all"
        exit 1
        ;;
esac
