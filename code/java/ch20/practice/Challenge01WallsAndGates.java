package ch20.practice;

import java.util.*;

/**
 * Challenge 1: Walls and Gates
 * Chapter 20: Graphs II — Real Problems
 *
 * PROBLEM: Fill empty rooms (INF) with distance to nearest gate (0). Walls are -1.
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Challenge01WallsAndGates {
    public static int[][] solve(int[][] rooms) {
        // TODO: Replace this with your solution
        return rooms;
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int rows = scan.nextInt(), cols = scan.nextInt();
        int[][] rooms = new int[rows][cols];
        for (int i = 0; i < rows; i++)
            for (int j = 0; j < cols; j++)
                rooms[i][j] = scan.nextInt();
        solve(rooms);
        for (int[] row : rooms)
            System.out.println(Arrays.toString(row));
        scan.close();
    }
}
