/*
 * Challenge 1: Sudoku Solver
 * ====================================
 * Chapter 13: Bronze Battle Plan — Complete Search & Simulation
 *
 * PROBLEM:
 *   Solve a 9x9 Sudoku puzzle. Empty cells are 0.
 *   Return the completed board.
 *
 * CONSTRAINTS:
 *   - board is 9x9
 *   - 0 represents empty cells
 *   - Each puzzle has exactly one solution
 */

#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> solve(vector<vector<int>> board) {
    // TODO: Replace this with your solution
    return board;
}

// -- Do not change anything below this line --------------------------
int main() {
    vector<vector<int>> board(9, vector<int>(9));
    for (int i = 0; i < 9; i++)
        for (int j = 0; j < 9; j++)
            cin >> board[i][j];
    vector<vector<int>> result = solve(board);
    for (auto& row : result) {
        for (int j = 0; j < 9; j++) {
            if (j > 0) cout << " ";
            cout << row[j];
        }
        cout << endl;
    }
    return 0;
}
