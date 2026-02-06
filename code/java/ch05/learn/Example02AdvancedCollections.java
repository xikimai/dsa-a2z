package ch05.learn;

import java.util.*;

/**
 * Example 02: Advanced Collections
 * =================================
 * Chapter 5: Collections
 *
 * This file covers HashSet, HashMap, pairs (using int[]), and sorting
 * with Comparators. These are essential tools for competitive programming.
 * Read through each section and run the file to see the output.
 *
 * Build and run:
 *   cd code/java
 *   javac ch05/learn/Example02AdvancedCollections.java
 *   java ch05.learn.Example02AdvancedCollections
 */
public class Example02AdvancedCollections {

    // ── 1. HashSet Operations ──────────────────────────────────────────
    // A Set stores unique values. No duplicates, no guaranteed order.
    // Great for "have I seen this before?" checks in O(1).

    static void demoHashSet() {
        HashSet<Integer> seen = new HashSet<>();

        // Adding elements
        seen.add(10);
        seen.add(20);
        seen.add(30);
        seen.add(20);  // duplicate — ignored!
        System.out.println("Set: " + seen);
        System.out.println("Size: " + seen.size());  // 3, not 4

        // Checking membership — O(1) average
        System.out.println("Contains 20? " + seen.contains(20));
        System.out.println("Contains 99? " + seen.contains(99));

        // Removing
        seen.remove(10);
        System.out.println("After remove 10: " + seen);

        // Use case: find unique elements in an array
        int[] nums = {1, 3, 2, 3, 1, 4, 2, 5};
        HashSet<Integer> unique = new HashSet<>();
        for (int n : nums) {
            unique.add(n);
        }
        System.out.println("Unique from array: " + unique);

        // Convert to sorted list
        ArrayList<Integer> sorted = new ArrayList<>(unique);
        Collections.sort(sorted);
        System.out.println("Sorted unique: " + sorted);
    }

    // ── 2. HashMap and Frequency Counting ──────────────────────────────
    // A Map stores key-value pairs. Think of it like a dictionary.
    // Keys must be unique; values can repeat.

    static void demoHashMap() {
        // Basic operations
        HashMap<String, Integer> ages = new HashMap<>();
        ages.put("Alice", 14);
        ages.put("Bob", 15);
        ages.put("Charlie", 14);
        System.out.println("Map: " + ages);
        System.out.println("Alice's age: " + ages.get("Alice"));
        System.out.println("Contains 'Bob'? " + ages.containsKey("Bob"));

        // getOrDefault — avoids null when key doesn't exist
        System.out.println("Dave's age: " + ages.getOrDefault("Dave", -1));

        // Iterating a map
        System.out.print("Entries: ");
        for (Map.Entry<String, Integer> entry : ages.entrySet()) {
            System.out.print(entry.getKey() + "=" + entry.getValue() + " ");
        }
        System.out.println();

        // ── Frequency counting (super common pattern!) ──
        String word = "mississippi";
        HashMap<Character, Integer> freq = new HashMap<>();
        for (char c : word.toCharArray()) {
            freq.put(c, freq.getOrDefault(c, 0) + 1);
        }
        System.out.println("Frequencies of '" + word + "': " + freq);

        // Find the most frequent character
        char maxChar = ' ';
        int maxCount = 0;
        for (Map.Entry<Character, Integer> entry : freq.entrySet()) {
            if (entry.getValue() > maxCount) {
                maxCount = entry.getValue();
                maxChar = entry.getKey();
            }
        }
        System.out.println("Most frequent: '" + maxChar + "' (" + maxCount + " times)");
    }

    // ── 3. Pairs Using int[] ───────────────────────────────────────────
    // Java doesn't have a built-in Pair class (unlike Python tuples).
    // For competitive programming, int[] of size 2 is the simplest approach.

    static void demoPairs() {
        // A "pair" as int[2]
        int[] pair = {3, 7};
        System.out.println("Pair: (" + pair[0] + ", " + pair[1] + ")");

        // List of pairs
        ArrayList<int[]> pairs = new ArrayList<>();
        pairs.add(new int[]{1, 5});
        pairs.add(new int[]{3, 2});
        pairs.add(new int[]{2, 8});

        System.out.print("Pairs: ");
        for (int[] p : pairs) {
            System.out.print("(" + p[0] + "," + p[1] + ") ");
        }
        System.out.println();

        // Sort pairs by first element, then by second
        pairs.sort((a, b) -> {
            if (a[0] != b[0]) return a[0] - b[0];
            return a[1] - b[1];
        });

        System.out.print("Sorted: ");
        for (int[] p : pairs) {
            System.out.print("(" + p[0] + "," + p[1] + ") ");
        }
        System.out.println();
    }

    // ── 4. Sorting with Comparators ────────────────────────────────────
    // Arrays.sort() and Collections.sort() use natural order by default.
    // You can pass a custom Comparator to sort however you want.

    static void demoSorting() {
        // Sorting an array
        int[] nums = {5, 2, 8, 1, 9, 3};
        Arrays.sort(nums);
        System.out.println("Sorted array: " + Arrays.toString(nums));

        // Sorting a list of strings (alphabetical by default)
        ArrayList<String> names = new ArrayList<>(
            Arrays.asList("Charlie", "Alice", "Bob", "Dave"));
        Collections.sort(names);
        System.out.println("Sorted names: " + names);

        // Custom sort: by string length
        names.sort((a, b) -> a.length() - b.length());
        System.out.println("By length: " + names);

        // Custom sort: reverse alphabetical
        names.sort((a, b) -> b.compareTo(a));
        System.out.println("Reverse alpha: " + names);

        // Sorting Integer array in reverse (can't use int[] with Comparator)
        Integer[] boxed = {5, 2, 8, 1, 9, 3};
        Arrays.sort(boxed, (a, b) -> b - a);
        System.out.println("Reverse sorted: " + Arrays.toString(boxed));

        // Sorting a subarray
        int[] partial = {5, 2, 8, 1, 9, 3};
        Arrays.sort(partial, 1, 4);  // sort indices 1..3 only
        System.out.println("Partial sort [1,4): " + Arrays.toString(partial));
    }

    // ── Main ───────────────────────────────────────────────────────────

    public static void main(String[] args) {

        System.out.println("=== 1. HashSet Operations ===");
        demoHashSet();
        System.out.println();

        System.out.println("=== 2. HashMap and Frequency Counting ===");
        demoHashMap();
        System.out.println();

        System.out.println("=== 3. Pairs Using int[] ===");
        demoPairs();
        System.out.println();

        System.out.println("=== 4. Sorting with Comparators ===");
        demoSorting();
    }
}
