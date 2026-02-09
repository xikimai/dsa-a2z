/*
 * Tests for Chapter 13: Bronze Battle Plan — Complete Search & Simulation
 * Build: g++ -std=c++17 -o /tmp/test_ch13 code/cpp/ch13/tests/test_ch13.cpp && /tmp/test_ch13
 */

#include <algorithm>
#include <cassert>
#include <functional>
#include <iostream>
#include <set>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

// =====================================================================
// Reference solutions (uniquely named with ref_ prefix)
// =====================================================================

// --- W1: Generate All Permutations ---
vector<vector<int>> ref_generate_permutations(vector<int> nums) {
    sort(nums.begin(), nums.end());
    vector<vector<int>> result;
    vector<bool> used(nums.size(), false);
    vector<int> current;
    function<void()> bt = [&]() {
        if ((int)current.size() == (int)nums.size()) {
            result.push_back(current);
            return;
        }
        for (int i = 0; i < (int)nums.size(); i++) {
            if (used[i]) continue;
            used[i] = true;
            current.push_back(nums[i]);
            bt();
            current.pop_back();
            used[i] = false;
        }
    };
    bt();
    return result;
}

// --- W2: Generate All Subsets ---
vector<vector<int>> ref_generate_subsets(vector<int> nums) {
    sort(nums.begin(), nums.end());
    vector<vector<int>> result;
    vector<int> current;
    function<void(int)> bt = [&](int idx) {
        if (idx == (int)nums.size()) { result.push_back(current); return; }
        bt(idx + 1);
        current.push_back(nums[idx]);
        bt(idx + 1);
        current.pop_back();
    };
    bt(0);
    sort(result.begin(), result.end(), [](const vector<int>& a, const vector<int>& b) {
        if (a.size() != b.size()) return a.size() < b.size();
        return a < b;
    });
    return result;
}

// --- W3: Simulate Robot Moves ---
vector<int> ref_simulate_robot(string commands) {
    int x = 0, y = 0;
    for (char c : commands) {
        if (c == 'U') y++;
        else if (c == 'D') y--;
        else if (c == 'L') x--;
        else if (c == 'R') x++;
    }
    return {x, y};
}

// --- W4: Count Binary Strings ---
int ref_count_binary_strings(int n) {
    if (n == 1) return 2;
    int a = 1, b = 1;
    for (int i = 2; i <= n; i++) {
        int na = a + b;
        b = a;
        a = na;
    }
    return a + b;
}

// --- W5: Tic-Tac-Toe Winner ---
string ref_tic_tac_toe(vector<vector<string>> board) {
    for (int i = 0; i < 3; i++) {
        if (board[i][0] == board[i][1] && board[i][1] == board[i][2] && board[i][0] != ".")
            return board[i][0];
        if (board[0][i] == board[1][i] && board[1][i] == board[2][i] && board[0][i] != ".")
            return board[0][i];
    }
    if (board[0][0] == board[1][1] && board[1][1] == board[2][2] && board[0][0] != ".")
        return board[0][0];
    if (board[0][2] == board[1][1] && board[1][1] == board[2][0] && board[0][2] != ".")
        return board[0][2];
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            if (board[i][j] == ".") return "Ongoing";
    return "Draw";
}

// --- P1: Subsets Using Bitmasks ---
vector<vector<int>> ref_subsets_bitmask(vector<int> nums) {
    sort(nums.begin(), nums.end());
    int n = nums.size();
    vector<vector<int>> result;
    for (int mask = 0; mask < (1 << n); mask++) {
        vector<int> subset;
        for (int i = 0; i < n; i++)
            if (mask & (1 << i)) subset.push_back(nums[i]);
        result.push_back(subset);
    }
    sort(result.begin(), result.end(), [](const vector<int>& a, const vector<int>& b) {
        if (a.size() != b.size()) return a.size() < b.size();
        return a < b;
    });
    return result;
}

// --- P2: N-Queens Count ---
int ref_n_queens_count(int n) {
    int count = 0;
    set<int> cols, d1, d2;
    function<void(int)> bt = [&](int row) {
        if (row == n) { count++; return; }
        for (int col = 0; col < n; col++) {
            if (cols.count(col) || d1.count(row - col) || d2.count(row + col)) continue;
            cols.insert(col); d1.insert(row - col); d2.insert(row + col);
            bt(row + 1);
            cols.erase(col); d1.erase(row - col); d2.erase(row + col);
        }
    };
    bt(0);
    return count;
}

