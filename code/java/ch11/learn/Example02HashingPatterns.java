package ch11.learn;

import java.util.*;

/**
 * Example 02: Hashing Patterns
 * ============================
 * Chapter 11: Hashing — The Secret Decoder Ring
 *
 * Four core patterns you'll see again and again:
 *   Part 1 — Frequency counting
 *   Part 2 — Complement technique (Two Sum trace)
 *   Part 3 — Prefix sum + hash map (subarray sum trace)
 *   Part 4 — Anagram grouping
 */
public class Example02HashingPatterns {

    public static void main(String[] args) {

        // ── Part 1: Frequency Counting Pattern ──────────────────
        System.out.println("═══ Part 1: Frequency Counting ═══");
        System.out.println("Goal: Count how many times each element appears.\n");

        int[] votes = {3, 1, 3, 2, 3, 2, 1, 3};
        HashMap<Integer, Integer> freq = new HashMap<>();
        for (int v : votes) {
            freq.put(v, freq.getOrDefault(v, 0) + 1);
        }
        System.out.println("Votes: " + Arrays.toString(votes));
        System.out.println("Tally: " + freq);

        // Find the winner (most votes)
        int winner = -1, maxVotes = 0;
        for (Map.Entry<Integer, Integer> e : freq.entrySet()) {
            if (e.getValue() > maxVotes) {
                maxVotes = e.getValue();
                winner = e.getKey();
            }
        }
        System.out.println("Winner: candidate " + winner + " with " + maxVotes + " votes\n");

        // ── Part 2: Complement Technique (Two Sum) ──────────────
        System.out.println("═══ Part 2: Complement Technique (Two Sum) ═══");
        System.out.println("Goal: Find two numbers that add up to target.\n");

        int[] nums = {2, 7, 11, 15};
        int target = 9;

        System.out.println("Array:  " + Arrays.toString(nums));
        System.out.println("Target: " + target);
        System.out.println();

        HashMap<Integer, Integer> seen = new HashMap<>(); // value -> index
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            System.out.printf("  i=%d, nums[i]=%d, need complement=%d, seen=%s%n",
                    i, nums[i], complement, seen);

            if (seen.containsKey(complement)) {
                System.out.printf("  --> Found it! indices [%d, %d]%n%n",
                        seen.get(complement), i);
                break;
            }
            seen.put(nums[i], i);
        }

        // ── Part 3: Prefix Sum + Hash Map ───────────────────────
        System.out.println("═══ Part 3: Prefix Sum + Hash Map ═══");
        System.out.println("Goal: Count subarrays whose elements sum to k.\n");

        int[] arr = {1, 2, 3, -2, 5};
        int k = 3;

        System.out.println("Array: " + Arrays.toString(arr));
        System.out.println("k = " + k);
        System.out.println();

        HashMap<Integer, Integer> prefixCount = new HashMap<>();
        prefixCount.put(0, 1); // empty prefix has sum 0
        int prefixSum = 0;
        int count = 0;

        for (int i = 0; i < arr.length; i++) {
            prefixSum += arr[i];
            int need = prefixSum - k;

            System.out.printf("  i=%d, arr[i]=%2d, prefixSum=%2d, need=%2d, prefixCount=%s",
                    i, arr[i], prefixSum, need, prefixCount);

            if (prefixCount.containsKey(need)) {
                int found = prefixCount.get(need);
                count += found;
                System.out.printf("  --> +%d subarray(s)!%n", found);
            } else {
                System.out.println();
            }

            prefixCount.put(prefixSum, prefixCount.getOrDefault(prefixSum, 0) + 1);
        }

        System.out.println("\nTotal subarrays with sum " + k + ": " + count);

        // Verify by brute force
        int bruteCount = 0;
        System.out.println("\nBrute-force verification:");
        for (int i = 0; i < arr.length; i++) {
            int sum = 0;
            for (int j = i; j < arr.length; j++) {
                sum += arr[j];
                if (sum == k) {
                    System.out.printf("  subarray [%d..%d] = %d%n", i, j, sum);
                    bruteCount++;
                }
            }
        }
        System.out.println("Brute-force count: " + bruteCount + "\n");

        // ── Part 4: Anagram Grouping ────────────────────────────
        System.out.println("═══ Part 4: Anagram Grouping ═══");
        System.out.println("Goal: Group words that are anagrams of each other.\n");

        String[] words = {"eat", "tea", "tan", "ate", "nat", "bat"};
        System.out.println("Words: " + Arrays.toString(words));
        System.out.println();

        HashMap<String, List<String>> groups = new HashMap<>();
        for (String w : words) {
            // The key insight: anagrams have the same sorted characters
            char[] ca = w.toCharArray();
            Arrays.sort(ca);
            String key = new String(ca);

            System.out.printf("  \"%s\"  ->  sorted key \"%s\"%n", w, key);

            groups.computeIfAbsent(key, x -> new ArrayList<>()).add(w);
        }

        System.out.println("\nGroups:");
        for (Map.Entry<String, List<String>> entry : groups.entrySet()) {
            System.out.println("  key=\"" + entry.getKey() + "\"  ->  " + entry.getValue());
        }

        System.out.println("\nPattern summary:");
        System.out.println("  1. Frequency counting  — getOrDefault(key, 0) + 1");
        System.out.println("  2. Complement technique — store seen values, check complement");
        System.out.println("  3. Prefix sum + map     — count prefixes that differ by k");
        System.out.println("  4. Anagram grouping     — canonical key from sorted chars");
    }
}
