package ch05.tests;

import java.util.*;

/**
 * Tests for Chapter 5: Collections
 * =================================
 * Chapter 5: Collections
 *
 * This file tests every solve() method from Chapter 5 using the reference
 * solutions. We define each solve() here so the test is self-contained.
 *
 * Build and run:
 *   cd code/java
 *   javac ch05/tests/TestCh05.java
 *   java -ea ch05.tests.TestCh05
 *
 * The -ea flag enables assertions. Without it, assert statements are ignored!
 */
public class TestCh05 {

    // ── Helper methods ───────────────────────────────────────────────

    static void assertEquals(Object expected, Object actual, String msg) {
        assert Objects.equals(expected, actual)
            : msg + " — expected " + expected + ", got " + actual;
    }

    static void assertArrayEquals(int[] expected, int[] actual, String msg) {
        assert Arrays.equals(expected, actual)
            : msg + " — expected " + Arrays.toString(expected)
              + ", got " + Arrays.toString(actual);
    }

    // ── Reference solutions ─────────────────────────────────────────

    // W1: Second Largest
    static int solveSecondLargest(int[] nums) {
        if (nums.length < 2) return -1;
        int first = Integer.MIN_VALUE;
        int second = Integer.MIN_VALUE;
        for (int n : nums) {
            if (n > first) {
                second = first;
                first = n;
            } else if (n > second && n != first) {
                second = n;
            }
        }
        return (second == Integer.MIN_VALUE) ? -1 : second;
    }

    // W2: Reverse List
    static int[] solveReverseList(int[] nums) {
        int[] result = nums.clone();
        int left = 0, right = result.length - 1;
        while (left < right) {
            int temp = result[left];
            result[left] = result[right];
            result[right] = temp;
            left++;
            right--;
        }
        return result;
    }

    // W3: Count Vowels
    static int solveCountVowels(String s) {
        Set<Character> vowels = new HashSet<>(Arrays.asList('a', 'e', 'i', 'o', 'u'));
        int count = 0;
        for (char c : s.toLowerCase().toCharArray()) {
            if (vowels.contains(c)) count++;
        }
        return count;
    }

