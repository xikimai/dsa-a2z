package ch23.solutions;

public class Challenge04Sol {
    public static int solve(int[] tree) {
        if (tree.length == 0) return 0;
        int[] result = dfs(tree, 0);
        return Math.max(result[0], result[1]);
    }

    // returns {rob_this, skip_this}
    private static int[] dfs(int[] tree, int idx) {
        if (idx >= tree.length || tree[idx] == -1) return new int[]{0, 0};
        int[] left = dfs(tree, 2 * idx + 1);
        int[] right = dfs(tree, 2 * idx + 2);
        int rob = tree[idx] + left[1] + right[1];
        int skip = Math.max(left[0], left[1]) + Math.max(right[0], right[1]);
        return new int[]{rob, skip};
    }
}
