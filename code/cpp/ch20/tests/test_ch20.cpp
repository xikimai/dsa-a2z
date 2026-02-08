/*
 * Tests for Chapter 20: Graphs II — Real Problems
 * Build: g++ -std=c++17 -o /tmp/test_ch20 code/cpp/ch20/tests/test_ch20.cpp && /tmp/test_ch20
 */

#include <algorithm>
#include <cassert>
#include <climits>
#include <deque>
#include <iostream>
#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

// =====================================================================
// Reference solutions (uniquely named with ref_ prefix)
// =====================================================================

// --- W1: Flood Fill ---
vector<vector<int>> ref_flood_fill(vector<vector<int>> image, int sr, int sc, int color) {
    int rows = image.size(), cols = image[0].size();
    int original = image[sr][sc];
    if (original == color) return image;
    int dr[] = {-1,1,0,0}, dc[] = {0,0,-1,1};
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

// --- W2: Number of Islands ---
int ref_num_islands(vector<vector<int>> grid) {
    int rows = grid.size(), cols = grid[0].size(), count = 0;
    int dr[] = {-1,1,0,0}, dc[] = {0,0,-1,1};
    for (int r = 0; r < rows; r++)
        for (int c = 0; c < cols; c++)
            if (grid[r][c] == 1) {
                count++;
                queue<pair<int,int>> q;
                q.push({r, c}); grid[r][c] = 0;
                while (!q.empty()) {
                    auto [cr, cc] = q.front(); q.pop();
                    for (int d = 0; d < 4; d++) {
                        int nr = cr + dr[d], nc = cc + dc[d];
                        if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc] == 1) {
                            grid[nr][nc] = 0; q.push({nr, nc});
                        }
                    }
                }
            }
    return count;
}

// --- W3: Max Area of Island ---
int ref_max_area(vector<vector<int>> grid) {
    int rows = grid.size(), cols = grid[0].size(), maxA = 0;
    int dr[] = {-1,1,0,0}, dc[] = {0,0,-1,1};
    for (int r = 0; r < rows; r++)
        for (int c = 0; c < cols; c++)
            if (grid[r][c] == 1) {
                int area = 0;
                queue<pair<int,int>> q;
                q.push({r, c}); grid[r][c] = 0;
                while (!q.empty()) {
                    auto [cr, cc] = q.front(); q.pop();
                    area++;
                    for (int d = 0; d < 4; d++) {
                        int nr = cr + dr[d], nc = cc + dc[d];
                        if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc] == 1) {
                            grid[nr][nc] = 0; q.push({nr, nc});
                        }
                    }
                }
                maxA = max(maxA, area);
            }
    return maxA;
}

// --- W4: Surrounded Regions ---
vector<vector<char>> ref_surrounded(vector<vector<char>> board) {
    int rows = board.size(), cols = board[0].size();
    int dr[] = {-1,1,0,0}, dc[] = {0,0,-1,1};
    queue<pair<int,int>> q;
    for (int r = 0; r < rows; r++)
        for (int c = 0; c < cols; c++)
            if ((r==0||r==rows-1||c==0||c==cols-1) && board[r][c]=='O') {
                q.push({r,c}); board[r][c]='S';
            }
    while (!q.empty()) {
        auto [r,c] = q.front(); q.pop();
        for (int d = 0; d < 4; d++) {
            int nr = r+dr[d], nc = c+dc[d];
            if (nr>=0&&nr<rows&&nc>=0&&nc<cols&&board[nr][nc]=='O') {
                board[nr][nc]='S'; q.push({nr,nc});
            }
        }
    }
    for (int r = 0; r < rows; r++)
        for (int c = 0; c < cols; c++) {
            if (board[r][c]=='O') board[r][c]='X';
            else if (board[r][c]=='S') board[r][c]='O';
        }
    return board;
}

