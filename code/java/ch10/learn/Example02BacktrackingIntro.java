package ch10.learn;

import java.util.*;

/**
 * Example 02: Backtracking — Explore, Choose, Undo
 * ==============================
 * Chapter 10: The Magic of Recursion
 *
 * Backtracking is a systematic way to explore all possibilities.
 * Think of it as walking through a maze: try a path, and if it
 * leads to a dead end, go back and try another.
 *
 * Build and run:
 *   cd code/java
 *   javac ch10/learn/Example02BacktrackingIntro.java
 *   java ch10.learn.Example02BacktrackingIntro
 */
public class Example02BacktrackingIntro {

    // ── 1. Generate Subsets of {1,2,3} with Trace ───────────────────

    static void subsetsHelper(int[] nums, int idx, List<Integer> current,
                              List<List<Integer>> result, int depth) {
        String indent = "  ".repeat(depth + 1);
        if (idx == nums.length) {
            System.out.println(indent + "-> subset found: " + current);
            result.add(new ArrayList<>(current));
            return;
        }
        // Exclude nums[idx]
        System.out.println(indent + "skip " + nums[idx]);
        subsetsHelper(nums, idx + 1, current, result, depth + 1);

        // Include nums[idx]
        System.out.println(indent + "take " + nums[idx]);
        current.add(nums[idx]);
        subsetsHelper(nums, idx + 1, current, result, depth + 1);
        current.remove(current.size() - 1);  // backtrack!
    }

    static void demoSubsets() {
        System.out.println("=== Part 1: Generate All Subsets of {1, 2, 3} ===");
        System.out.println("At each element, we choose: SKIP it or TAKE it.\n");

        int[] nums = {1, 2, 3};
        List<List<Integer>> result = new ArrayList<>();
        subsetsHelper(nums, 0, new ArrayList<>(), result, 0);

        System.out.println("\n  All " + result.size() + " subsets: " + result);
        System.out.println("  For n elements, there are 2^n subsets (here 2^3 = 8).\n");
    }

    // ── 2. Generate Permutations of {1,2,3} ─────────────────────────

    static void permuteHelper(int[] nums, boolean[] used, List<Integer> current,
                              List<List<Integer>> result) {
        if (current.size() == nums.length) {
            result.add(new ArrayList<>(current));
            return;
        }
        for (int i = 0; i < nums.length; i++) {
            if (used[i]) continue;
            used[i] = true;
            current.add(nums[i]);
            permuteHelper(nums, used, current, result);
            current.remove(current.size() - 1);  // backtrack!
            used[i] = false;                      // backtrack!
        }
    }

    static void demoPermutations() {
        System.out.println("=== Part 2: Generate All Permutations of {1, 2, 3} ===");
        System.out.println("At each position, try every unused element.\n");

        int[] nums = {1, 2, 3};
        List<List<Integer>> result = new ArrayList<>();
        permuteHelper(nums, new boolean[nums.length], new ArrayList<>(), result);

        for (List<Integer> perm : result) {
            System.out.println("  " + perm);
        }
        System.out.println("\n  All " + result.size() + " permutations (3! = 6).\n");
    }

    // ── 3. N-Queens 4x4 Demo ────────────────────────────────────────

    static boolean isSafe(int[] queens, int row, int col) {
        for (int r = 0; r < row; r++) {
            int c = queens[r];
            if (c == col) return false;                    // same column
            if (Math.abs(r - row) == Math.abs(c - col)) return false;  // diagonal
        }
        return true;
    }

    static void nQueensHelper(int n, int row, int[] queens, List<int[]> solutions) {
        if (row == n) {
            solutions.add(queens.clone());
            return;
        }
        for (int col = 0; col < n; col++) {
            if (isSafe(queens, row, col)) {
                queens[row] = col;
                nQueensHelper(n, row + 1, queens, solutions);
                queens[row] = -1;  // backtrack!
            }
        }
    }

    static void printBoard(int[] queens, int n) {
        for (int r = 0; r < n; r++) {
            StringBuilder sb = new StringBuilder("    ");
            for (int c = 0; c < n; c++) {
                sb.append(queens[r] == c ? "Q " : ". ");
            }
            System.out.println(sb);
        }
    }

    static void demoNQueens() {
        System.out.println("=== Part 3: N-Queens (4x4) ===");
        System.out.println("Place 4 queens on a 4x4 board so no two attack each other.\n");

        int n = 4;
        List<int[]> solutions = new ArrayList<>();
        nQueensHelper(n, 0, new int[n], solutions);

        System.out.println("  Found " + solutions.size() + " solutions:\n");
        int count = 0;
        for (int[] sol : solutions) {
            count++;
            System.out.println("  Solution " + count + ":");
            printBoard(sol, n);
            System.out.println();
        }
    }

    // ── 4. Backtracking Template Summary ────────────────────────────

    static void demoTemplate() {
        System.out.println("=== Part 4: The Backtracking Template ===\n");
        System.out.println("  Every backtracking problem follows this pattern:\n");
        System.out.println("    void backtrack(state, choices) {");
        System.out.println("        if (isGoal(state)) {");
        System.out.println("            recordSolution(state);");
        System.out.println("            return;");
        System.out.println("        }");
        System.out.println("        for (choice in choices) {");
        System.out.println("            if (isValid(choice)) {");
        System.out.println("                makeChoice(state, choice);   // DO");
        System.out.println("                backtrack(state, choices);   // EXPLORE");
        System.out.println("                undoChoice(state, choice);   // UNDO");
        System.out.println("            }");
        System.out.println("        }");
        System.out.println("    }\n");
        System.out.println("  The 3 steps: DO -> EXPLORE -> UNDO");
        System.out.println("  This is the heart of backtracking!\n");
    }

    // ── Main ────────────────────────────────────────────────────────

    public static void main(String[] args) {
        System.out.println("Chapter 10: Backtracking Introduction");
        System.out.println("======================================\n");

        demoSubsets();
        demoPermutations();
        demoNQueens();
        demoTemplate();

        System.out.println("KEY TAKEAWAYS:");
        System.out.println("  1. Subsets: at each element, choose SKIP or TAKE (2^n total)");
        System.out.println("  2. Permutations: at each slot, try every unused element (n! total)");
        System.out.println("  3. N-Queens: place one queen per row, check safety before placing");
        System.out.println("  4. Backtracking = DO, EXPLORE, UNDO — remember to undo your choice!");
    }
}
