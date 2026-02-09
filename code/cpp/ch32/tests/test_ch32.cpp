/*
 * Tests for Chapter 32: String Algorithms — Beyond Brute Force
 * Build: g++ -std=c++17 -o /tmp/test_ch32 code/cpp/ch32/tests/test_ch32.cpp && /tmp/test_ch32
 */

#include <algorithm>
#include <cassert>
#include <climits>
#include <iostream>
#include <set>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

// =====================================================================
// Reference solutions (uniquely named with ref_ prefix)
// =====================================================================

// ── Trie Node for W1, W2 ────────────────────────────────────────
struct RefTrieNode {
    RefTrieNode* ch[26] = {};
    bool isEnd = false;
    int cnt = 0;
};

// W1: Trie Insert and Search
vector<bool> ref_trie_search(vector<string> words, vector<string> queries) {
    RefTrieNode* root = new RefTrieNode();
    for (auto& w : words) {
        RefTrieNode* n = root;
        for (char c : w) {
            int i = c - 'a';
            if (!n->ch[i]) n->ch[i] = new RefTrieNode();
            n = n->ch[i];
        }
        n->isEnd = true;
    }
    vector<bool> res;
    for (auto& q : queries) {
        RefTrieNode* n = root;
        bool found = true;
        for (char c : q) {
            int i = c - 'a';
            if (!n->ch[i]) { found = false; break; }
            n = n->ch[i];
        }
        res.push_back(found && n->isEnd);
    }
    return res;
}

// W2: Trie Prefix Count
vector<int> ref_trie_prefix_count(vector<string> words, vector<string> prefixes) {
    RefTrieNode* root = new RefTrieNode();
    for (auto& w : words) {
        RefTrieNode* n = root;
        for (char c : w) {
            int i = c - 'a';
            if (!n->ch[i]) n->ch[i] = new RefTrieNode();
            n = n->ch[i];
            n->cnt++;
        }
    }
    vector<int> res;
    for (auto& p : prefixes) {
        RefTrieNode* n = root;
        bool found = true;
        for (char c : p) {
            int i = c - 'a';
            if (!n->ch[i]) { found = false; break; }
            n = n->ch[i];
        }
        res.push_back(found ? n->cnt : 0);
    }
    return res;
}

// W3: KMP Pattern Search
vector<int> ref_kmp_search(string text, string pattern) {
    int n = text.size(), m = pattern.size();
    vector<int> matches;
    if (m == 0) return matches;
    vector<int> fail(m, 0);
    int len = 0, i = 1;
    while (i < m) {
        if (pattern[i] == pattern[len]) fail[i++] = ++len;
        else if (len > 0) len = fail[len - 1];
        else fail[i++] = 0;
    }
    int j = 0;
    for (i = 0; i < n; i++) {
        while (j > 0 && text[i] != pattern[j]) j = fail[j - 1];
        if (text[i] == pattern[j]) j++;
        if (j == m) { matches.push_back(i - m + 1); j = fail[j - 1]; }
    }
    return matches;
}

// W4: Z-Function
vector<int> ref_z_function(string s) {
    int n = s.size();
    vector<int> z(n, 0);
    int l = 0, r = 0;
    for (int i = 1; i < n; i++) {
        if (i < r) z[i] = min(r - i, z[i - l]);
        while (i + z[i] < n && s[z[i]] == s[i + z[i]]) z[i]++;
        if (i + z[i] > r) { l = i; r = i + z[i]; }
    }
    return z;
}

// P1: Rabin-Karp Pattern Search
vector<int> ref_rabin_karp(string text, string pattern) {
    int n = text.size(), m = pattern.size();
    vector<int> matches;
    if (m == 0 || m > n) return matches;
    long long BASE = 131, MOD = 1e9 + 7;
    long long pH = 0, tH = 0, pw = 1;
    for (int i = 0; i < m - 1; i++) pw = pw * BASE % MOD;
    for (int i = 0; i < m; i++) {
        pH = (pH * BASE + pattern[i]) % MOD;
        tH = (tH * BASE + text[i]) % MOD;
    }
    for (int i = 0; i <= n - m; i++) {
        if (pH == tH && text.substr(i, m) == pattern) matches.push_back(i);
        if (i < n - m)
            tH = ((tH - text[i] * pw % MOD + MOD) * BASE + text[i + m]) % MOD;
    }
    return matches;
}

// P2: Longest Common Prefix
string ref_lcp(vector<string> words) {
    if (words.empty()) return "";
    string prefix;
    for (int i = 0; i < (int)words[0].size(); i++) {
        char c = words[0][i];
        for (int j = 1; j < (int)words.size(); j++)
            if (i >= (int)words[j].size() || words[j][i] != c) return prefix;
        prefix += c;
    }
    return prefix;
}

// P3: Count Distinct Substrings
int ref_distinct_substrings(string s) {
    set<string> subs;
    int n = s.size();
    for (int i = 0; i < n; i++)
        for (int j = i + 1; j <= n; j++)
            subs.insert(s.substr(i, j - i));
    return subs.size() + 1;
}

