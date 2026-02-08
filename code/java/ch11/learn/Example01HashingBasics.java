package ch11.learn;

import java.util.*;

/**
 * Example 01: Hashing Basics
 * ==========================
 * Chapter 11: Hashing — The Secret Decoder Ring
 *
 * This example demonstrates the fundamental building blocks of hashing in Java:
 *   Part 1 — HashSet basics (add, contains, size, timing vs ArrayList)
 *   Part 2 — HashMap basics (put, get, getOrDefault, iteration, frequency counting)
 *   Part 3 — Collision demo (hash values mod small table size)
 *   Part 4 — Performance comparison (HashSet vs ArrayList vs binary search)
 */
public class Example01HashingBasics {

    public static void main(String[] args) {

        // ── Part 1: HashSet Demo ────────────────────────────────
        System.out.println("═══ Part 1: HashSet Basics ═══");

        HashSet<Integer> seen = new HashSet<>();
        seen.add(10);
        seen.add(20);
        seen.add(30);
        seen.add(20); // duplicate — ignored

        System.out.println("Set: " + seen);           // {20, 10, 30} (order not guaranteed)
        System.out.println("Contains 20? " + seen.contains(20));  // true
        System.out.println("Contains 99? " + seen.contains(99));  // false
        System.out.println("Size: " + seen.size());                // 3

        // Timing: HashSet.contains vs ArrayList.contains
        int n = 100_000;
        HashSet<Integer> bigSet = new HashSet<>();
        ArrayList<Integer> bigList = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            bigSet.add(i);
            bigList.add(i);
        }

        long start = System.nanoTime();
        for (int i = 0; i < 1000; i++) {
            bigSet.contains(n - 1);  // worst-case element
        }
        long setTime = System.nanoTime() - start;

        start = System.nanoTime();
        for (int i = 0; i < 1000; i++) {
            bigList.contains(n - 1); // worst-case element — scans entire list
        }
        long listTime = System.nanoTime() - start;

        System.out.printf("HashSet  1000 lookups: %,d ns%n", setTime);
        System.out.printf("ArrayList 1000 lookups: %,d ns%n", listTime);
        System.out.printf("ArrayList is ~%.0fx slower%n%n", (double) listTime / setTime);

        // ── Part 2: HashMap Demo ────────────────────────────────
        System.out.println("═══ Part 2: HashMap Basics ═══");

        HashMap<String, Integer> ages = new HashMap<>();
        ages.put("Alice", 14);
        ages.put("Bob", 15);
        ages.put("Charlie", 14);

        System.out.println("Alice's age: " + ages.get("Alice"));           // 14
        System.out.println("Unknown:     " + ages.get("Zara"));            // null
        System.out.println("With default: " + ages.getOrDefault("Zara", -1)); // -1

        // Iterating over entries
        System.out.println("\nAll entries:");
        for (Map.Entry<String, Integer> entry : ages.entrySet()) {
            System.out.println("  " + entry.getKey() + " -> " + entry.getValue());
        }

        // Frequency counting — the bread and butter of hashing
        System.out.println("\nFrequency counting demo:");
        String word = "mississippi";
        HashMap<Character, Integer> freq = new HashMap<>();
        for (char c : word.toCharArray()) {
            freq.put(c, freq.getOrDefault(c, 0) + 1);
        }
        System.out.println("  \"" + word + "\" -> " + freq);
        // {m=1, i=4, s=4, p=2}

        // ── Part 3: Collision Demo ──────────────────────────────
        System.out.println("\n═══ Part 3: Collision Demo ═══");
        System.out.println("Imagine a hash table with only 7 buckets.");
        System.out.println("hash(key) = key % 7\n");

        int tableSize = 7;
        int[] keys = {10, 20, 15, 7, 3, 17, 24};
        HashMap<Integer, List<Integer>> buckets = new HashMap<>();

        for (int key : keys) {
            int bucket = key % tableSize;
            buckets.computeIfAbsent(bucket, k -> new ArrayList<>()).add(key);
            System.out.printf("  key=%2d  ->  bucket %d%n", key, bucket);
        }

        System.out.println("\nBucket contents:");
        for (int i = 0; i < tableSize; i++) {
            List<Integer> contents = buckets.getOrDefault(i, Collections.emptyList());
            System.out.printf("  Bucket %d: %s%s%n", i, contents,
                    contents.size() > 1 ? "  <-- COLLISION!" : "");
        }

        // ── Part 4: Performance Comparison ──────────────────────
        System.out.println("\n═══ Part 4: Performance Comparison ═══");
        System.out.println("Looking up 10,000 elements in a collection of " + n + " items:\n");

        // Sorted array for binary search
        int[] sortedArr = new int[n];
        for (int i = 0; i < n; i++) sortedArr[i] = i;

        int lookups = 10_000;
        Random rng = new Random(42);
        int[] targets = new int[lookups];
        for (int i = 0; i < lookups; i++) targets[i] = rng.nextInt(n);

        // HashSet
        start = System.nanoTime();
        for (int t : targets) bigSet.contains(t);
        long hsTime = System.nanoTime() - start;

        // ArrayList (linear scan)
        start = System.nanoTime();
        for (int t : targets) bigList.contains(t);
        long alTime = System.nanoTime() - start;

        // Binary search on sorted array
        start = System.nanoTime();
        for (int t : targets) Arrays.binarySearch(sortedArr, t);
        long bsTime = System.nanoTime() - start;

        System.out.printf("  HashSet        : %,10d ns  (O(1) average)%n", hsTime);
        System.out.printf("  Binary Search  : %,10d ns  (O(log n))%n", bsTime);
        System.out.printf("  ArrayList scan : %,10d ns  (O(n))%n", alTime);

        System.out.println("\nKey takeaway: HashSet gives O(1) lookup — the fastest option");
        System.out.println("for the question 'Is X in this collection?'");
    }
}
