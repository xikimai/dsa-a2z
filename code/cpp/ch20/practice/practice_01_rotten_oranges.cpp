#include <vector>
#include <queue>
#include <iostream>
using namespace std;

int solve(vector<vector<int>>& grid) {
    // TODO: Replace this with your solution
    return 0;
}

int main() {
    int rows, cols;
    cin >> rows >> cols;
    vector<vector<int>> grid(rows, vector<int>(cols));
    for (int i = 0; i < rows; i++)
        for (int j = 0; j < cols; j++)
            cin >> grid[i][j];
    cout << solve(grid) << endl;
    return 0;
}
