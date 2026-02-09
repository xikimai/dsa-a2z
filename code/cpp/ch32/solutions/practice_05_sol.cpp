/*
 * Solution for Practice 5: Longest Happy Prefix
 * Chapter 32: String Algorithms — Beyond Brute Force
 */
#include <string>
#include <vector>
using namespace std;

string solve(string s) {
    int n = s.size();
    if (n <= 1) return "";

    vector<int> fail(n, 0);
    int length = 0, i = 1;
    while (i < n) {
        if (s[i] == s[length]) fail[i++] = ++length;
        else if (length > 0) length = fail[length - 1];
        else fail[i++] = 0;
    }
    return s.substr(0, fail[n - 1]);
}

int main() { return 0; }
