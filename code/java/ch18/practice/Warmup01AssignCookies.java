package ch18.practice;

import java.util.*;

/**
 * Warmup 1: Assign Cookies
 * Chapter 18: Greedy Algorithms — The Smart Shortcut
 *
 * PROBLEM: Maximize content children. A child is content if cookie >= greed.
 *
 * EXAMPLES:
 *   solve([1,2,3], [1,1])       -> 1
 *   solve([1,2], [1,2,3])       -> 2
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Warmup01AssignCookies {
    public static int solve(int[] greed, int[] cookies) {
        // TODO: Replace this with your solution
        return 0;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] greed = Arrays.stream(sc.nextLine().trim().split(" ")).mapToInt(Integer::parseInt).toArray();
        int[] cookies = Arrays.stream(sc.nextLine().trim().split(" ")).mapToInt(Integer::parseInt).toArray();
        System.out.println(solve(greed, cookies));
        sc.close();
    }
}