// P4: Repeated String Match
int ref_repeated_string(string a, string b) {
    if (a.empty() || b.empty()) return b.empty() ? 1 : -1;
    int reps = (b.size() + a.size() - 1) / a.size();
    string rep;
    for (int i = 0; i < reps; i++) rep += a;
    if (rep.find(b) != string::npos) return reps;
    rep += a;
    if (rep.find(b) != string::npos) return reps + 1;
    return -1;
}

// P5: Longest Happy Prefix
string ref_happy_prefix(string s) {
    int n = s.size();
    if (n <= 1) return "";
    vector<int> fail(n, 0);
    int len = 0, i = 1;
    while (i < n) {
        if (s[i] == s[len]) fail[i++] = ++len;
        else if (len > 0) len = fail[len - 1];
        else fail[i++] = 0;
    }
    return s.substr(0, fail[n - 1]);
}

// C1: Word Search II
struct C1Trie {
    C1Trie* ch[26] = {};
    string word;
};

void c1_dfs(vector<vector<char>>& board, int r, int c, C1Trie* node,
            vector<string>& res, int R, int C) {
    char ch = board[r][c];
    if (ch == '.' || !node->ch[ch - 'a']) return;
    C1Trie* next = node->ch[ch - 'a'];
    if (!next->word.empty()) { res.push_back(next->word); next->word.clear(); }
    board[r][c] = '.';
    int d[][2] = {{-1,0},{1,0},{0,-1},{0,1}};
    for (auto& dd : d) {
        int nr = r + dd[0], nc = c + dd[1];
        if (nr >= 0 && nr < R && nc >= 0 && nc < C && board[nr][nc] != '.')
            c1_dfs(board, nr, nc, next, res, R, C);
    }
    board[r][c] = ch;
}

vector<string> ref_word_search_ii(vector<vector<char>> board, vector<string> words) {
    C1Trie* root = new C1Trie();
    for (auto& w : words) {
        C1Trie* n = root;
        for (char c : w) {
            int i = c - 'a';
            if (!n->ch[i]) n->ch[i] = new C1Trie();
            n = n->ch[i];
        }
        n->word = w;
    }
    int R = board.size(), C = board[0].size();
    vector<string> res;
    for (int r = 0; r < R; r++)
        for (int c = 0; c < C; c++)
            c1_dfs(board, r, c, root, res, R, C);
    sort(res.begin(), res.end());
    return res;
}

// C2: Shortest Palindrome
string ref_shortest_palindrome(string s) {
    if (s.size() <= 1) return s;
    string rev = s;
    reverse(rev.begin(), rev.end());
    string combined = s + "#" + rev;
    int n = combined.size();
    vector<int> fail(n, 0);
    int len = 0, i = 1;
    while (i < n) {
        if (combined[i] == combined[len]) fail[i++] = ++len;
        else if (len > 0) len = fail[len - 1];
        else fail[i++] = 0;
    }
    return rev.substr(0, s.size() - fail[n - 1]) + s;
}

// C3: Distinct Substrings of Length K
int ref_distinct_k(string s, int k) {
    int n = s.size();
    if (k > n) return 0;
    set<string> seen;
    for (int i = 0; i <= n - k; i++)
        seen.insert(s.substr(i, k));
    return seen.size();
}

// =====================================================================
// Test runner
// =====================================================================

int passed_count = 0, failed_count = 0;

void check(bool condition, const string& msg) {
    if (condition) { passed_count++; }
    else { failed_count++; cout << "FAIL: " << msg << endl; }
}

void check_vec(vector<int> expected, vector<int> actual, const string& msg) {
    if (expected == actual) { passed_count++; }
    else {
        failed_count++;
        cout << "FAIL: " << msg << " — expected [";
        for (int i = 0; i < (int)expected.size(); i++) cout << (i?",":"") << expected[i];
        cout << "], got [";
        for (int i = 0; i < (int)actual.size(); i++) cout << (i?",":"") << actual[i];
        cout << "]" << endl;
    }
}

void check_bool_vec(vector<bool> expected, vector<bool> actual, const string& msg) {
    if (expected == actual) { passed_count++; }
    else { failed_count++; cout << "FAIL: " << msg << endl; }
}

void check_str(const string& expected, const string& actual, const string& msg) {
    if (expected == actual) { passed_count++; }
    else { failed_count++; cout << "FAIL: " << msg << " — expected '" << expected << "', got '" << actual << "'" << endl; }
}

void check_str_vec(vector<string> expected, vector<string> actual, const string& msg) {
    if (expected == actual) { passed_count++; }
    else { failed_count++; cout << "FAIL: " << msg << endl; }
}

void check_int(int expected, int actual, const string& msg) {
    if (expected == actual) { passed_count++; }
    else { failed_count++; cout << "FAIL: " << msg << " — expected " << expected << ", got " << actual << endl; }
}

