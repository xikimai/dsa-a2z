"""
Example 02: Common Hashing Patterns in Action
==============================================
Chapter 11: Hashing — The Secret Decoder Ring

This example demonstrates:
  - Part 1: Frequency counting pattern — word frequencies in a sentence
  - Part 2: Complement technique — Two Sum walkthrough with hash map
  - Part 3: Prefix sum + hash map — subarray sum walkthrough
  - Part 4: Anagram grouping — sorted-key technique demo
"""


# ── Part 1: Frequency Counting Pattern ─────────────────────────────

def part1_frequency_counting():
    """Count word frequencies, find most/least frequent."""
    print("=" * 60)
    print("PART 1: Frequency Counting Pattern")
    print("=" * 60)

    sentence = "the cat sat on the mat and the cat ate the rat"
    words = sentence.split()
    print(f"  Sentence: \"{sentence}\"")
    print(f"  Words: {words}\n")

    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1

    print("  Frequency map:")
    for word, count in freq.items():
        bar = "#" * count
        print(f"    '{word}': {count}  {bar}")

    most_common = max(freq, key=lambda k: freq[k])
    least_common = min(freq, key=lambda k: freq[k])
    print(f"\n  Most frequent:  '{most_common}' ({freq[most_common]} times)")
    print(f"  Least frequent: '{least_common}' ({freq[least_common]} time)")


# ── Part 2: Complement Technique (Two Sum) ─────────────────────────

def part2_complement_technique():
    """Two Sum walkthrough with hash map, step by step."""
    print("\n" + "=" * 60)
    print("PART 2: Complement Technique — Two Sum Walkthrough")
    print("=" * 60)

    nums = [2, 7, 11, 15]
    target = 9
    print(f"  nums = {nums}, target = {target}")
    print(f"\n  Strategy: For each number, ask 'Have I seen its complement?'")
    print(f"  complement = target - current_number\n")

    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        print(f"  Step {i}: num = {num}, complement = {target} - {num} = {complement}")
        if complement in seen:
            print(f"    -> YES! complement {complement} was seen at index {seen[complement]}")
            print(f"    -> Answer: indices [{seen[complement]}, {i}]")
            break
        else:
            print(f"    -> Not seen yet. Store {num} -> index {i}")
            seen[num] = i
            print(f"    -> seen = {seen}")

    # Second example with more steps
    print(f"\n  --- Another example ---")
    nums2 = [3, 5, -4, 8, 11, 1, -1, 6]
    target2 = 10
    print(f"  nums = {nums2}, target = {target2}\n")

    seen2 = {}
    for i, num in enumerate(nums2):
        complement = target2 - num
        print(f"  Step {i}: num = {num}, complement = {complement}", end="")
        if complement in seen2:
            print(f"  -> FOUND! Answer: [{seen2[complement]}, {i}]")
            break
        else:
            seen2[num] = i
            print(f"  -> store {num}")


# ── Part 3: Prefix Sum + Hash Map ──────────────────────────────────

def part3_prefix_sum_hashmap():
    """Subarray sum walkthrough using prefix sums and a hash map."""
    print("\n" + "=" * 60)
    print("PART 3: Prefix Sum + Hash Map — Subarray Sum = K")
    print("=" * 60)

    arr = [1, 2, 3, -2, 5]
    k = 4
    print(f"  arr = {arr}, k = {k}")
    print(f"\n  Key insight: If prefix_sum[j] - prefix_sum[i] == k,")
    print(f"  then subarray arr[i+1..j] sums to k.\n")

    prefix_sum = 0
    prefix_map = {0: 0}  # prefix_sum -> earliest index (using 0-based prefix index)
    count = 0

    print(f"  {'Index':>5}  {'Elem':>5}  {'PrefixSum':>10}  {'Need':>5}  {'Found?':>8}  {'Map'}")
    print(f"  {'-'*5}  {'-'*5}  {'-'*10}  {'-'*5}  {'-'*8}  {'-'*30}")

    for i, num in enumerate(arr):
        prefix_sum += num
        need = prefix_sum - k
        found = need in prefix_map
        if found:
            count += 1
        print(f"  {i:>5}  {num:>5}  {prefix_sum:>10}  {need:>5}  {'YES' if found else 'no':>8}  {prefix_map}")
        if prefix_sum not in prefix_map:
            prefix_map[prefix_sum] = i + 1

    print(f"\n  Total subarrays with sum = {k}: {count}")


# ── Part 4: Anagram Grouping ──────────────────────────────────────

def part4_anagram_grouping():
    """Group words by anagram equivalence using sorted-key technique."""
    print("\n" + "=" * 60)
    print("PART 4: Anagram Grouping — Sorted-Key Technique")
    print("=" * 60)

    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(f"  Words: {words}")
    print(f"\n  Strategy: Sort each word's letters -> use as dictionary key\n")

    groups = {}
    for word in words:
        key = "".join(sorted(word))
        print(f"  '{word}' -> sorted = '{key}'", end="")
        if key not in groups:
            groups[key] = []
            print(f"  -> NEW group")
        else:
            print(f"  -> join existing group {groups[key]}")
        groups[key].append(word)

    print(f"\n  Final groups (key -> words):")
    for key, group in groups.items():
        print(f"    '{key}' -> {group}")

    # Show the result
    result = sorted([sorted(g) for g in groups.values()])
    print(f"\n  Cleaned result: {result}")


# ── Main ────────────────────────────────────────────────────────────

if __name__ == "__main__":
    part1_frequency_counting()
    part2_complement_technique()
    part3_prefix_sum_hashmap()
    part4_anagram_grouping()
