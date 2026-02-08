/*
 * Solution for Warmup 5: Check Tic-Tac-Toe Winner
 * Chapter 13: Bronze Battle Plan — Complete Search & Simulation
 *
 * APPROACH: Check 8 lines (3 rows, 3 cols, 2 diags).
 * TIME:  O(1)
 * SPACE: O(1)
 */

#include <iostream>
#include <string>
#include <vector>
using namespace std;

string solve(vector<vector<string>> board) {
    // Check rows and columns
    for (int i = 0; i < 3; i++) {
        if (board[i][0] == board[i][1] && board[i][1] == board[i][2] && board[i][0] != ".")
            return board[i][0];
        if (board[0][i] == board[1][i] && board[1][i] == board[2][i] && board[0][i] != ".")
            return board[0][i];
    }
    // Check diagonals
    if (board[0][0] == board[1][1] && board[1][1] == board[2][2] && board[0][0] != ".")
        return board[0][0];
    if (board[0][2] == board[1][1] && board[1][1] == board[2][0] && board[0][2] != ".")
        return board[0][2];

    // Check for ongoing
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            if (board[i][j] == ".")
                return "Ongoing";
    return "Draw";
}

// -- Do not change anything below this line --------------------------
int main() {
    vector<vector<string>> board(3, vector<string>(3));
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            cin >> board[i][j];
    cout << solve(board) << endl;
    return 0;
}
