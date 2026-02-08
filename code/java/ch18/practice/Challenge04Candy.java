package ch18.practice;

import java.util.*;

/**
 * Challenge 4: Candy Distribution
 * Chapter 18: Greedy Algorithms — The Smart Shortcut
 *
 * PROBLEM: Min candies so each child gets >=1 and higher-rated neighbors get more.
 *
 * EXAMPLES:
 *   solve([1,0,2]) -> 5
 *   solve([1,2,2]) -> 4
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Challenge04Candy {
    public static int solve(int[] ratings) {
        // TODO: Replace this with your solution
        return 0;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] ratings = Arrays.stream(sc.nextLine().trim().split(" ")).mapToInt(Integer::parseInt).toArray();
        System.out.println(solve(ratings));
        sc.close();
    }
}
