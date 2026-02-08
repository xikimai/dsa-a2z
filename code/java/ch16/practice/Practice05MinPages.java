package ch16.practice;

import java.util.*;

/**
 * Practice 5: Minimum Pages Allocation
 * Chapter 16: Binary Search Beyond Arrays — Searching on Answers
 *
 * PROBLEM: Allocate n books to k students contiguously.
 *          Return minimum possible maximum pages any student reads.
 *          Return -1 if more students than books.
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Practice05MinPages {
    public static int solve(int[] pages, int students) {
        // TODO: Replace this with your solution
        return 0;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine().trim();
        int[] pages = Arrays.stream(line.split(" ")).mapToInt(Integer::parseInt).toArray();
        int students = sc.nextInt();
        System.out.println(solve(pages, students));
        sc.close();
    }
}
