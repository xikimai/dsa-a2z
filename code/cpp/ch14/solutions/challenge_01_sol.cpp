#include <algorithm>
#include <climits>
#include <iostream>
#include <vector>
using namespace std;

vector<long long> solve(vector<vector<int>> matrix, vector<vector<int>> queries) {
    if (matrix.empty() || matrix[0].empty()) return vector<long long>(queries.size(), 0);
    int rows = matrix.size(), cols = matrix[0].size();
    vector<vector<long long>> prefix(rows+1, vector<long long>(cols+1, 0));
    for (int i = 1; i <= rows; i++)
        for (int j = 1; j <= cols; j++)
            prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1] + matrix[i-1][j-1];
    vector<long long> result;
    for (auto& q : queries) {
        int r1=q[0], c1=q[1], r2=q[2], c2=q[3];
        result.push_back(prefix[r2+1][c2+1] - prefix[r1][c2+1] - prefix[r2+1][c1] + prefix[r1][c1]);
    }
    return result;
}

int main() {
    int rows, cols;
    cin >> rows >> cols;
    vector<vector<int>> matrix(rows, vector<int>(cols));
    for (int i = 0; i < rows; i++) for (int j = 0; j < cols; j++) cin >> matrix[i][j];
    int q; cin >> q;
    vector<vector<int>> queries(q, vector<int>(4));
    for (int i = 0; i < q; i++)
        cin >> queries[i][0] >> queries[i][1] >> queries[i][2] >> queries[i][3];
    auto result = solve(matrix, queries);
    for (int i = 0; i < (int)result.size(); i++)
        cout << result[i] << (i < (int)result.size()-1 ? " " : "\n");
    return 0;
}
