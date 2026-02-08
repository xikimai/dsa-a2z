/*
 * Solution for Challenge 4: LRU Cache
 * Chapter 22: Stacks & Queues — Order Matters
 * APPROACH: list (DLL) + unordered_map for O(1) get/put.
 * TIME: O(1) per op, SPACE: O(capacity)
 */
#include <iostream>
#include <list>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

vector<int> solve(int capacity, vector<vector<string>> operations) {
    list<pair<int,int>> items; // {key, value}, front = most recent
    unordered_map<int, list<pair<int,int>>::iterator> cache;
    vector<int> results;

    for (auto& op : operations) {
        if (op[0] == "get") {
            int key = stoi(op[1]);
            auto it = cache.find(key);
            if (it == cache.end()) {
                results.push_back(-1);
            } else {
                items.splice(items.begin(), items, it->second);
                results.push_back(it->second->second);
            }
        } else if (op[0] == "put") {
            int key = stoi(op[1]), value = stoi(op[2]);
            auto it = cache.find(key);
            if (it != cache.end()) {
                it->second->second = value;
                items.splice(items.begin(), items, it->second);
            } else {
                if ((int)cache.size() >= capacity) {
                    auto last = items.back();
                    cache.erase(last.first);
                    items.pop_back();
                }
                items.push_front({key, value});
                cache[key] = items.begin();
            }
        }
    }
    return results;
}

int main() {
    int capacity = 2;
    vector<vector<string>> ops = {
        {"put","1","1"},{"put","2","2"},{"get","1"},
        {"put","3","3"},{"get","2"},
        {"put","4","4"},{"get","1"},{"get","3"},{"get","4"}
    };
    for (int r : solve(capacity, ops)) cout << r << " ";
    cout << endl;
    return 0;
}
