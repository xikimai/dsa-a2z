/*
 * Solution for Challenge 3: Distinct Substrings of Length K
 * Chapter 32: String Algorithms — Beyond Brute Force
 */
#include <set>
#include <string>
#include <vector>
using namespace std;

int solve(string s, int k) {
    int n = s.size();
    if (k > n) return 0;
    set<string> seen;
    for (int i = 0; i <= n - k; i++)
        seen.insert(s.substr(i, k));
    return seen.size();
}

int main() { return 0; }
