/*
 * Example 2: Hashing Patterns
 * ============================
 * Chapter 11: Hashing — The Secret Decoder Ring
 *
 * Demonstrates four essential hashing patterns:
 *   Part 1: Frequency counting pattern
 *   Part 2: Complement technique (Two Sum trace)
 *   Part 3: Prefix sum + unordered_map
 *   Part 4: Anagram grouping demo
 */

#include <algorithm>
#include <iostream>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

// ---------- Part 1: Frequency counting pattern ----------
void part1_frequency_counting() {
    cout << "=== Part 1: Frequency Counting Pattern ===" << endl;

    // The most common hashing pattern: count occurrences
    vector<int> nums = {4, 1, 2, 1, 2, 4, 4, 3};

    unordered_map<int, int> freq;
    for (int x : nums) {
        freq[x]++;  // key auto-created with value 0, then incremented
    }

    cout << "Array: {4, 1, 2, 1, 2, 4, 4, 3}" << endl;
    cout << "Frequencies:" << endl;
    for (auto& [val, cnt] : freq) {
        cout << "  " << val << " appears " << cnt << " time(s)" << endl;
    }

    // Find the most frequent element
    int max_val = 0, max_cnt = 0;
    for (auto& [val, cnt] : freq) {
        if (cnt > max_cnt) {
            max_cnt = cnt;
            max_val = val;
        }
    }
    cout << "Most frequent: " << max_val << " (" << max_cnt << " times)" << endl;

    // Character frequency in a string
    string word = "mississippi";
    unordered_map<char, int> char_freq;
    for (char c : word) char_freq[c]++;
    cout << "\nCharacter frequencies in \"" << word << "\":" << endl;
    for (auto& [ch, cnt] : char_freq) {
        cout << "  '" << ch << "' -> " << cnt << endl;
    }
    cout << endl;
}

// ---------- Part 2: Complement technique (Two Sum trace) ----------
void part2_complement_technique() {
    cout << "=== Part 2: Complement Technique (Two Sum) ===" << endl;

    // Problem: find two indices whose values sum to target
    vector<int> nums = {2, 7, 11, 15};
    int target = 9;

    cout << "Array: {2, 7, 11, 15}, target = " << target << endl;
    cout << "Step-by-step trace:" << endl;

    unordered_map<int, int> seen;  // value -> index
    for (int i = 0; i < (int)nums.size(); i++) {
        int complement = target - nums[i];
        cout << "  i=" << i << ", nums[i]=" << nums[i]
             << ", complement=" << complement;

        if (seen.count(complement)) {
            cout << " -> FOUND at index " << seen[complement] << "!" << endl;
            cout << "\nAnswer: indices {" << seen[complement] << ", " << i << "}" << endl;
            break;
        } else {
            cout << " -> not in map, storing " << nums[i] << "->" << i << endl;
            seen[nums[i]] = i;
        }
    }

    // Key insight: instead of checking all pairs O(n^2),
    // we ask: "Have I already seen my complement?" — O(1) per lookup.
    cout << "\nWhy O(n): each element is inserted and looked up at most once." << endl;
    cout << endl;
}

// ---------- Part 3: Prefix sum + unordered_map ----------
void part3_prefix_sum_map() {
    cout << "=== Part 3: Prefix Sum + Hash Map ===" << endl;

    // Problem: count subarrays with sum == k
    vector<int> arr = {1, 2, 3, -2, 5};
    int k = 3;

    cout << "Array: {1, 2, 3, -2, 5}, k = " << k << endl;
    cout << "Step-by-step trace:" << endl;

    unordered_map<int, int> prefix_count;
    prefix_count[0] = 1;  // empty prefix has sum 0
    int prefix_sum = 0;
    int count = 0;

    for (int i = 0; i < (int)arr.size(); i++) {
        prefix_sum += arr[i];
        int need = prefix_sum - k;

        cout << "  i=" << i << ", arr[i]=" << arr[i]
             << ", prefix_sum=" << prefix_sum
             << ", need=" << need;

        if (prefix_count.count(need)) {
            count += prefix_count[need];
            cout << " -> found " << prefix_count[need] << " match(es)";
        }
        prefix_count[prefix_sum]++;
        cout << endl;
    }

    cout << "\nTotal subarrays with sum " << k << ": " << count << endl;
    cout << "\nKey insight: if prefix_sum[j] - prefix_sum[i] == k," << endl;
    cout << "then subarr [i+1..j] has sum k. We track prefix sums in a map." << endl;
    cout << endl;
}

// ---------- Part 4: Anagram grouping demo ----------
void part4_anagram_grouping() {
    cout << "=== Part 4: Anagram Grouping ===" << endl;

    vector<string> words = {"eat", "tea", "tan", "ate", "nat", "bat"};

    cout << "Words: {\"eat\", \"tea\", \"tan\", \"ate\", \"nat\", \"bat\"}" << endl;
    cout << "Step-by-step:" << endl;

    // Key idea: two words are anagrams if they have the same sorted characters
    unordered_map<string, vector<string>> groups;
    for (const string& w : words) {
        string key = w;
        sort(key.begin(), key.end());  // "eat" -> "aet", "tea" -> "aet"
        cout << "  \"" << w << "\" -> key \"" << key << "\"" << endl;
        groups[key].push_back(w);
    }

    cout << "\nGrouped anagrams:" << endl;
    for (auto& [key, group] : groups) {
        cout << "  key=\"" << key << "\": {";
        for (int i = 0; i < (int)group.size(); i++) {
            if (i > 0) cout << ", ";
            cout << "\"" << group[i] << "\"";
        }
        cout << "}" << endl;
    }

    cout << "\nWhy O(n * k log k): n words, each sorted in O(k log k) where k = word length." << endl;
    cout << "Hash map grouping is O(1) amortised per insert/lookup." << endl;
    cout << endl;
}

int main() {
    part1_frequency_counting();
    part2_complement_technique();
    part3_prefix_sum_map();
    part4_anagram_grouping();
    return 0;
}
