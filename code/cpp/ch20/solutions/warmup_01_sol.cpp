#include <vector>
#include <queue>
#include <iostream>
using namespace std;

vector<vector<int>> solve(vector<vector<int>> image, int sr, int sc, int color) {
    int rows = image.size(), cols = image[0].size();
    int original = image[sr][sc];
    if (original == color) return image;

    int dr[] = {-1, 1, 0, 0}, dc[] = {0, 0, -1, 1};
    queue<pair<int,int>> q;
    q.push({sr, sc});
    image[sr][sc] = color;

    while (!q.empty()) {
        auto [r, c] = q.front(); q.pop();
        for (int d = 0; d < 4; d++) {
            int nr = r + dr[d], nc = c + dc[d];
            if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && image[nr][nc] == original) {
                image[nr][nc] = color;
                q.push({nr, nc});
            }
        }
    }
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
