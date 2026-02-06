# ==============================================================================
# DSA Olympiad Workbook — C++ Build & Test Runner
# ==============================================================================
# Usage:
#   make test-ch01       # Run all tests for chapter 01
#   make test-all        # Run all tests for all chapters
#   make clean           # Remove compiled binaries
# ==============================================================================

CXX = g++
CXXFLAGS = -std=c++17 -Wall -Wextra -O2
BUILD_DIR = /tmp/dsa-a2z-cpp

# Find all chapter directories
CHAPTERS := $(wildcard ch*/)

# Test a specific chapter: make test-ch01
test-%:
	@echo "=== Testing $* ==="
	@mkdir -p $(BUILD_DIR)
	@if [ -d "$*/tests" ]; then \
		for test_file in $*/tests/*.cpp; do \
			if [ -f "$$test_file" ]; then \
				name=$$(basename "$$test_file" .cpp); \
				echo -n "  $$name... "; \
				if $(CXX) $(CXXFLAGS) -I"$*" -o "$(BUILD_DIR)/$$name" "$$test_file" 2>/dev/null; then \
					if $(BUILD_DIR)/$$name 2>/dev/null; then \
						echo "PASS"; \
					else \
						echo "FAIL"; \
					fi; \
				else \
					echo "COMPILE ERROR"; \
				fi; \
			fi; \
		done; \
	else \
		echo "  No tests found for $*"; \
	fi

# Test all chapters
test-all: $(foreach ch,$(CHAPTERS),test-$(patsubst %/,%,$(ch)))

# Clean compiled files
clean:
	rm -rf $(BUILD_DIR)

.PHONY: test-all clean
