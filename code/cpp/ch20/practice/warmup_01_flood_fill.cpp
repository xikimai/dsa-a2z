#include <vector>
#include <queue>
#include <iostream>
using namespace std;

vector<vector<int>> solve(vector<vector<int>> image, int sr, int sc, int color) {
    // TODO: Replace this with your solution
    return image;
}

int main() {
    int rows, cols, sr, sc, color;
    cin >> rows >> cols >> sr >> sc >> color;
    vector<vector<int>> image(rows, vector<int>(cols));
    for (int i = 0; i < rows; i++)
        for (int j = 0; j < cols; j++)
            cin >> image[i][j];
    auto result = solve(image, sr, sc, color);
    for (auto& row : result) {
        for (int v : row) cout << v << " ";
        cout << "\n";
    }
    return 0;
}
