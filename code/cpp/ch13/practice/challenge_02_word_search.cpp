/*
 * Challenge 2: Word Search
 * ====================================
 * Chapter 13: Bronze Battle Plan — Complete Search & Simulation
 *
 * PROBLEM:
 *   Given a 2D grid of characters and a word, determine if the word
 *   exists in the grid via adjacent (horizontal/vertical) cells.
 *   Each cell may be used at most once per path.
 *
 * CONSTRAINTS:
 *   - 1 <= rows, cols <= 6
 *   - 1 <= word.size() <= 15
 */

#include <iostream>
#include <string>
#include <vector>
using namespace std;

bool solve(vector<vector<char>> board, string word) {
    // TODO: Replace this with your solution
    return false;
}

// -- Do not change anything below this line --------------------------
int main() {
    int m, n;
    cin >> m >> n;
    vector<vector<char>> board(m, vector<char>(n));
    for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++)
            cin >> board[i][j];
    string word;
    cin >> word;
    cout << (solve(board, word) ? "true" : "false") << endl;
    return 0;
}
