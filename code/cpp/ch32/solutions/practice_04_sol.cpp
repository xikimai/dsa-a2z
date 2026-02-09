/*
 * Solution for Practice 4: Repeated String Match
 * Chapter 32: String Algorithms — Beyond Brute Force
 */
#include <string>
#include <vector>
using namespace std;

int solve(string a, string b) {
    if (a.empty() || b.empty()) return b.empty() ? 1 : -1;
    int repeats = (b.size() + a.size() - 1) / a.size();
    string repeated;
    for (int i = 0; i < repeats; i++) repeated += a;
    if (repeated.find(b) != string::npos) return repeats;
    repeated += a;
    if (repeated.find(b) != string::npos) return repeats + 1;
    return -1;
}

int main() { return 0; }
