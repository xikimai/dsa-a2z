/*
 * Solution for Practice 2: Accounts Merge
 * Chapter 29: Union-Find & Minimum Spanning Trees
 */
#include <algorithm>
#include <climits>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <string>
#include <vector>
using namespace std;

vector<vector<string>> solve(vector<vector<string>>& accounts) {
    map<string, int> emailToId;
    map<string, string> emailToName;
    int id = 0;

    for (auto& acc : accounts) {
        string name = acc[0];
        for (int i = 1; i < (int)acc.size(); i++) {
            if (emailToId.find(acc[i]) == emailToId.end())
                emailToId[acc[i]] = id++;
            emailToName[acc[i]] = name;
        }
    }

    vector<int> parent(id), rnk(id, 0);
    iota(parent.begin(), parent.end(), 0);
    function<int(int)> find = [&](int x) -> int {
        return parent[x] == x ? x : parent[x] = find(parent[x]);
    };
    auto unite = [&](int x, int y) {
        int rx = find(x), ry = find(y);
        if (rx == ry) return;
        if (rnk[rx] < rnk[ry]) parent[rx] = ry;
        else if (rnk[rx] > rnk[ry]) parent[ry] = rx;
        else { parent[ry] = rx; rnk[rx]++; }
    };

    for (auto& acc : accounts) {
        int firstId = emailToId[acc[1]];
        for (int i = 2; i < (int)acc.size(); i++)
            unite(firstId, emailToId[acc[i]]);
    }

    map<int, set<string>> groups;
    for (auto& [email, eid] : emailToId)
        groups[find(eid)].insert(email);

    vector<vector<string>> result;
    for (auto& [root, emails] : groups) {
        vector<string> merged;
        merged.push_back(emailToName[*emails.begin()]);
        for (auto& e : emails) merged.push_back(e);
        result.push_back(merged);
    }
    sort(result.begin(), result.end(), [](auto& a, auto& b) { return a[1] < b[1]; });
    return result;
}

int main() { return 0; }
