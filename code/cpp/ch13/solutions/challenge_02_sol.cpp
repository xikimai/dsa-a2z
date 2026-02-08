/*
 * Solution for Challenge 2: Word Search
 * Chapter 13: Bronze Battle Plan — Complete Search & Simulation
 *
 * APPROACH: Try each cell as start, backtrack with in-place marking.
 * TIME:  O(m * n * 4^L)
 * SPACE: O(L)
 */

#include <iostream>
#include <string>
#include <vector>
using namespace std;

bool solve(vector<vector<char>> board, string word) {
    if (board.empty() || word.empty()) return false;
    int rows = board.size(), cols = board[0].size();

    int dirs[4][2] = {{-1,0},{1,0},{0,-1},{0,1}};

    function<bool(int, int, int)> bt = [&](int r, int c, int idx) -> bool {
        if (idx == (int)word.size()) return true;
        if (r < 0 || r >= rows || c < 0 || c >= cols) return false;
        if (board[r][c] != word[idx]) return false;

        char tmp = board[r][c];
        board[r][c] = '#';
        for (auto& d : dirs) {
            if (bt(r + d[0], c + d[1], idx + 1)) {
                board[r][c] = tmp;
                return true;
            }
        }
        board[r][c] = tmp;
        return false;
    };

    for (int r = 0; r < rows; r++)
        for (int c = 0; c < cols; c++)
            if (bt(r, c, 0)) return true;
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