// --- P1: Rotten Oranges ---
int ref_rotten_oranges(vector<vector<int>> grid) {
    int rows = grid.size(), cols = grid[0].size();
    queue<pair<int,int>> q; int fresh = 0;
    int dr[] = {-1,1,0,0}, dc[] = {0,0,-1,1};
    for (int r = 0; r < rows; r++)
        for (int c = 0; c < cols; c++) {
            if (grid[r][c]==2) q.push({r,c});
            else if (grid[r][c]==1) fresh++;
        }
    if (fresh==0) return 0;
    int minutes = 0;
    while (!q.empty() && fresh > 0) {
        minutes++;
        int sz = q.size();
        for (int i = 0; i < sz; i++) {
            auto [r,c] = q.front(); q.pop();
            for (int d = 0; d < 4; d++) {
                int nr = r+dr[d], nc = c+dc[d];
                if (nr>=0&&nr<rows&&nc>=0&&nc<cols&&grid[nr][nc]==1) {
                    grid[nr][nc]=2; fresh--; q.push({nr,nc});
                }
            }
        }
    }
    return fresh==0 ? minutes : -1;
}

// --- P2: 01 Matrix ---
vector<vector<int>> ref_01_matrix(vector<vector<int>> mat) {
    int rows = mat.size(), cols = mat[0].size();
    vector<vector<int>> dist(rows, vector<int>(cols, INT_MAX));
    queue<pair<int,int>> q;
    int dr[] = {-1,1,0,0}, dc[] = {0,0,-1,1};
    for (int r = 0; r < rows; r++)
        for (int c = 0; c < cols; c++)
            if (mat[r][c]==0) { dist[r][c]=0; q.push({r,c}); }
    while (!q.empty()) {
        auto [r,c] = q.front(); q.pop();
        for (int d = 0; d < 4; d++) {
            int nr = r+dr[d], nc = c+dc[d];
            if (nr>=0&&nr<rows&&nc>=0&&nc<cols&&dist[nr][nc]>dist[r][c]+1) {
                dist[nr][nc]=dist[r][c]+1; q.push({nr,nc});
            }
        }
    }
    return dist;
}

// --- P4: Shortest Path Binary Matrix ---
int ref_shortest_path(vector<vector<int>> grid) {
    int n = grid.size();
    if (grid[0][0]==1||grid[n-1][n-1]==1) return -1;
    if (n==1) return 1;
    int dirs[][2] = {{-1,-1},{-1,0},{-1,1},{0,-1},{0,1},{1,-1},{1,0},{1,1}};
    queue<tuple<int,int,int>> q;
    q.push({0,0,1}); grid[0][0]=1;
    while (!q.empty()) {
        auto [r,c,dist] = q.front(); q.pop();
        for (auto& d : dirs) {
            int nr = r+d[0], nc = c+d[1];
            if (nr>=0&&nr<n&&nc>=0&&nc<n&&grid[nr][nc]==0) {
                if (nr==n-1&&nc==n-1) return dist+1;
                grid[nr][nc]=1; q.push({nr,nc,dist+1});
            }
        }
    }
    return -1;
}

// --- P5: Number of Enclaves ---
int ref_enclaves(vector<vector<int>> grid) {
    int rows = grid.size(), cols = grid[0].size();
    int dr[] = {-1,1,0,0}, dc[] = {0,0,-1,1};
    queue<pair<int,int>> q;
    for (int r = 0; r < rows; r++)
        for (int c = 0; c < cols; c++)
            if ((r==0||r==rows-1||c==0||c==cols-1)&&grid[r][c]==1) {
                q.push({r,c}); grid[r][c]=0;
            }
    while (!q.empty()) {
        auto [r,c] = q.front(); q.pop();
        for (int d = 0; d < 4; d++) {
            int nr = r+dr[d], nc = c+dc[d];
            if (nr>=0&&nr<rows&&nc>=0&&nc<cols&&grid[nr][nc]==1) {
                grid[nr][nc]=0; q.push({nr,nc});
            }
        }
    }
    int count = 0;
    for (auto& row : grid) for (int v : row) if (v==1) count++;
    return count;
}

