#include <vector>
#include <queue>
#include <climits>
#include <iostream>
using namespace std;

vector<vector<int>> solve(vector<vector<int>>& mat) {
    // TODO: Replace this with your solution
    return mat;
}

int main() {
    int rows, cols;
    cin >> rows >> cols;
    vector<vector<int>> mat(rows, vector<int>(cols));
    for (int i = 0; i < rows; i++)
        for (int j = 0; j < cols; j++)
            cin >> mat[i][j];
    auto result = solve(mat);
    for (auto& row : result) {
        for (int v : row) cout << v << " ";
        cout << "\n";
    }
    return 0;
}
