/*
 * Warmup 5: Check Tic-Tac-Toe Winner
 * ====================================
 * Chapter 13: Bronze Battle Plan — Complete Search & Simulation
 *
 * PROBLEM:
 *   Given a 3x3 board with 'X', 'O', or '.', return the game state:
 *   "X", "O", "Draw", or "Ongoing".
 *
 * EXAMPLES:
 *   board = {{"X","X","X"},{"O","O","."},{".",".","."}} -> "X"
 *   board = {{"X","O","X"},{"O","X","O"},{"O","X","O"}} -> "Draw"
 */

#include <iostream>
#include <string>
#include <vector>
using namespace std;

string solve(vector<vector<string>> board) {
    // TODO: Replace this with your solution
    return "";
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