// --- C1: Walls and Gates ---
vector<vector<int>> ref_walls_gates(vector<vector<int>> rooms) {
    int rows = rooms.size(), cols = rooms[0].size();
    int dr[] = {-1,1,0,0}, dc[] = {0,0,-1,1};
    int INF = 2147483647;
    queue<pair<int,int>> q;
    for (int r = 0; r < rows; r++)
        for (int c = 0; c < cols; c++)
            if (rooms[r][c]==0) q.push({r,c});
    while (!q.empty()) {
        auto [r,c] = q.front(); q.pop();
        for (int d = 0; d < 4; d++) {
            int nr = r+dr[d], nc = c+dc[d];
            if (nr>=0&&nr<rows&&nc>=0&&nc<cols&&rooms[nr][nc]==INF) {
                rooms[nr][nc]=rooms[r][c]+1; q.push({nr,nc});
            }
        }
    }
    return rooms;
}

// --- C2: Shortest Bridge ---
int ref_shortest_bridge(vector<vector<int>> grid) {
    int n = grid.size();
    int dr[] = {-1,1,0,0}, dc[] = {0,0,-1,1};
    queue<tuple<int,int,int>> mq;
    bool found = false;
    for (int r = 0; r < n && !found; r++)
        for (int c = 0; c < n && !found; c++)
            if (grid[r][c]==1) {
                queue<pair<int,int>> bfs;
                bfs.push({r,c}); grid[r][c]=2;
                while (!bfs.empty()) {
                    auto [cr,cc] = bfs.front(); bfs.pop();
                    mq.push({cr,cc,0});
                    for (int d = 0; d < 4; d++) {
                        int nr = cr+dr[d], nc = cc+dc[d];
                        if (nr>=0&&nr<n&&nc>=0&&nc<n&&grid[nr][nc]==1) {
                            grid[nr][nc]=2; bfs.push({nr,nc});
                        }
                    }
                }
                found=true;
            }
    while (!mq.empty()) {
        auto [r,c,dist] = mq.front(); mq.pop();
        for (int d = 0; d < 4; d++) {
            int nr = r+dr[d], nc = c+dc[d];
            if (nr>=0&&nr<n&&nc>=0&&nc<n) {
                if (grid[nr][nc]==1) return dist;
                if (grid[nr][nc]==0) { grid[nr][nc]=2; mq.push({nr,nc,dist+1}); }
            }
        }
    }
    return -1;
}

// --- C3: Making a Large Island ---
int ref_large_island(vector<vector<int>> grid) {
    int n = grid.size();
    vector<vector<int>> islandId(n, vector<int>(n, 0));
    unordered_map<int,int> islandSize;
    int dr[] = {-1,1,0,0}, dc[] = {0,0,-1,1};
    int curId = 2;
    for (int r = 0; r < n; r++)
        for (int c = 0; c < n; c++)
            if (grid[r][c]==1 && islandId[r][c]==0) {
                queue<pair<int,int>> q;
                q.push({r,c}); islandId[r][c]=curId;
                int sz = 0;
                while (!q.empty()) {
                    auto [cr,cc] = q.front(); q.pop();
                    sz++;
                    for (int d = 0; d < 4; d++) {
                        int nr = cr+dr[d], nc = cc+dc[d];
                        if (nr>=0&&nr<n&&nc>=0&&nc<n&&grid[nr][nc]==1&&islandId[nr][nc]==0) {
                            islandId[nr][nc]=curId; q.push({nr,nc});
                        }
                    }
                }
                islandSize[curId]=sz; curId++;
            }
    if (islandSize.empty()) return 1;
    int maxSz = 0;
    for (auto& [id,sz] : islandSize) maxSz = max(maxSz, sz);
    for (int r = 0; r < n; r++)
        for (int c = 0; c < n; c++)
            if (grid[r][c]==0) {
                unordered_set<int> nids;
                for (int d = 0; d < 4; d++) {
                    int nr = r+dr[d], nc = c+dc[d];
                    if (nr>=0&&nr<n&&nc>=0&&nc<n&&islandId[nr][nc]!=0) nids.insert(islandId[nr][nc]);
                }
                int total = 1;
                for (int id : nids) total += islandSize[id];
                maxSz = max(maxSz, total);
            }
    return maxSz;
}