// --- P3: Rat in a Maze ---
vector<string> ref_rat_in_maze(vector<vector<int>> maze) {
    int n = maze.size();
    if (n == 0 || maze[0][0] == 0) return {};
    vector<string> result;
    vector<vector<bool>> vis(n, vector<bool>(n, false));
    int dr[] = {1, 0, 0, -1};
    int dc[] = {0, -1, 1, 0};
    char dir[] = {'D', 'L', 'R', 'U'};
    function<void(int, int, string)> bt = [&](int r, int c, string path) {
        if (r == n - 1 && c == n - 1) { result.push_back(path); return; }
        for (int d = 0; d < 4; d++) {
            int nr = r + dr[d], nc = c + dc[d];
            if (nr >= 0 && nr < n && nc >= 0 && nc < n && maze[nr][nc] == 1 && !vis[nr][nc]) {
                vis[nr][nc] = true;
                bt(nr, nc, path + dir[d]);
                vis[nr][nc] = false;
            }
        }
    };
    vis[0][0] = true;
    bt(0, 0, "");
    return result;
}

// --- P4: Letter Combinations ---
vector<string> ref_letter_combinations(string digits) {
    if (digits.empty()) return {};
    unordered_map<char, string> m = {
        {'2',"abc"},{'3',"def"},{'4',"ghi"},{'5',"jkl"},
        {'6',"mno"},{'7',"pqrs"},{'8',"tuv"},{'9',"wxyz"}
    };
    vector<string> result;
    function<void(int, string)> bt = [&](int idx, string cur) {
        if (idx == (int)digits.size()) { result.push_back(cur); return; }
        for (char ch : m[digits[idx]]) bt(idx + 1, cur + ch);
    };
    bt(0, "");
    return result;
}

// --- P5: Combination Sum ---
vector<vector<int>> ref_combination_sum(vector<int> cands, int target) {
    sort(cands.begin(), cands.end());
    vector<vector<int>> result;
    vector<int> cur;
    function<void(int, int)> bt = [&](int start, int rem) {
        if (rem == 0) { result.push_back(cur); return; }
        for (int i = start; i < (int)cands.size(); i++) {
            if (cands[i] > rem) break;
            cur.push_back(cands[i]);
            bt(i, rem - cands[i]);
            cur.pop_back();
        }
    };
    bt(0, target);
    return result;
}

// --- C1: Sudoku Solver ---
vector<vector<int>> ref_sudoku_solver(vector<vector<int>> board) {
    function<bool(int, int, int)> valid = [&](int r, int c, int num) -> bool {
        for (int i = 0; i < 9; i++)
            if (board[r][i] == num || board[i][c] == num) return false;
        int br = 3 * (r / 3), bc = 3 * (c / 3);
        for (int i = br; i < br + 3; i++)
            for (int j = bc; j < bc + 3; j++)
                if (board[i][j] == num) return false;
        return true;
    };
    function<bool()> bt = [&]() -> bool {
        for (int r = 0; r < 9; r++)
            for (int c = 0; c < 9; c++)
                if (board[r][c] == 0) {
                    for (int n = 1; n <= 9; n++)
                        if (valid(r, c, n)) { board[r][c] = n; if (bt()) return true; board[r][c] = 0; }
                    return false;
                }
        return true;
    };
    bt();
    return board;
}

// Sudoku validator
bool is_valid_sudoku(const vector<vector<int>>& board) {
    for (int i = 0; i < 9; i++) {
        set<int> row_set, col_set;
        for (int j = 0; j < 9; j++) {
            if (board[i][j] < 1 || board[i][j] > 9) return false;
            if (!row_set.insert(board[i][j]).second) return false;
            if (!col_set.insert(board[j][i]).second) return false;
        }
    }
    for (int br = 0; br < 9; br += 3)
        for (int bc = 0; bc < 9; bc += 3) {
            set<int> box_set;
            for (int i = br; i < br + 3; i++)
                for (int j = bc; j < bc + 3; j++)
                    if (!box_set.insert(board[i][j]).second) return false;
        }
    return true;
}

// --- C2: Word Search ---
bool ref_word_search(vector<vector<char>> board, string word) {
    if (board.empty() || word.empty()) return false;
    int rows = board.size(), cols = board[0].size();
    int dirs[4][2] = {{-1,0},{1,0},{0,-1},{0,1}};
    function<bool(int, int, int)> bt = [&](int r, int c, int idx) -> bool {
        if (idx == (int)word.size()) return true;
        if (r < 0 || r >= rows || c < 0 || c >= cols || board[r][c] != word[idx]) return false;
        char tmp = board[r][c]; board[r][c] = '#';
        for (auto& d : dirs)
            if (bt(r + d[0], c + d[1], idx + 1)) { board[r][c] = tmp; return true; }
        board[r][c] = tmp;
        return false;
    };
    for (int r = 0; r < rows; r++)
        for (int c = 0; c < cols; c++)
            if (bt(r, c, 0)) return true;
    return false;
}

