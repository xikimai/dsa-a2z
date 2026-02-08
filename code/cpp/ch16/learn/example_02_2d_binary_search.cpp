/*
 * Example 02: 2D Binary Search — Searching in Matrices
 * ======================================================
 * Chapter 16: Binary Search Beyond Arrays — Searching on Answers
 *
 * Demonstrates searching in a fully sorted matrix and row with max 1s.
 */

#include <iostream>
#include <vector>
using namespace std;

int main() {
    // Part 1: Search in Sorted Matrix
    cout << "=== Part 1: Search in Sorted Matrix ===" << endl;
    vector<vector<int>> matrix = {
        {1, 3, 5, 7},
        {10, 11, 16, 20},
        {23, 30, 34, 60},
        {61, 62, 67, 70}
    };

    cout << "Matrix:" << endl;
    for (auto& row : matrix) {
        cout << "  [";
        for (int j = 0; j < (int)row.size(); j++) {
            cout << row[j] << (j < (int)row.size() - 1 ? ", " : "");
        }
        cout << "]" << endl;
    }

    int target = 30;
    int rows = matrix.size(), cols = matrix[0].size();
    cout << "\nSearching for " << target << ":" << endl;

    int lo = 0, hi = rows * cols - 1;
    int step = 0;
    while (lo <= hi) {
        int mid = lo + (hi - lo) / 2;
        int r = mid / cols, c = mid % cols;
        int val = matrix[r][c];
        step++;
        cout << "  Step " << step << ": idx=" << mid << " -> [" << r << "][" << c << "] = " << val;
        if (val == target) {
            cout << "  FOUND!" << endl;
            break;
        } else if (val < target) {
            cout << " < " << target << " -> search right" << endl;
            lo = mid + 1;
        } else {
            cout << " > " << target << " -> search left" << endl;
            hi = mid - 1;
        }
    }

    // Part 2: Row with Maximum 1s
    cout << "\n=== Part 2: Row with Maximum 1s ===" << endl;
    vector<vector<int>> binMatrix = {
        {0, 0, 0, 1, 1},
        {0, 0, 1, 1, 1},
        {0, 0, 0, 0, 1},
        {0, 1, 1, 1, 1},
        {0, 0, 0, 0, 0}
    };

    int binCols = binMatrix[0].size();
    int bestRow = -1, bestCount = 0;
    for (int i = 0; i < (int)binMatrix.size(); i++) {
        int blo = 0, bhi = binCols;
        while (blo < bhi) {
            int mid = blo + (bhi - blo) / 2;
            if (binMatrix[i][mid] == 1) bhi = mid;
            else blo = mid + 1;
        }
        int count = binCols - blo;
        string marker = (count > bestCount) ? " <-- BEST" : "";
        cout << "  Row " << i << ": first 1 at idx " << blo << ", count=" << count << marker << endl;
        if (count > bestCount) { bestCount = count; bestRow = i; }
    }
    cout << "Row with max 1s: " << bestRow << " (" << bestCount << " ones)" << endl;

    return 0;
}
