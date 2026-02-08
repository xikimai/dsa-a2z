/*
 * Challenge 2: Intersection of Two Lists
 * Chapter 21: Linked Lists — Pointers and Connections
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
#include <iostream>
#include <vector>
using namespace std;

int solve(vector<int> arrA, vector<int> arrB, int skipA, int skipB) {
    // TODO: Replace this with your solution
    return -1;
}

int main() {
    int na; cin >> na;
    vector<int> arrA(na);
    for (int i = 0; i < na; i++) cin >> arrA[i];
    int nb; cin >> nb;
    vector<int> arrB(nb);
    for (int i = 0; i < nb; i++) cin >> arrB[i];
    int skipA, skipB; cin >> skipA >> skipB;
    cout << solve(arrA, arrB, skipA, skipB) << endl;
    return 0;
}