// --- C3: N-Queens All Solutions ---
vector<vector<string>> ref_n_queens_all(int n) {
    vector<vector<string>> result;
    vector<int> queens;
    set<int> cols, d1, d2;
    function<void(int)> bt = [&](int row) {
        if (row == n) {
            vector<string> board;
            for (int r = 0; r < n; r++) {
                string s(n, '.'); s[queens[r]] = 'Q';
                board.push_back(s);
            }
            result.push_back(board);
            return;
        }
        for (int col = 0; col < n; col++) {
            if (cols.count(col) || d1.count(row - col) || d2.count(row + col)) continue;
            cols.insert(col); d1.insert(row - col); d2.insert(row + col);
            queens.push_back(col);
            bt(row + 1);
            queens.pop_back();
            cols.erase(col); d1.erase(row - col); d2.erase(row + col);
        }
    };
    bt(0);
    sort(result.begin(), result.end());
    return result;
}

// --- C4: Fence Painting ---
int ref_fence_painting(vector<vector<int>> fences) {
    if (fences.empty()) return 0;
    sort(fences.begin(), fences.end());
    int total = 0, cs = fences[0][0], ce = fences[0][1];
    for (int i = 1; i < (int)fences.size(); i++) {
        if (fences[i][0] <= ce) ce = max(ce, fences[i][1]);
        else { total += ce - cs; cs = fences[i][0]; ce = fences[i][1]; }
    }
    total += ce - cs;
    return total;
}

// =====================================================================
// Test framework
// =====================================================================

int tests_passed = 0;
int tests_total = 0;

void check(bool condition, const string& name) {
    tests_total++;
    if (condition) {
        tests_passed++;
    } else {
        cout << "  FAIL: " << name << endl;
    }
}

// =====================================================================
// Test functions
// =====================================================================

void test_w1_generate_permutations() {
    cout << "Testing W1: Generate All Permutations..." << endl;
    check(ref_generate_permutations({1,2,3}).size() == 6, "3 elements -> 6 perms");
    check(ref_generate_permutations({1,2,3})[0] == vector<int>{1,2,3}, "first perm is sorted");
    check(ref_generate_permutations({0,1}) == vector<vector<int>>{{0,1},{1,0}}, "2 elements");
    check(ref_generate_permutations({5}).size() == 1, "single element");
    check(ref_generate_permutations({3,1,2}).size() == 6, "unsorted input -> 6 perms");
    check(ref_generate_permutations({3,1,2})[0] == vector<int>{1,2,3}, "unsorted sorted first");
}

void test_w2_generate_subsets() {
    cout << "Testing W2: Generate All Subsets..." << endl;
    auto r = ref_generate_subsets({1,2,3});
    check(r.size() == 8, "3 elements -> 8 subsets");
    check(r[0] == vector<int>{}, "first subset is empty");
    check(ref_generate_subsets({}).size() == 1, "empty -> 1 subset");
    check(ref_generate_subsets({0}).size() == 2, "1 element -> 2 subsets");
    check(ref_generate_subsets({5,3}).size() == 4, "2 elements -> 4 subsets");
    check(ref_generate_subsets({1,2,3,4}).size() == 16, "4 elements -> 16 subsets");
}

void test_w3_simulate_robot() {
    cout << "Testing W3: Simulate Robot Moves..." << endl;
    check(ref_simulate_robot("UURRDDLL") == vector<int>{0,0}, "round trip");
    check(ref_simulate_robot("UUU") == vector<int>{0,3}, "up only");
    check(ref_simulate_robot("RRUULL") == vector<int>{0,2}, "right then up then left");
    check(ref_simulate_robot("") == vector<int>{0,0}, "empty commands");
    check(ref_simulate_robot("RRRRR") == vector<int>{5,0}, "all right");
    check(ref_simulate_robot("UDLR") == vector<int>{0,0}, "cancel out");
}

void test_w4_count_binary_strings() {
    cout << "Testing W4: Count Binary Strings..." << endl;
    check(ref_count_binary_strings(1) == 2, "n=1");
    check(ref_count_binary_strings(2) == 3, "n=2");
    check(ref_count_binary_strings(3) == 5, "n=3");
    check(ref_count_binary_strings(4) == 8, "n=4");
    check(ref_count_binary_strings(5) == 13, "n=5");
    check(ref_count_binary_strings(10) == 144, "n=10");
}

