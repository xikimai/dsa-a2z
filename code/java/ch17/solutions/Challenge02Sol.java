package ch17.solutions;

import java.util.*;

/**
 * Solution for Challenge 2: Task Scheduler
 * Chapter 17: Heaps & Priority Queues — The VIP Line
 *
 * APPROACH: Max-heap of frequencies. Each round pick up to (n+1) tasks.
 * TIME:  O(total_tasks)
 * SPACE: O(1) auxiliary
 */
public class Challenge02Sol {
    public static int solve(char[] tasks, int n) {
        int[] freq = new int[26];
        for (char t : tasks) freq[t - 'A']++;

        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        for (int f : freq) {
            if (f > 0) maxHeap.add(f);
        }

        int time = 0;
        while (!maxHeap.isEmpty()) {
            int cycle = n + 1;
            List<Integer> temp = new ArrayList<>();
            int tasksDone = 0;
            for (int i = 0; i < cycle; i++) {
                if (!maxHeap.isEmpty()) {
                    int cnt = maxHeap.poll();
                    if (cnt > 1) temp.add(cnt - 1);
                    tasksDone++;
                }
            }
            for (int t : temp) maxHeap.add(t);
            time += maxHeap.isEmpty() ? tasksDone : cycle;
        }
        return time;
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
