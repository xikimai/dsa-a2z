"""
Example 02: KMP and Z-Function Demo
====================================
Chapter 32: String Algorithms — Beyond Brute Force

This example demonstrates:
  - Building the KMP failure function
  - KMP pattern matching
  - Building the Z-array
  - Using the Z-function for pattern matching
  - Rabin-Karp rolling hash
"""


# ── KMP: Failure Function ────────────────────────────────────

def build_failure(pattern):
    """Build the KMP failure (prefix) function.

    fail[i] = length of longest proper prefix of pattern[0..i]
              that is also a suffix of pattern[0..i].
    """
    m = len(pattern)
    fail = [0] * m
    length = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            fail[i] = length
            i += 1
        elif length > 0:
            length = fail[length - 1]
        else:
            fail[i] = 0
            i += 1
    return fail


def kmp_search(text, pattern):
    """Find all occurrences of pattern in text using KMP. Returns list of starting indices."""
    n, m = len(text), len(pattern)
    if m == 0:
        return []
    fail = build_failure(pattern)
    matches = []
    j = 0
    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = fail[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == m:
            matches.append(i - m + 1)
            j = fail[j - 1]
    return matches


# ── Z-Function ───────────────────────────────────────────────

def z_function(s):
    """Compute the Z-array for string s.

    z[i] = length of the longest substring starting at i
           that matches a prefix of s. z[0] = 0 by convention.
    """
    n = len(s)
    if n == 0:
        return []
    z = [0] * n
    l, r = 0, 0
    for i in range(1, n):
        if i < r:
            z[i] = min(r - i, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > r:
            l, r = i, i + z[i]
    return z


def z_search(text, pattern):
    """Find all occurrences of pattern in text using Z-function."""
    if not pattern:
        return []
    combined = pattern + "$" + text
    z = z_function(combined)
    m = len(pattern)
    return [i - m - 1 for i in range(m + 1, len(combined)) if z[i] == m]


# ── Rabin-Karp ───────────────────────────────────────────────

def rabin_karp_search(text, pattern):
    """Find all occurrences of pattern in text using rolling hash."""
    n, m = len(text), len(pattern)
    if m == 0 or m > n:
        return []

    BASE, MOD = 131, 10**9 + 7
    p_hash = t_hash = 0
    power = pow(BASE, m - 1, MOD)

    for i in range(m):
        p_hash = (p_hash * BASE + ord(pattern[i])) % MOD
        t_hash = (t_hash * BASE + ord(text[i])) % MOD

    matches = []
    for i in range(n - m + 1):
        if p_hash == t_hash and text[i:i + m] == pattern:
            matches.append(i)
        if i < n - m:
            t_hash = ((t_hash - ord(text[i]) * power) * BASE
                      + ord(text[i + m])) % MOD
    return matches


# ── Main ─────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 60)
    print("KMP, Z-FUNCTION, AND RABIN-KARP DEMO")
    print("=" * 60)

    # KMP failure function
    pattern = "AABAAAB"
    fail = build_failure(pattern)
    print(f"\n  Pattern: '{pattern}'")
    print(f"  Failure function: {fail}")

    # KMP search
    text = "AABAACAADAABAABA"
    pattern = "AABA"
    matches = kmp_search(text, pattern)
    print(f"\n  Text: '{text}'")
    print(f"  Pattern: '{pattern}'")
    print(f"  KMP matches at: {matches}")

    # Z-function
    s = "aabxaa"
    z = z_function(s)
    print(f"\n  String: '{s}'")
    print(f"  Z-array: {z}")

    # Z-function search
    matches_z = z_search(text, pattern)
    print(f"\n  Z-function matches at: {matches_z}")

    # Rabin-Karp
    matches_rk = rabin_karp_search(text, pattern)
    print(f"  Rabin-Karp matches at: {matches_rk}")

    # Overlapping matches
    text2 = "AAAAA"
    pattern2 = "AA"
    print(f"\n  Text: '{text2}', Pattern: '{pattern2}'")
    print(f"  KMP matches at: {kmp_search(text2, pattern2)}")
    print(f"  Z matches at: {z_search(text2, pattern2)}")
    print(f"  RK matches at: {rabin_karp_search(text2, pattern2)}")
