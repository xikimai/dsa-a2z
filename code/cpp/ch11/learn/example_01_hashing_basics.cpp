/*
 * Example 1: Hashing Basics
 * ==========================
 * Chapter 11: Hashing — The Secret Decoder Ring
 *
 * Demonstrates the fundamental hash-based containers in C++:
 *   Part 1: unordered_set (insert, count, size, timing vs vector find)
 *   Part 2: unordered_map (insert, [], at, count, iteration, frequency counting)
 *   Part 3: Collision demo (hash values mod a small table size)
 *   Part 4: Performance comparison (unordered_set vs vector find vs binary search)
 */

#include <algorithm>
#include <chrono>
#include <iostream>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

// ---------- Part 1: unordered_set demo ----------
void part1_unordered_set() {
    cout << "=== Part 1: unordered_set ===" << endl;

    unordered_set<int> seen;

    // Insert elements
    seen.insert(10);
    seen.insert(20);
    seen.insert(30);
    seen.insert(20);  // duplicate — ignored

    cout << "Size after inserting {10,20,30,20}: " << seen.size() << endl;
    // => 3

    // Check membership with count (returns 0 or 1)
    cout << "Contains 20? " << (seen.count(20) ? "yes" : "no") << endl;
    cout << "Contains 99? " << (seen.count(99) ? "yes" : "no") << endl;

    // Erase an element
    seen.erase(10);
    cout << "Size after erasing 10: " << seen.size() << endl;

    // Iterate (order is NOT guaranteed)
    cout << "Elements: ";
    for (int x : seen) cout << x << " ";
    cout << endl;

    // Timing: unordered_set lookup vs linear search in a vector
    const int N = 100000;
    vector<int> v;
    unordered_set<int> s;
    for (int i = 0; i < N; i++) {
        v.push_back(i);
        s.insert(i);
    }

    auto t1 = chrono::high_resolution_clock::now();
    for (int i = 0; i < 1000; i++) {
        volatile bool found = (find(v.begin(), v.end(), N - 1) != v.end());
        (void)found;
    }
    auto t2 = chrono::high_resolution_clock::now();
    auto vec_us = chrono::duration_cast<chrono::microseconds>(t2 - t1).count();

    t1 = chrono::high_resolution_clock::now();
    for (int i = 0; i < 1000; i++) {
        volatile bool found = (s.count(N - 1) > 0);
        (void)found;
    }
    t2 = chrono::high_resolution_clock::now();
    auto set_us = chrono::duration_cast<chrono::microseconds>(t2 - t1).count();

    cout << "1000 lookups (worst-case element):" << endl;
    cout << "  vector find : " << vec_us << " us" << endl;
    cout << "  unordered_set: " << set_us << " us" << endl;
    cout << endl;
}

// ---------- Part 2: unordered_map demo ----------
void part2_unordered_map() {
    cout << "=== Part 2: unordered_map ===" << endl;

    unordered_map<string, int> ages;

    // Insert with []
    ages["Alice"] = 14;
    ages["Bob"] = 15;
    ages["Charlie"] = 14;

    // Access with []
    cout << "Alice's age: " << ages["Alice"] << endl;

    // Access with at() — throws if key missing
    cout << "Bob's age: " << ages.at("Bob") << endl;

    // Check existence with count()
    cout << "Has 'Dave'? " << (ages.count("Dave") ? "yes" : "no") << endl;

    // [] on missing key creates it with default value (0 for int)
    cout << "ages['Dave'] (auto-created): " << ages["Dave"] << endl;
    cout << "Has 'Dave' now? " << (ages.count("Dave") ? "yes" : "no") << endl;

    // Iteration (order NOT guaranteed)
    cout << "All entries:" << endl;
    for (auto& [name, age] : ages) {
        cout << "  " << name << " -> " << age << endl;
    }

    // Frequency counting — the bread and butter of hashing
    cout << "\nFrequency counting demo:" << endl;
    vector<string> words = {"apple", "banana", "apple", "cherry", "banana", "apple"};
    unordered_map<string, int> freq;
    for (const string& w : words) {
        freq[w]++;  // auto-initialises to 0, then increments
    }
    for (auto& [word, cnt] : freq) {
        cout << "  " << word << ": " << cnt << endl;
    }
    cout << endl;
}

// ---------- Part 3: Collision demo ----------
void part3_collisions() {
    cout << "=== Part 3: Collision Demo ===" << endl;

    // Simulate a tiny hash table with 7 buckets
    const int TABLE_SIZE = 7;
    hash<int> hasher;

    vector<int> keys = {10, 17, 24, 31, 3, 38};
    cout << "Hash values mod " << TABLE_SIZE << ":" << endl;
    for (int k : keys) {
        size_t h = hasher(k);
        cout << "  key=" << k << "  hash=" << h
             << "  bucket=" << (h % TABLE_SIZE) << endl;
    }
    cout << "(Collisions happen when two keys land in the same bucket)" << endl;

    // Show actual bucket info from an unordered_set
    unordered_set<int> s(keys.begin(), keys.end());
    cout << "\nunordered_set internal stats:" << endl;
    cout << "  bucket_count : " << s.bucket_count() << endl;
    cout << "  load_factor  : " << s.load_factor() << endl;
    cout << "  max_load_factor: " << s.max_load_factor() << endl;
    cout << endl;
}

// ---------- Part 4: Performance comparison ----------
void part4_performance() {
    cout << "=== Part 4: Performance Comparison ===" << endl;

    const int N = 200000;
    vector<int> data;
    for (int i = 0; i < N; i++) data.push_back(i);

    // Build structures
    unordered_set<int> uset(data.begin(), data.end());
    vector<int> sorted_data = data;  // already sorted here

    // Lookups: 10000 random-ish queries
    vector<int> queries;
    for (int i = 0; i < 10000; i++) queries.push_back((i * 7919) % N);

    // 1. vector find — O(n) each
    auto t1 = chrono::high_resolution_clock::now();
    int found1 = 0;
    for (int q : queries) {
        if (find(data.begin(), data.end(), q) != data.end()) found1++;
    }
    auto t2 = chrono::high_resolution_clock::now();
    auto vec_ms = chrono::duration_cast<chrono::milliseconds>(t2 - t1).count();

    // 2. binary search — O(log n) each
    t1 = chrono::high_resolution_clock::now();
    int found2 = 0;
    for (int q : queries) {
        if (binary_search(sorted_data.begin(), sorted_data.end(), q)) found2++;
    }
    t2 = chrono::high_resolution_clock::now();
    auto bs_ms = chrono::duration_cast<chrono::milliseconds>(t2 - t1).count();

    // 3. unordered_set — O(1) average each
    t1 = chrono::high_resolution_clock::now();
    int found3 = 0;
    for (int q : queries) {
        if (uset.count(q)) found3++;
    }
    t2 = chrono::high_resolution_clock::now();
    auto uset_ms = chrono::duration_cast<chrono::milliseconds>(t2 - t1).count();

    cout << "10000 lookups in " << N << " elements:" << endl;
    cout << "  vector find    : " << vec_ms << " ms (found " << found1 << ")" << endl;
    cout << "  binary_search  : " << bs_ms << " ms (found " << found2 << ")" << endl;
    cout << "  unordered_set  : " << uset_ms << " ms (found " << found3 << ")" << endl;
    cout << endl;
}

int main() {
    part1_unordered_set();
    part2_unordered_map();
    part3_collisions();
    part4_performance();
    return 0;
}
