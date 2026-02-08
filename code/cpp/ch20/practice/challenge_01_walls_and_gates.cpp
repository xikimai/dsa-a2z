#include <vector>
#include <queue>
#include <climits>
#include <iostream>
using namespace std;

void solve(vector<vector<int>>& rooms) {
    // TODO: Replace this with your solution
}

int main() {
    int rows, cols;
    cin >> rows >> cols;
    vector<vector<int>> rooms(rows, vector<int>(cols));
    for (int i = 0; i < rows; i++)
        for (int j = 0; j < cols; j++)
            cin >> rooms[i][j];
    solve(rooms);
    for (auto& row : rooms) {
        for (int v : row) cout << v << " ";
        cout << "\n";
    }
    return 0;
}
