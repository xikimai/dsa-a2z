#include <vector>
#include <queue>
#include <iostream>
using namespace std;

void solve(vector<vector<char>>& board) {
    int rows = board.size(), cols = board[0].size();
    int dr[] = {-1, 1, 0, 0}, dc[] = {0, 0, -1, 1};
    queue<pair<int,int>> q;

    for (int r = 0; r < rows; r++)
        for (int c = 0; c < cols; c++)
            if ((r == 0 || r == rows-1 || c == 0 || c == cols-1) && board[r][c] == 'O') {
                q.push({r, c});
                board[r][c] = 'S';
            }

    while (!q.empty()) {
        auto [r, c] = q.front(); q.pop();
        for (int d = 0; d < 4; d++) {
            int nr = r + dr[d], nc = c + dc[d];
            if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && board[nr][nc] == 'O') {
                board[nr][nc] = 'S';
                q.push({nr, nc});
            }
        }
    }

    for (int r = 0; r < rows; r++)
        for (int c = 0; c < cols; c++) {
            if (board[r][c] == 'O') board[r][c] = 'X';
            else if (board[r][c] == 'S') board[r][c] = 'O';
        }
}

int main() {
    int rows, cols;
    cin >> rows >> cols;
    vector<vector<char>> board(rows, vector<char>(cols));
    for (int i = 0; i < rows; i++)
        for (int j = 0; j < cols; j++)
            cin >> board[i][j];
    solve(board);
    for (auto& row : board) {
        for (char c : row) cout << c << " ";
        cout << "\n";
    }
    return 0;
}
