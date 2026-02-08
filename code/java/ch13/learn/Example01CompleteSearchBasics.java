package ch13.learn;

import java.util.*;

/**
 * Example 01: Complete Search Basics
 * ====================================
 * Chapter 13: Bronze Battle Plan — Complete Search & Simulation
 *
 * Demonstrates:
 *   Part 1 — Subset generation (recursive)
 *   Part 2 — Bitmask subset generation
 *   Part 3 — Permutation generation (backtracking)
 *   Part 4 — Simulation (robot on grid)
 */
public class Example01CompleteSearchBasics {

    // ── Part 1: Recursive Subsets ──
    static void generateSubsets(int[] nums, int index, List<Integer> current, List<List<Integer>> result) {
        if (index == nums.length) {
            result.add(new ArrayList<>(current));
            return;
        }
        generateSubsets(nums, index + 1, current, result);
        current.add(nums[index]);
        generateSubsets(nums, index + 1, current, result);
        current.remove(current.size() - 1);
    }

    // ── Part 2: Bitmask Subsets ──
    static List<List<Integer>> bitmaskSubsets(int[] nums) {
        int n = nums.length;
        List<List<Integer>> result = new ArrayList<>();
        for (int mask = 0; mask < (1 << n); mask++) {
            List<Integer> subset = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                if ((mask & (1 << i)) != 0) subset.add(nums[i]);
            }
            result.add(subset);
        }
        return result;
    }

    // ── Part 3: Permutations ──
    static void generatePermutations(int[] nums, boolean[] used, List<Integer> current, List<List<Integer>> result) {
        if (current.size() == nums.length) {
            result.add(new ArrayList<>(current));
            return;
        }
        for (int i = 0; i < nums.length; i++) {
            if (used[i]) continue;
            used[i] = true;
            current.add(nums[i]);
            generatePermutations(nums, used, current, result);
            current.remove(current.size() - 1);
            used[i] = false;
        }
    }

    // ── Part 4: Robot Simulation ──
    static int[] simulateRobot(String commands) {
        int x = 0, y = 0;
        for (char cmd : commands.toCharArray()) {
            if (cmd == 'U') y++;
            else if (cmd == 'D') y--;
            else if (cmd == 'L') x--;
            else if (cmd == 'R') x++;
        }
        return new int[]{x, y};
    }

    public static void main(String[] args) {
        // Part 1
        System.out.println("=== Part 1: Recursive Subsets ===");
        int[] nums = {1, 2, 3};
        List<List<Integer>> subsets = new ArrayList<>();
        generateSubsets(nums, 0, new ArrayList<>(), subsets);
        System.out.println("Subsets of [1,2,3]: " + subsets);

        // Part 2
        System.out.println("\n=== Part 2: Bitmask Subsets ===");
        List<List<Integer>> bmSubsets = bitmaskSubsets(nums);
        for (int mask = 0; mask < bmSubsets.size(); mask++) {
            System.out.printf("  mask=%d binary=%s subset=%s%n",
                mask, Integer.toBinaryString(mask), bmSubsets.get(mask));
        }

        // Part 3
        System.out.println("\n=== Part 3: Permutations ===");
        List<List<Integer>> perms = new ArrayList<>();
        generatePermutations(nums, new boolean[nums.length], new ArrayList<>(), perms);
        System.out.println("Permutations of [1,2,3]: " + perms.size() + " total");
        for (List<Integer> p : perms) System.out.println("  " + p);

        // Part 4
        System.out.println("\n=== Part 4: Robot Simulation ===");
        String cmds = "UURRDLL";
        int[] pos = simulateRobot(cmds);
        System.out.println("Commands: " + cmds + " -> Final position: (" + pos[0] + ", " + pos[1] + ")");
    }
}
