package ch19.solutions;

import java.util.*;

public class Practice04Sol {
    public static List<List<Integer>> solve(List<List<Integer>> adj) {
        List<List<Integer>> clone = new ArrayList<>();
        for (List<Integer> neighbors : adj) {
            clone.add(new ArrayList<>(neighbors));
        }
        return clone;
    }
}
