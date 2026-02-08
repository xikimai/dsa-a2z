/*
 * Solution for Challenge 1: Sudoku Solver
 * Chapter 13: Bronze Battle Plan — Complete Search & Simulation
 *
 * APPROACH: Backtrack — find empty cell, try 1-9, validate row/col/box.
 * TIME:  O(9^empty) worst case, much less with pruning
 * SPACE: O(81)
 */

#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> solve(vector<vector<int>> board) {
    function<bool(int, int, int)> is_valid = [&](int r, int c, int num) -> bool {
        for (int i = 0; i < 9; i++) {
            if (board[r][i] == num || board[i][c] == num) return false;
        }
        int br = 3 * (r / 3), bc = 3 * (c / 3);
        for (int i = br; i < br + 3; i++)
            for (int j = bc; j < bc + 3; j++)
                if (board[i][j] == num) return false;
        return true;
    };

    function<bool()> backtrack = [&]() -> bool {
        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                if (board[r][c] == 0) {
                    for (int num = 1; num <= 9; num++) {
                        if (is_valid(r, c, num)) {
                            board[r][c] = num;
                            if (backtrack()) return true;
                            board[r][c] = 0;
                        }
                    }
                    return false;
                }
            }
        }
        return true;
    };

    backtrack();
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
