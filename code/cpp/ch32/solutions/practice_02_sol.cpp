/*
 * Solution for Practice 2: Longest Common Prefix
 * Chapter 32: String Algorithms — Beyond Brute Force
 */
#include <string>
#include <vector>
using namespace std;

string solve(vector<string>& words) {
    if (words.empty()) return "";
    string prefix;
    for (int i = 0; i < (int)words[0].size(); i++) {
        char ch = words[0][i];
        for (int j = 1; j < (int)words.size(); j++) {
            if (i >= (int)words[j].size() || words[j][i] != ch)
                return prefix;
        }
        prefix += ch;
    }
    return prefix;
}

int main() { return 0; }
