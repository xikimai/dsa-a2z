/*
 * Solution for Challenge 3: Minimum Bit Flips
 * TIME: O(k) where k = differing bits   SPACE: O(1)
 */
#include <iostream>
using namespace std;

int solve(int start, int goal) {
    int x = start ^ goal;
    int count = 0;
    while (x) {
        x &= (x - 1);
        count++;
    }
    return count;
}

int main() {
    int start, goal;
    cin >> start >> goal;
    cout << solve(start, goal) << endl;
    return 0;
}
