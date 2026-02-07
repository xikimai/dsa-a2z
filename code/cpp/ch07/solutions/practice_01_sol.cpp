/*
 * Solution -- Practice 1: All Divisors
 * ======================================
 * Chapter 7: Number Wizardry -- Math for Programmers
 *
 * APPROACH: Iterate from 1 to sqrt(n). If i divides n, add both i and n/i.
 *           Sort the result before returning.
 * TIME:  O(sqrt(n) + d*log(d)) where d = number of divisors
 * SPACE: O(d)
 */

#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

vector<int> solve(int n) {
    vector<int> divs;
    for (int i = 1; (long long)i * i <= n; i++) {
        if (n % i == 0) {
            divs.push_back(i);
            if (i != n / i) {
                divs.push_back(n / i);
            }
        }
    }
    sort(divs.begin(), divs.end());
    return divs;
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    vector<int> result = solve(n);
    for (int i = 0; i < (int)result.size(); i++) {
        if (i > 0) cout << " ";
        cout << result[i];
    }
    cout << endl;
    return 0;
}
