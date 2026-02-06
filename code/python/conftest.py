"""
Shared pytest configuration for the DSA Olympiad Workbook.

This file is automatically discovered by pytest and applies to all tests
in the code/python/ directory.
"""
import sys
import os

# Add the python code root to the path so imports work across chapters
sys.path.insert(0, os.path.dirname(__file__))