// --- C4: Swim in Rising Water ---
int ref_swim(vector<vector<int>> grid) {
    int n = grid.size();
    int dr[] = {-1,1,0,0}, dc[] = {0,0,-1,1};
    int lo = max(grid[0][0], grid[n-1][n-1]), hi = n*n-1;
    while (lo < hi) {
        int mid = (lo+hi)/2;
        if (grid[0][0] > mid) { lo = mid+1; continue; }
        vector<vector<bool>> vis(n, vector<bool>(n, false));
        queue<pair<int,int>> q;
        q.push({0,0}); vis[0][0]=true;
        bool ok = false;
        while (!q.empty()) {
            auto [r,c] = q.front(); q.pop();
            if (r==n-1&&c==n-1) { ok=true; break; }
            for (int d = 0; d < 4; d++) {
                int nr = r+dr[d], nc = c+dc[d];
                if (nr>=0&&nr<n&&nc>=0&&nc<n&&!vis[nr][nc]&&grid[nr][nc]<=mid) {
                    vis[nr][nc]=true; q.push({nr,nc});
                }
            }
        }
        if (ok) hi=mid; else lo=mid+1;
    }
    return lo;
}

// =====================================================================
// Tests
// =====================================================================

int main() {
    int tests_passed = 0, tests_failed = 0;

    auto check = [&](bool cond, const char* name) {
        if (cond) { tests_passed++; }
        else { tests_failed++; cout << "FAIL: " << name << endl; }
    };

    // W1: Flood Fill
    check(ref_flood_fill({{1,1,1},{1,1,0},{1,0,1}}, 1, 1, 2) == vector<vector<int>>{{2,2,2},{2,2,0},{2,0,1}}, "W1 basic");
    check(ref_flood_fill({{0,0,0},{0,0,0}}, 0, 0, 0) == vector<vector<int>>{{0,0,0},{0,0,0}}, "W1 same color");
    check(ref_flood_fill({{5}}, 0, 0, 3) == vector<vector<int>>{{3}}, "W1 single");
    check(ref_flood_fill({{1,1},{1,1}}, 0, 0, 7) == vector<vector<int>>{{7,7},{7,7}}, "W1 all connected");

    // W2: Number of Islands
    check(ref_num_islands({{1,1,0,0,0},{1,1,0,0,0},{0,0,1,0,0},{0,0,0,1,1}}) == 3, "W2 three");
    check(ref_num_islands({{1,1,1},{0,1,0},{1,1,1}}) == 1, "W2 one");
    check(ref_num_islands({{0,0},{0,0}}) == 0, "W2 none");
    check(ref_num_islands({{1,0},{0,1}}) == 2, "W2 diagonal");

    // W3: Max Area
    check(ref_max_area({{0,0,1,0,0},{0,0,1,0,0},{0,1,1,0,1},{0,0,1,0,0}}) == 5, "W3 basic");
    check(ref_max_area({{0,0,0,0}}) == 0, "W3 none");
    check(ref_max_area({{1,1},{1,1}}) == 4, "W3 all land");

    // W4: Surrounded Regions
    check(ref_surrounded({{'X','X','X','X'},{'X','O','O','X'},{'X','X','O','X'},{'X','O','X','X'}})
        == vector<vector<char>>{{'X','X','X','X'},{'X','X','X','X'},{'X','X','X','X'},{'X','O','X','X'}}, "W4 basic");
    check(ref_surrounded({{'O','O'},{'O','O'}}) == vector<vector<char>>{{'O','O'},{'O','O'}}, "W4 all O border");

    // P1: Rotten Oranges
    check(ref_rotten_oranges({{2,1,1},{1,1,0},{0,1,1}}) == 4, "P1 basic");
    check(ref_rotten_oranges({{2,1,1},{0,1,1},{1,0,1}}) == -1, "P1 impossible");
    check(ref_rotten_oranges({{0,2}}) == 0, "P1 no fresh");
    check(ref_rotten_oranges({{2,1,1},{1,1,1},{1,1,2}}) == 2, "P1 multi source");

    // P2: 01 Matrix
    check(ref_01_matrix({{0,0,0},{0,1,0},{0,0,0}}) == vector<vector<int>>{{0,0,0},{0,1,0},{0,0,0}}, "P2 center");
    check(ref_01_matrix({{0,0,0},{0,1,0},{1,1,1}}) == vector<vector<int>>{{0,0,0},{0,1,0},{1,2,1}}, "P2 bottom");

    // P4: Shortest Path Binary Matrix
    check(ref_shortest_path({{0,1},{1,0}}) == 2, "P4 2x2");
    check(ref_shortest_path({{0,0,0},{1,1,0},{1,1,0}}) == 4, "P4 3x3");
    check(ref_shortest_path({{1,0,0},{1,1,0},{1,1,0}}) == -1, "P4 blocked");
    check(ref_shortest_path({{0}}) == 1, "P4 single");

    // P5: Enclaves
    check(ref_enclaves({{0,0,0,0},{1,0,1,0},{0,1,1,0},{0,0,0,0}}) == 3, "P5 basic");
    check(ref_enclaves({{0,1,1,0},{0,0,1,0},{0,0,1,0},{0,0,0,0}}) == 0, "P5 no enclaves");
    check(ref_enclaves({{0,0,0},{0,1,0},{0,0,0}}) == 1, "P5 single");

    // C1: Walls and Gates
    {
        int INF = 2147483647;
        check(ref_walls_gates({{INF,-1,0,INF},{INF,INF,INF,-1},{INF,-1,INF,-1},{0,-1,INF,INF}})
            == vector<vector<int>>{{3,-1,0,1},{2,2,1,-1},{1,-1,2,-1},{0,-1,3,4}}, "C1 basic");
        check(ref_walls_gates({{0,INF},{INF,INF}}) == vector<vector<int>>{{0,1},{1,2}}, "C1 single gate");
    }

    // C2: Shortest Bridge
    check(ref_shortest_bridge({{0,1},{1,0}}) == 1, "C2 diagonal");
    check(ref_shortest_bridge({{0,1,0},{0,0,0},{0,0,1}}) == 2, "C2 separated");
    check(ref_shortest_bridge({{1,1,1,1,1},{1,0,0,0,1},{1,0,1,0,1},{1,0,0,0,1},{1,1,1,1,1}}) == 1, "C2 concentric");

    // C3: Making a Large Island
    check(ref_large_island({{1,0},{0,1}}) == 3, "C3 diagonal");
    check(ref_large_island({{1,1},{1,0}}) == 4, "C3 almost full");
    check(ref_large_island({{1,1},{1,1}}) == 4, "C3 full");
    check(ref_large_island({{1,0,1},{1,0,1},{0,0,0}}) == 5, "C3 bridge");

    // C4: Swim in Rising Water
    check(ref_swim({{0,2},{1,3}}) == 3, "C4 2x2");
    check(ref_swim({{0,1,2,3,4},{24,23,22,21,5},{12,13,14,15,16},{11,17,18,19,20},{10,9,8,7,6}}) == 16, "C4 5x5");
    check(ref_swim({{0}}) == 0, "C4 1x1");

    cout << "\n========================================" << endl;
    cout << "Chapter 20 C++ Tests: " << tests_passed << " passed, " << tests_failed << " failed" << endl;
    if (tests_failed == 0) cout << "All ch20 tests passed!" << endl;
    else return 1;
    return 0;
}