int main() {
    cout << "Chapter 32: String Algorithms — Beyond Brute Force" << endl;
    cout << "================================================================" << endl << endl;

    // W1: Trie Insert and Search
    check_bool_vec({true,true,false,true},
        ref_trie_search({"apple","app","banana"}, {"app","apple","ban","banana"}), "W1: basic");
    check_bool_vec({true,false,false},
        ref_trie_search({"hello"}, {"hello","hell","helloo"}), "W1: single word");
    check_bool_vec({false,true},
        ref_trie_search({"application"}, {"app","application"}), "W1: prefix not word");

    // W2: Trie Prefix Count
    check_vec({3,4,1,0},
        ref_trie_prefix_count({"apple","app","application","apt","banana"}, {"app","a","ban","c"}), "W2: basic");
    check_vec({3,3},
        ref_trie_prefix_count({"test","testing","tested"}, {"test","tes"}), "W2: same prefix");
    check_vec({0},
        ref_trie_prefix_count({"abc","abd"}, {"xyz"}), "W2: no match");

    // W3: KMP Pattern Search
    check_vec({0,9,12}, ref_kmp_search("AABAACAADAABAABA", "AABA"), "W3: multiple matches");
    check_vec({0,3}, ref_kmp_search("ABCABC", "ABC"), "W3: two matches");
    check_vec({0,1,2,3}, ref_kmp_search("AAAAA", "AA"), "W3: overlapping");
    check_vec({}, ref_kmp_search("HELLO", "WORLD"), "W3: no match");

    // W4: Z-Function
    check_vec({0,1,0,0,2,1}, ref_z_function("aabxaa"), "W4: mixed");
    check_vec({0,4,3,2,1}, ref_z_function("aaaaa"), "W4: all same");
    check_vec({0,0,0,0,0,0}, ref_z_function("abcdef"), "W4: all different");

    // P1: Rabin-Karp
    check_vec({0,9,12}, ref_rabin_karp("AABAACAADAABAABA", "AABA"), "P1: multiple matches");
    check_vec({0,2,4}, ref_rabin_karp("ABABABAB", "ABAB"), "P1: overlapping");
    check_vec({0}, ref_rabin_karp("HELLO", "HELLO"), "P1: full match");

    // P2: Longest Common Prefix
    check_str("fl", ref_lcp({"flower","flow","flight"}), "P2: partial");
    check_str("", ref_lcp({"dog","racecar","car"}), "P2: none");
    check_str("inter", ref_lcp({"interstellar","internet","internal"}), "P2: longer");
    check_str("a", ref_lcp({"a"}), "P2: single");

    // P3: Count Distinct Substrings
    check_int(8, ref_distinct_substrings("abab"), "P3: abab");
    check_int(4, ref_distinct_substrings("aaa"), "P3: aaa");
    check_int(7, ref_distinct_substrings("abc"), "P3: abc");

    // P4: Repeated String Match
    check_int(3, ref_repeated_string("abcd", "cdabcdab"), "P4: three repeats");
    check_int(2, ref_repeated_string("a", "aa"), "P4: two repeats");
    check_int(-1, ref_repeated_string("abc", "xyz"), "P4: impossible");
    check_int(1, ref_repeated_string("abc", "abc"), "P4: one repeat");

    // P5: Longest Happy Prefix
    check_str("l", ref_happy_prefix("level"), "P5: level");
    check_str("abab", ref_happy_prefix("ababab"), "P5: ababab");
    check_str("", ref_happy_prefix("a"), "P5: single");
    check_str("abc", ref_happy_prefix("abcabc"), "P5: abcabc");

    // C1: Word Search II
    check_str_vec({"eat","oath"},
        ref_word_search_ii({{'o','a','a','n'},{'e','t','a','e'},{'i','h','k','r'},{'i','f','l','v'}},
                           {"oath","pea","eat","rain"}), "C1: basic");
    check_str_vec({},
        ref_word_search_ii({{'a','b'},{'c','d'}}, {"abcb"}), "C1: no match");

    // C2: Shortest Palindrome
    check_str("aaacecaaa", ref_shortest_palindrome("aacecaaa"), "C2: almost palindrome");
    check_str("dcbabcd", ref_shortest_palindrome("abcd"), "C2: no palindrome");
    check_str("a", ref_shortest_palindrome("a"), "C2: single");
    check_str("", ref_shortest_palindrome(""), "C2: empty");

    // C3: Distinct Substrings of Length K
    check_int(3, ref_distinct_k("abcabc", 3), "C3: abc");
    check_int(1, ref_distinct_k("aaaa", 2), "C3: all same");
    check_int(6, ref_distinct_k("abcdef", 1), "C3: all different");

    cout << endl;
    if (failed_count == 0) {
        printf("All %d ch32 C++ tests passed!\n", passed_count);
    } else {
        printf("%d passed, %d failed.\n", passed_count, failed_count);
        return 1;
    }
    return 0;
}