    // W4: Remove Duplicates
    static int[] solveRemoveDuplicates(int[] nums) {
        if (nums.length == 0) return nums;
        int unique = 1;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] != nums[i - 1]) unique++;
        }
        int[] result = new int[unique];
        result[0] = nums[0];
        int write = 1;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] != nums[i - 1]) {
                result[write++] = nums[i];
            }
        }
        return result;
    }

    // W5: Character Frequency
    static Map<Character, Integer> solveCharFrequency(String s) {
        Map<Character, Integer> freq = new HashMap<>();
        for (char c : s.toCharArray()) {
            freq.put(c, freq.getOrDefault(c, 0) + 1);
        }
        return freq;
    }

    // W6: Move Zeros
    static int[] solveMoveZeros(int[] nums) {
        int[] result = nums.clone();
        int write = 0;
        for (int i = 0; i < result.length; i++) {
            if (result[i] != 0) {
                result[write++] = result[i];
            }
        }
        while (write < result.length) {
            result[write++] = 0;
        }
        return result;
    }

    // P1: Union Arrays
    static int[] solveUnionArrays(int[] a, int[] b) {
        HashSet<Integer> set = new HashSet<>();
        for (int n : a) set.add(n);
        for (int n : b) set.add(n);
        int[] result = new int[set.size()];
        int i = 0;
        for (int n : set) result[i++] = n;
        Arrays.sort(result);
        return result;
    }

    // P2: Anagram Check
    static boolean solveAnagramCheck(String s1, String s2) {
        String a = s1.toLowerCase();
        String b = s2.toLowerCase();
        if (a.length() != b.length()) return false;
        Map<Character, Integer> freq = new HashMap<>();
        for (char c : a.toCharArray()) freq.put(c, freq.getOrDefault(c, 0) + 1);
        for (char c : b.toCharArray()) freq.put(c, freq.getOrDefault(c, 0) - 1);
        for (int count : freq.values()) {
            if (count != 0) return false;
        }
        return true;
    }

    // P3: Two Sum
    static int[] solveTwoSum(int[] nums, int target) {
        Map<Integer, Integer> seen = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (seen.containsKey(complement)) {
                return new int[]{seen.get(complement), i};
            }
            seen.put(nums[i], i);
        }
        return new int[]{-1, -1};
    }

    // P4: Sort by Frequency
    static int[] solveSortByFrequency(int[] nums) {
        Map<Integer, Integer> freq = new HashMap<>();
        for (int n : nums) freq.put(n, freq.getOrDefault(n, 0) + 1);
        Integer[] boxed = new Integer[nums.length];
        for (int i = 0; i < nums.length; i++) boxed[i] = nums[i];
        Arrays.sort(boxed, (a, b) -> {
            int diff = freq.get(b) - freq.get(a);
            if (diff != 0) return diff;
            return a - b;
        });
        int[] result = new int[nums.length];
        for (int i = 0; i < boxed.length; i++) result[i] = boxed[i];
        return result;
    }

    // P5: Longest Common Prefix
    static String solveLongestCommonPrefix(String[] strs) {
        if (strs.length == 0) return "";
        String first = strs[0];
        for (int i = 0; i < first.length(); i++) {
            char c = first.charAt(i);
            for (int j = 1; j < strs.length; j++) {
                if (i >= strs[j].length() || strs[j].charAt(i) != c) {
                    return first.substring(0, i);
                }
            }
        }
        return first;
    }

    // C1: Find Duplicates
    static int[] solveFindDuplicates(int[] nums) {
        HashSet<Integer> seen = new HashSet<>();
        TreeSet<Integer> dups = new TreeSet<>();
        for (int n : nums) {
            if (!seen.add(n)) dups.add(n);
        }
        return dups.stream().mapToInt(Integer::intValue).toArray();
    }

    // C2: Group Anagrams
    static List<List<String>> solveGroupAnagrams(String[] strs) {
        TreeMap<String, List<String>> groups = new TreeMap<>();
        for (String s : strs) {
            char[] chars = s.toCharArray();
            Arrays.sort(chars);
            String key = new String(chars);
            groups.computeIfAbsent(key, k -> new ArrayList<>()).add(s);
        }
        List<List<String>> result = new ArrayList<>();
        for (List<String> group : groups.values()) {
            Collections.sort(group);
            result.add(group);
        }
        result.sort((a, b) -> a.get(0).compareTo(b.get(0)));
        return result;
    }

    // C3: Rotate Array
    static void reverseRange(int[] nums, int start, int end) {
        while (start < end) {
            int temp = nums[start];
            nums[start] = nums[end];
            nums[end] = temp;
            start++;
            end--;
        }
    }

    static int[] solveRotateArray(int[] nums, int k) {
        int[] result = nums.clone();
        int n = result.length;
        if (n == 0) return result;
        k = k % n;
        if (k == 0) return result;
        reverseRange(result, 0, n - 1);
        reverseRange(result, 0, k - 1);
        reverseRange(result, k, n - 1);
        return result;
    }

    // ── Warmup 01: Second Largest ────────────────────────────────────

    static void testSecondLargestNormal() {
        assertEquals(4, solveSecondLargest(new int[]{3, 1, 4, 1, 5}),
            "Second largest of {3,1,4,1,5}");
        System.out.println("  test_second_largest_normal....... PASS");
    }

    static void testSecondLargestAllSame() {
        assertEquals(-1, solveSecondLargest(new int[]{7, 7, 7}),
            "All same elements");
        System.out.println("  test_second_largest_all_same..... PASS");
    }

    static void testSecondLargestTwoElements() {
        assertEquals(1, solveSecondLargest(new int[]{1, 2}),
            "Two elements");
        System.out.println("  test_second_largest_two_elem..... PASS");
    }

    static void testSecondLargestSingle() {
        assertEquals(-1, solveSecondLargest(new int[]{10}),
            "Single element");
        System.out.println("  test_second_largest_single....... PASS");
    }

    // ── Warmup 02: Reverse List ──────────────────────────────────────

    static void testReverseListNormal() {
        assertArrayEquals(new int[]{5, 4, 3, 2, 1},
            solveReverseList(new int[]{1, 2, 3, 4, 5}),
            "Reverse {1,2,3,4,5}");
        System.out.println("  test_reverse_list_normal......... PASS");
    }

    static void testReverseListSingle() {
        assertArrayEquals(new int[]{1},
            solveReverseList(new int[]{1}),
            "Reverse single element");
        System.out.println("  test_reverse_list_single......... PASS");
    }

    static void testReverseListEmpty() {
        assertArrayEquals(new int[]{},
            solveReverseList(new int[]{}),
            "Reverse empty array");
        System.out.println("  test_reverse_list_empty.......... PASS");
    }

    // ── Warmup 03: Count Vowels ──────────────────────────────────────

    static void testCountVowelsHello() {
        assertEquals(3, solveCountVowels("Hello World"),
            "Vowels in 'Hello World'");
        System.out.println("  test_count_vowels_hello.......... PASS");
    }

    static void testCountVowelsAllVowels() {
        assertEquals(5, solveCountVowels("aeiou"),
            "Vowels in 'aeiou'");
        System.out.println("  test_count_vowels_all............ PASS");
    }

    static void testCountVowelsNone() {
        assertEquals(0, solveCountVowels("xyz"),
            "Vowels in 'xyz'");
        System.out.println("  test_count_vowels_none........... PASS");
    }

    static void testCountVowelsEmpty() {
        assertEquals(0, solveCountVowels(""),
            "Vowels in empty string");
        System.out.println("  test_count_vowels_empty.......... PASS");
    }

    // ── Warmup 04: Remove Duplicates ─────────────────────────────────

    static void testRemoveDupsBasic() {
        assertArrayEquals(new int[]{1, 2},
            solveRemoveDuplicates(new int[]{1, 1, 2}),
            "Remove dups from {1,1,2}");
        System.out.println("  test_remove_dups_basic........... PASS");
    }

    static void testRemoveDupsMultiple() {
        assertArrayEquals(new int[]{1, 2, 3},
            solveRemoveDuplicates(new int[]{1, 1, 1, 2, 2, 3}),
            "Remove dups from {1,1,1,2,2,3}");
        System.out.println("  test_remove_dups_multiple........ PASS");
    }

    static void testRemoveDupsSingle() {
        assertArrayEquals(new int[]{1},
            solveRemoveDuplicates(new int[]{1}),
            "Remove dups from {1}");
        System.out.println("  test_remove_dups_single.......... PASS");
    }

    // ── Warmup 05: Character Frequency ───────────────────────────────

    static void testCharFreqBasic() {
        Map<Character, Integer> result = solveCharFrequency("aab");
        assertEquals(2, result.get('a'), "Freq of 'a' in 'aab'");
        assertEquals(1, result.get('b'), "Freq of 'b' in 'aab'");
        assertEquals(2, result.size(), "Unique chars in 'aab'");
        System.out.println("  test_char_freq_basic............. PASS");
    }

    static void testCharFreqEmpty() {
        Map<Character, Integer> result = solveCharFrequency("");
        assertEquals(0, result.size(), "Freq of empty string");
        System.out.println("  test_char_freq_empty............. PASS");
    }

    static void testCharFreqRepeated() {
        Map<Character, Integer> result = solveCharFrequency("aaa");
        assertEquals(3, result.get('a'), "Freq of 'a' in 'aaa'");
        assertEquals(1, result.size(), "Unique chars in 'aaa'");
        System.out.println("  test_char_freq_repeated.......... PASS");
    }

    // ── Warmup 06: Move Zeros ────────────────────────────────────────

    static void testMoveZerosNormal() {
        assertArrayEquals(new int[]{1, 3, 12, 0, 0},
            solveMoveZeros(new int[]{0, 1, 0, 3, 12}),
            "Move zeros in {0,1,0,3,12}");
        System.out.println("  test_move_zeros_normal........... PASS");
    }

    static void testMoveZerosLeading() {
        assertArrayEquals(new int[]{1, 0, 0},
            solveMoveZeros(new int[]{0, 0, 1}),
            "Move zeros in {0,0,1}");
        System.out.println("  test_move_zeros_leading.......... PASS");
    }

    static void testMoveZerosNoZeros() {
        assertArrayEquals(new int[]{1, 2, 3},
            solveMoveZeros(new int[]{1, 2, 3}),
            "No zeros to move");
        System.out.println("  test_move_zeros_no_zeros......... PASS");
    }

    // ── Practice 01: Union Arrays ────────────────────────────────────

    static void testUnionBasic() {
        assertArrayEquals(new int[]{1, 2, 3, 4, 5},
            solveUnionArrays(new int[]{1, 2, 3}, new int[]{3, 4, 5}),
            "Union of {1,2,3} and {3,4,5}");
        System.out.println("  test_union_basic................. PASS");
    }

    static void testUnionWithDups() {
        assertArrayEquals(new int[]{1, 2, 3},
            solveUnionArrays(new int[]{1, 1, 2}, new int[]{2, 3, 3}),
            "Union of {1,1,2} and {2,3,3}");
        System.out.println("  test_union_with_dups............. PASS");
    }

    // ── Practice 02: Anagram Check ───────────────────────────────────

    static void testAnagramTrue() {
        assertEquals(true, solveAnagramCheck("listen", "silent"),
            "listen/silent are anagrams");
        System.out.println("  test_anagram_true................ PASS");
    }

    static void testAnagramFalse() {
        assertEquals(false, solveAnagramCheck("hello", "world"),
            "hello/world are not anagrams");
        System.out.println("  test_anagram_false............... PASS");
    }

    static void testAnagramEmpty() {
        assertEquals(true, solveAnagramCheck("", ""),
            "Empty strings are anagrams");
        System.out.println("  test_anagram_empty............... PASS");
    }

    // ── Practice 03: Two Sum ─────────────────────────────────────────

    static void testTwoSumBasic() {
        assertArrayEquals(new int[]{0, 1},
            solveTwoSum(new int[]{2, 7, 11, 15}, 9),
            "Two sum {2,7,11,15} target 9");
        System.out.println("  test_two_sum_basic............... PASS");
    }

    static void testTwoSumDuplicates() {
        assertArrayEquals(new int[]{0, 1},
            solveTwoSum(new int[]{3, 3}, 6),
            "Two sum {3,3} target 6");
        System.out.println("  test_two_sum_duplicates.......... PASS");
    }

    static void testTwoSumNoSolution() {
        assertArrayEquals(new int[]{-1, -1},
            solveTwoSum(new int[]{1, 2, 3}, 10),
            "Two sum no solution");
        System.out.println("  test_two_sum_no_solution......... PASS");
    }

    // ── Practice 04: Sort by Frequency ───────────────────────────────

    static void testSortFreqBasic() {
        assertArrayEquals(new int[]{2, 2, 3, 3, 1},
            solveSortByFrequency(new int[]{2, 3, 1, 3, 2}),
            "Sort by freq {2,3,1,3,2}");
        System.out.println("  test_sort_freq_basic............. PASS");
    }

    static void testSortFreqSingle() {
        assertArrayEquals(new int[]{1},
            solveSortByFrequency(new int[]{1}),
            "Sort by freq {1}");
        System.out.println("  test_sort_freq_single............ PASS");
    }

    // ── Practice 05: Longest Common Prefix ───────────────────────────

    static void testLCPBasic() {
        assertEquals("fl",
            solveLongestCommonPrefix(new String[]{"flower", "flow", "flight"}),
            "LCP of flower/flow/flight");
        System.out.println("  test_lcp_basic................... PASS");
    }

    static void testLCPNone() {
        assertEquals("",
            solveLongestCommonPrefix(new String[]{"dog", "racecar", "car"}),
            "LCP of dog/racecar/car");
        System.out.println("  test_lcp_none.................... PASS");
    }

    // ── Challenge 01: Find Duplicates ────────────────────────────────

    static void testFindDupsBasic() {
        assertArrayEquals(new int[]{2, 3},
            solveFindDuplicates(new int[]{4, 3, 2, 7, 8, 2, 3, 1}),
            "Duplicates in {4,3,2,7,8,2,3,1}");
        System.out.println("  test_find_dups_basic............. PASS");
    }

    static void testFindDupsNone() {
        assertArrayEquals(new int[]{},
            solveFindDuplicates(new int[]{1, 2, 3}),
            "No duplicates in {1,2,3}");
        System.out.println("  test_find_dups_none.............. PASS");
    }

    static void testFindDupsAllSame() {
        assertArrayEquals(new int[]{1},
            solveFindDuplicates(new int[]{1, 1, 1, 1}),
            "Duplicates in {1,1,1,1}");
        System.out.println("  test_find_dups_all_same.......... PASS");
    }

    // ── Challenge 02: Group Anagrams ─────────────────────────────────

    static void testGroupAnagramsBasic() {
        List<List<String>> result = solveGroupAnagrams(
            new String[]{"eat", "tea", "tan", "ate", "nat", "bat"});

        List<List<String>> expected = new ArrayList<>();
        expected.add(Arrays.asList("ate", "eat", "tea"));
        expected.add(Arrays.asList("bat"));
        expected.add(Arrays.asList("nat", "tan"));

        assertEquals(expected.size(), result.size(), "Number of anagram groups");
        for (int i = 0; i < expected.size(); i++) {
            assertEquals(expected.get(i), result.get(i),
                "Anagram group " + i);
        }
        System.out.println("  test_group_anagrams_basic........ PASS");
    }

    // ── Challenge 03: Rotate Array ───────────────────────────────────

    static void testRotateBasic() {
        assertArrayEquals(new int[]{5, 6, 7, 1, 2, 3, 4},
            solveRotateArray(new int[]{1, 2, 3, 4, 5, 6, 7}, 3),
            "Rotate {1..7} by 3");
        System.out.println("  test_rotate_basic................ PASS");
    }

    static void testRotateOverLength() {
        assertArrayEquals(new int[]{2, 1},
            solveRotateArray(new int[]{1, 2}, 3),
            "Rotate {1,2} by 3");
        System.out.println("  test_rotate_over_length.......... PASS");
    }

    // ── Runner ───────────────────────────────────────────────────────

    public static void main(String[] args) {

        System.out.println("Testing Chapter 5...\n");

        System.out.println("--- Warmup Problems ---");

        System.out.println("=== Warmup 01: Second Largest ===");
        testSecondLargestNormal();
        testSecondLargestAllSame();
        testSecondLargestTwoElements();
        testSecondLargestSingle();
        System.out.println();

        System.out.println("=== Warmup 02: Reverse List ===");
        testReverseListNormal();
        testReverseListSingle();
        testReverseListEmpty();
        System.out.println();

        System.out.println("=== Warmup 03: Count Vowels ===");
        testCountVowelsHello();
        testCountVowelsAllVowels();
        testCountVowelsNone();
        testCountVowelsEmpty();
        System.out.println();

        System.out.println("=== Warmup 04: Remove Duplicates ===");
        testRemoveDupsBasic();
        testRemoveDupsMultiple();
        testRemoveDupsSingle();
        System.out.println();

        System.out.println("=== Warmup 05: Character Frequency ===");
        testCharFreqBasic();
        testCharFreqEmpty();
        testCharFreqRepeated();
        System.out.println();

        System.out.println("=== Warmup 06: Move Zeros ===");
        testMoveZerosNormal();
        testMoveZerosLeading();
        testMoveZerosNoZeros();
        System.out.println();

        System.out.println("--- Practice Problems ---");

        System.out.println("=== Practice 01: Union Arrays ===");
        testUnionBasic();
        testUnionWithDups();
        System.out.println();

        System.out.println("=== Practice 02: Anagram Check ===");
        testAnagramTrue();
        testAnagramFalse();
        testAnagramEmpty();
        System.out.println();

        System.out.println("=== Practice 03: Two Sum ===");
        testTwoSumBasic();
        testTwoSumDuplicates();
        testTwoSumNoSolution();
        System.out.println();

        System.out.println("=== Practice 04: Sort by Frequency ===");
        testSortFreqBasic();
        testSortFreqSingle();
        System.out.println();

        System.out.println("=== Practice 05: Longest Common Prefix ===");
        testLCPBasic();
        testLCPNone();
        System.out.println();

        System.out.println("--- Challenge Problems ---");

        System.out.println("=== Challenge 01: Find Duplicates ===");
        testFindDupsBasic();
        testFindDupsNone();
        testFindDupsAllSame();
        System.out.println();

        System.out.println("=== Challenge 02: Group Anagrams ===");
        testGroupAnagramsBasic();
        System.out.println();

        System.out.println("=== Challenge 03: Rotate Array ===");
        testRotateBasic();
        testRotateOverLength();
        System.out.println();

        System.out.println("All tests passed!");
    }
}
