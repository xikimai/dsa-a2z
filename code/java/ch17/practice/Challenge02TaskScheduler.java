package ch17.practice;

import java.util.*;

/**
 * Challenge 2: Task Scheduler
 * Chapter 17: Heaps & Priority Queues — The VIP Line
 *
 * PROBLEM: Find min intervals to complete all tasks with cooldown n.
 * EXAMPLES:
 *   solve(['A','A','A','B','B','B'], 2) -> 8
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Challenge02TaskScheduler {
    public static int solve(char[] tasks, int n) {
        // TODO: Replace this with your solution
        return 0;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] parts = sc.nextLine().trim().split(" ");
        char[] tasks = new char[parts.length];
        for (int i = 0; i < parts.length; i++) tasks[i] = parts[i].charAt(0);
        int n = Integer.parseInt(sc.nextLine().trim());
        System.out.println(solve(tasks, n));
        sc.close();
    }
}
