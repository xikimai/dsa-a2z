#include <vector>
#include <queue>
#include <algorithm>
#include <iostream>
using namespace std;

vector<vector<int>> solve(vector<vector<int>>& heights) {
    // TODO: Replace this with your solution
    return {};
}

int main() {
    int rows, cols;
    cin >> rows >> cols;
    vector<vector<int>> heights(rows, vector<int>(cols));
    for (int i = 0; i < rows; i++)
        for (int j = 0; j < cols; j++)
            cin >> heights[i][j];
    auto result = solve(heights);
    for (auto& cell : result)
        cout << cell[0] << " " << cell[1] << "\n";
    return 0;
}
