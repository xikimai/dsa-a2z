#include <vector>
#include <queue>
#include <iostream>
using namespace std;

void solve(vector<vector<char>>& board) {
    // TODO: Replace this with your solution
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
