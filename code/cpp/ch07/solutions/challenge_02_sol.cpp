/*
 * Solution -- Challenge 2: Sieve of Eratosthenes
 * ================================================
 * Chapter 7: Number Wizardry -- Math for Programmers
 *
 * APPROACH: Classic sieve. Create boolean array, mark composites starting
 *           from i*i for each prime i up to sqrt(n). Collect survivors.
 * TIME:  O(n log log n)
 * SPACE: O(n)
 */

#include <iostream>
#include <vector>
using namespace std;

vector<int> solve(int n) {
    vector<int> primes;
    if (n < 2) return primes;

    vector<bool> is_prime(n + 1, true);
    is_prime[0] = is_prime[1] = false;

    for (int i = 2; (long long)i * i <= n; i++) {
        if (is_prime[i]) {
            for (int j = i * i; j <= n; j += i) {
                is_prime[j] = false;
            }
        }
    }

    for (int i = 2; i <= n; i++) {
        if (is_prime[i]) primes.push_back(i);
    }
    return primes;
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