void test_w5_tic_tac_toe() {
    cout << "Testing W5: Tic-Tac-Toe Winner..." << endl;
    check(ref_tic_tac_toe({{"X","X","X"},{"O","O","."},{".",".","."}} ) == "X", "X wins row");
    check(ref_tic_tac_toe({{"X","O","."},{"X","O","."},{"X",".","."}} ) == "X", "X wins col");
    check(ref_tic_tac_toe({{"O","X","X"},{"X","O","."},{".",".","O"}} ) == "O", "O wins diag");
    check(ref_tic_tac_toe({{"X","O","X"},{"O","X","O"},{"O","X","O"}} ) == "Draw", "draw");
    check(ref_tic_tac_toe({{"X","O","."},{".",".","."},{".",".","."}}) == "Ongoing", "ongoing");
    check(ref_tic_tac_toe({{".",".","."},{".",".","."},{".",".","."}} ) == "Ongoing", "all empty");
}

void test_p1_subsets_bitmask() {
    cout << "Testing P1: Subsets Using Bitmasks..." << endl;
    auto r = ref_subsets_bitmask({1,2,3});
    check(r.size() == 8, "3 elements -> 8 subsets");
    check(r[0] == vector<int>{}, "first is empty");
    check(ref_subsets_bitmask({}).size() == 1, "empty input");
    check(ref_subsets_bitmask({5}).size() == 2, "single element");
    check(ref_subsets_bitmask({3,1}).size() == 4, "two elements");

    // Verify bitmask and recursion produce same result
    auto a = ref_generate_subsets({2,3,5});
    auto b = ref_subsets_bitmask({2,3,5});
    check(a == b, "bitmask matches recursive subsets");
}

void test_p2_n_queens_count() {
    cout << "Testing P2: N-Queens Count..." << endl;
    check(ref_n_queens_count(1) == 1, "n=1");
    check(ref_n_queens_count(2) == 0, "n=2");
    check(ref_n_queens_count(3) == 0, "n=3");
    check(ref_n_queens_count(4) == 2, "n=4");
    check(ref_n_queens_count(5) == 10, "n=5");
    check(ref_n_queens_count(8) == 92, "n=8");
}

void test_p3_rat_in_maze() {
    cout << "Testing P3: Rat in a Maze..." << endl;
    auto r1 = ref_rat_in_maze({{1,0,0,0},{1,1,0,1},{1,1,0,0},{0,1,1,1}});
    check(r1.size() == 2, "4x4 maze -> 2 paths");
    check(r1[0] == "DDRDRR", "first path DDRDRR");
    check(r1[1] == "DRDDRR", "second path DRDDRR");
    check(ref_rat_in_maze({{1,0},{0,1}}).empty(), "blocked maze");
    check(ref_rat_in_maze({{1}}) == vector<string>{""}, "1x1 maze");
    check(ref_rat_in_maze({{0}}).empty(), "blocked start");
    auto r5 = ref_rat_in_maze({{1,1},{1,1}});
    check(r5.size() == 2, "2x2 open -> 2 paths");
}

void test_p4_letter_combinations() {
    cout << "Testing P4: Letter Combinations..." << endl;
    auto r = ref_letter_combinations("23");
    check(r.size() == 9, "digits 23 -> 9 combos");
    check(r[0] == "ad", "first combo");
    check(ref_letter_combinations("").empty(), "empty digits");
    check(ref_letter_combinations("7").size() == 4, "digit 7 -> 4 letters");
    check(ref_letter_combinations("9").size() == 4, "digit 9 -> 4 letters");
    check(ref_letter_combinations("234").size() == 27, "3 digits -> 27 combos");
}

void test_p5_combination_sum() {
    cout << "Testing P5: Combination Sum..." << endl;
    auto r1 = ref_combination_sum({2,3,6,7}, 7);
    check(r1.size() == 2, "target 7 -> 2 combos");
    check(r1[0] == vector<int>{2,2,3}, "first combo [2,2,3]");
    check(r1[1] == vector<int>{7}, "second combo [7]");
    auto r2 = ref_combination_sum({2,3,5}, 8);
    check(r2.size() == 3, "target 8 -> 3 combos");
    check(ref_combination_sum({2}, 1).empty(), "impossible target");
    check(ref_combination_sum({1}, 3).size() == 1, "[1] target 3 -> [[1,1,1]]");
}

