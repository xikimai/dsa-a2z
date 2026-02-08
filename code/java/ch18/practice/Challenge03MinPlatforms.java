package ch18.practice;

import java.util.*;

/**
 * Challenge 3: Minimum Platforms
 * Chapter 18: Greedy Algorithms — The Smart Shortcut
 *
 * PROBLEM: Min platforms so no train waits.
 *
 * EXAMPLES:
 *   solve([900,940,950,1100,1500,1800], [910,1200,1120,1130,1900,2000]) -> 3
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Challenge03MinPlatforms {
    public static int solve(int[] arrivals, int[] departures) {
        // TODO: Replace this with your solution
        return 0;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] arr = Arrays.stream(sc.nextLine().trim().split(" ")).mapToInt(Integer::parseInt).toArray();
        int[] dep = Arrays.stream(sc.nextLine().trim().split(" ")).mapToInt(Integer::parseInt).toArray();
        System.out.println(solve(arr, dep));
        sc.close();
    }
}
