#!/bin/bash
# ==============================================================================
# DSA Olympiad Workbook — macOS Development Environment Setup
# ==============================================================================
# Run this script once to set up Python, Java, C++, and testing tools.
# Usage: bash scripts/setup_mac.sh
# ==============================================================================

set -e

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo "============================================="
echo "  DSA Olympiad Workbook — Environment Setup"
echo "============================================="
echo ""

# --- Helper functions ---
check_installed() {
    if command -v "$1" &> /dev/null; then
        echo -e "${GREEN}[OK]${NC} $2 is installed: $($1 --version 2>&1 | head -1)"
        return 0
    else
        echo -e "${YELLOW}[MISSING]${NC} $2 is not installed"
        return 1
    fi
}

# --- Step 1: Xcode Command Line Tools (provides clang/g++) ---
echo "--- Step 1: Xcode Command Line Tools ---"
if xcode-select -p &> /dev/null; then
    echo -e "${GREEN}[OK]${NC} Xcode Command Line Tools installed"
else
    echo "Installing Xcode Command Line Tools..."
    xcode-select --install
    echo "Please complete the installation dialog, then re-run this script."
    exit 1
fi
echo ""

# --- Step 2: Homebrew ---
echo "--- Step 2: Homebrew ---"
if check_installed brew "Homebrew"; then
    echo "Updating Homebrew..."
    brew update
else
    echo "Installing Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    # Add to PATH for Apple Silicon Macs
    if [[ $(uname -m) == "arm64" ]]; then
        echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
        eval "$(/opt/homebrew/bin/brew shellenv)"
    fi
fi
echo ""

# --- Step 3: Python via pyenv ---
echo "--- Step 3: Python ---"
if check_installed pyenv "pyenv"; then
    echo "pyenv already installed"
else
    echo "Installing pyenv..."
    brew install pyenv
    # Add pyenv to shell
    echo '' >> ~/.zshrc
    echo '# pyenv (added by DSA workbook setup)' >> ~/.zshrc
    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
    echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
    echo 'eval "$(pyenv init -)"' >> ~/.zshrc
    export PYENV_ROOT="$HOME/.pyenv"
    export PATH="$PYENV_ROOT/bin:$PATH"
    eval "$(pyenv init -)"
fi

PYTHON_VERSION="3.12.4"
if pyenv versions 2>/dev/null | grep -q "$PYTHON_VERSION"; then
    echo -e "${GREEN}[OK]${NC} Python $PYTHON_VERSION already installed via pyenv"
else
    echo "Installing Python $PYTHON_VERSION..."
    pyenv install "$PYTHON_VERSION"
fi
pyenv global "$PYTHON_VERSION"

# Install pytest
echo "Installing pytest..."
pip install --quiet pytest
echo ""

# --- Step 4: Java (JDK 21) ---
echo "--- Step 4: Java ---"
if check_installed java "Java"; then
    echo "Java already installed"
else
    echo "Installing OpenJDK 21..."
    brew install openjdk@21
    sudo ln -sfn "$(brew --prefix openjdk@21)/libexec/openjdk.jdk" /Library/Java/JavaVirtualMachines/openjdk-21.jdk 2>/dev/null || true
    echo 'export PATH="$(brew --prefix openjdk@21)/bin:$PATH"' >> ~/.zshrc
fi
echo ""

# --- Step 5: C++ (clang from Xcode CLT) ---
echo "--- Step 5: C++ ---"
if check_installed g++ "C++ compiler (g++/clang++)"; then
    echo "C++ compiler ready"
else
    echo -e "${RED}[ERROR]${NC} C++ compiler not found. Xcode Command Line Tools should provide this."
    echo "Try: xcode-select --install"
fi
echo ""

# --- Step 6: VS Code ---
echo "--- Step 6: VS Code ---"
if check_installed code "VS Code"; then
    echo "Installing recommended extensions..."
    code --install-extension ms-python.python --force 2>/dev/null || true
    code --install-extension vscjava.vscode-java-pack --force 2>/dev/null || true
    code --install-extension ms-vscode.cpptools --force 2>/dev/null || true
    echo -e "${GREEN}[OK]${NC} VS Code extensions installed"
else
    echo -e "${YELLOW}[INFO]${NC} VS Code not found. Install it from https://code.visualstudio.com/"
    echo "After installing, run this script again to install extensions."
fi
echo ""

# --- Step 7: Verification ---
echo "============================================="
echo "  Verification"
echo "============================================="
echo ""

ALL_GOOD=true

echo -n "Python:  "
if python3 -c "print('Hello from Python!')" 2>/dev/null; then
    echo -e "${GREEN}[PASS]${NC}"
else
    echo -e "${RED}[FAIL]${NC}"
    ALL_GOOD=false
fi

echo -n "Java:    "
TMPDIR=$(mktemp -d)
echo 'public class Hello { public static void main(String[] args) { System.out.println("Hello from Java!"); } }' > "$TMPDIR/Hello.java"
if javac "$TMPDIR/Hello.java" && java -cp "$TMPDIR" Hello 2>/dev/null; then
    echo -e "${GREEN}[PASS]${NC}"
else
    echo -e "${RED}[FAIL]${NC}"
    ALL_GOOD=false
fi
rm -rf "$TMPDIR"

echo -n "C++:     "
TMPDIR=$(mktemp -d)
echo '#include <iostream>
int main() { std::cout << "Hello from C++!" << std::endl; return 0; }' > "$TMPDIR/hello.cpp"
if g++ -std=c++17 -o "$TMPDIR/hello" "$TMPDIR/hello.cpp" && "$TMPDIR/hello" 2>/dev/null; then
    echo -e "${GREEN}[PASS]${NC}"
else
    echo -e "${RED}[FAIL]${NC}"
    ALL_GOOD=false
fi
rm -rf "$TMPDIR"

echo -n "pytest:  "
if python3 -m pytest --version &>/dev/null; then
    echo -e "${GREEN}[PASS]${NC} $(python3 -m pytest --version 2>&1)"
else
    echo -e "${RED}[FAIL]${NC}"
    ALL_GOOD=false
fi

echo -n "git:     "
if check_installed git "Git" > /dev/null 2>&1; then
    echo -e "${GREEN}[PASS]${NC} $(git --version)"
else
    echo -e "${RED}[FAIL]${NC}"
    ALL_GOOD=false
fi

echo ""
if $ALL_GOOD; then
    echo -e "${GREEN}============================================="
    echo "  All checks passed! You're ready to code!"
    echo -e "=============================================${NC}"
else
    echo -e "${RED}============================================="
    echo "  Some checks failed. Fix the issues above"
    echo "  and run this script again."
    echo -e "=============================================${NC}"
fi
