"""
Solution for Challenge 2: Shortest Palindrome (KMP)
=====================================================
Chapter 32: String Algorithms — Beyond Brute Force

APPROACH
--------
To make s a palindrome by adding characters to the front:
1. We need to find the longest palindromic prefix of s.
2. Then prepend the reverse of the remaining suffix.

To find the longest palindromic prefix efficiently:
- Create the string: s + "#" + reverse(s)
- Build the KMP failure function on this combined string
- The last value of the failure function gives the length of the
  longest prefix of s that matches a suffix of reverse(s),
  which is exactly the longest palindromic prefix.

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(n)
"""


def solve(s: str) -> str:
    """Return the shortest palindrome by adding characters to the front of s."""
    if len(s) <= 1:
        return s

    rev = s[::-1]
    combined = s + "#" + rev

    # Build KMP failure function
    n = len(combined)
    fail = [0] * n
    length = 0
    i = 1
    while i < n:
        if combined[i] == combined[length]:
            length += 1
            fail[i] = length
            i += 1
        elif length > 0:
            length = fail[length - 1]
        else:
            fail[i] = 0
            i += 1

    # Length of longest palindromic prefix
    longest_palindrome_prefix = fail[-1]

    # Add the reverse of the non-palindromic suffix to the front
    suffix_to_add = rev[:len(s) - longest_palindrome_prefix]
    return suffix_to_add + s


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    s = sys.stdin.read().strip()
    print(solve(s))