void test_c1_sudoku_solver() {
    cout << "Testing C1: Sudoku Solver..." << endl;
    vector<vector<int>> board = {
        {5,3,0,0,7,0,0,0,0},
        {6,0,0,1,9,5,0,0,0},
        {0,9,8,0,0,0,0,6,0},
        {8,0,0,0,6,0,0,0,3},
        {4,0,0,8,0,3,0,0,1},
        {7,0,0,0,2,0,0,0,6},
        {0,6,0,0,0,0,2,8,0},
        {0,0,0,4,1,9,0,0,5},
        {0,0,0,0,8,0,0,7,9}
    };
    auto result = ref_sudoku_solver(board);
    check(is_valid_sudoku(result), "solution is valid sudoku");
    check(result[0][0] == 5, "given cell preserved");
    check(result[0][2] != 0, "empty cell filled");

    // Second puzzle
    vector<vector<int>> board2 = {
        {0,0,0,2,6,0,7,0,1},
        {6,8,0,0,7,0,0,9,0},
        {1,9,0,0,0,4,5,0,0},
        {8,2,0,1,0,0,0,4,0},
        {0,0,4,6,0,2,9,0,0},
        {0,5,0,0,0,3,0,2,8},
        {0,0,9,3,0,0,0,7,4},
        {0,4,0,0,5,0,0,3,6},
        {7,0,3,0,1,8,0,0,0}
    };
    auto result2 = ref_sudoku_solver(board2);
    check(is_valid_sudoku(result2), "second puzzle valid");
}

void test_c2_word_search() {
    cout << "Testing C2: Word Search..." << endl;
    vector<vector<char>> board = {
        {'A','B','C','E'},
        {'S','F','C','S'},
        {'A','D','E','E'}
    };
    check(ref_word_search(board, "ABCCED") == true, "ABCCED exists");
    check(ref_word_search(board, "SEE") == true, "SEE exists");
    check(ref_word_search(board, "ABCB") == false, "ABCB doesn't exist");
    check(ref_word_search({{'A'}}, "A") == true, "single cell match");
    check(ref_word_search({{'A'}}, "B") == false, "single cell no match");
    check(ref_word_search({{'A','B'},{'C','D'}}, "ABDC") == true, "2x2 path");
}

void test_c3_n_queens_all() {
    cout << "Testing C3: N-Queens All Solutions..." << endl;
    auto r1 = ref_n_queens_all(1);
    check(r1.size() == 1, "n=1 -> 1 solution");
    check(r1[0] == vector<string>{"Q"}, "n=1 board is Q");
    auto r4 = ref_n_queens_all(4);
    check(r4.size() == 2, "n=4 -> 2 solutions");
    check(r4[0][0] == "..Q.", "first 4-queen solution row 0");
    auto r8 = ref_n_queens_all(8);
    check(r8.size() == 92, "n=8 -> 92 solutions");
    // Verify each solution row has exactly one Q
    for (auto& sol : r4) {
        for (auto& row : sol) {
            int q_count = 0;
            for (char c : row) if (c == 'Q') q_count++;
            check(q_count == 1, "each row has one Q");
        }
    }
}

void test_c4_fence_painting() {
    cout << "Testing C4: Fence Painting..." << endl;
    check(ref_fence_painting({{0,5},{3,8}}) == 8, "overlapping");
    check(ref_fence_painting({{1,3},{5,7}}) == 4, "non-overlapping");
    check(ref_fence_painting({{0,10},{2,6}}) == 10, "contained");
    check(ref_fence_painting({}) == 0, "empty");
    check(ref_fence_painting({{0,5}}) == 5, "single fence");
    check(ref_fence_painting({{0,3},{3,6},{6,10}}) == 10, "touching");
    check(ref_fence_painting({{5,10},{1,3},{2,7}}) == 9, "unsorted overlapping");
}

// =====================================================================
// Main
// =====================================================================

int main() {
    test_w1_generate_permutations();
    test_w2_generate_subsets();
    test_w3_simulate_robot();
    test_w4_count_binary_strings();
    test_w5_tic_tac_toe();
    test_p1_subsets_bitmask();
    test_p2_n_queens_count();
    test_p3_rat_in_maze();
    test_p4_letter_combinations();
    test_p5_combination_sum();
    test_c1_sudoku_solver();
    test_c2_word_search();
    test_c3_n_queens_all();
    test_c4_fence_painting();

    cout << endl;
    if (tests_passed == tests_total) {
        cout << "All " << tests_total << " tests passed!" << endl;
    } else {
        cout << tests_passed << " / " << tests_total << " tests passed." << endl;
    }
    return (tests_passed == tests_total) ? 0 : 1;
}
