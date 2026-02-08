/*
 * Practice 5: Minimum Pages Allocation
 * Chapter 16: Binary Search Beyond Arrays — Searching on Answers
 *
 * PROBLEM: Allocate n books to k students. Minimize max pages per student.
 *          Return -1 if more students than books.
 */

#include <algorithm>
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;

int solve(vector<int> pages, int students) {
    // TODO: Replace this with your solution
    return 0;
}

int main() {
    int n;
    cin >> n;
    vector<int> pages(n);
    for (int i = 0; i < n; i++) cin >> pages[i];
    int students;
    cin >> students;
    cout << solve(pages, students) << endl;
    return 0;
}
