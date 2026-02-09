package ch26.solutions;

/**
 * Solution: Binary Tree Cameras — Chapter 26: Trees — Branches of Logic
 */
public class Challenge04Sol {
    public static class TreeNode {
        int val;
        TreeNode left, right;
        TreeNode(int v) { val = v; }
    }

    public static TreeNode buildTree(Integer[] values) {
        if (values == null || values.length == 0 || values[0] == null) return null;
        TreeNode root = new TreeNode(values[0]);
        java.util.Queue<TreeNode> queue = new java.util.LinkedList<>();
        queue.add(root);
        int i = 1;
        while (!queue.isEmpty() && i < values.length) {
            TreeNode node = queue.poll();
            if (i < values.length && values[i] != null) {
                node.left = new TreeNode(values[i]);
                queue.add(node.left);
            }
            i++;
            if (i < values.length && values[i] != null) {
                node.right = new TreeNode(values[i]);
                queue.add(node.right);
            }
            i++;
        }
        return root;
    }

    static int cameras;
    static final int NOT_COVERED = 0, HAS_CAMERA = 1, COVERED = 2;
    public static int solve(TreeNode root) {
        cameras = 0;
        if (dfs(root) == NOT_COVERED) cameras++;
        return cameras;
    }
    private static int dfs(TreeNode node) {
        if (node == null) return COVERED;
        int left = dfs(node.left);
        int right = dfs(node.right);
        if (left == NOT_COVERED || right == NOT_COVERED) { cameras++; return HAS_CAMERA; }
        if (left == HAS_CAMERA || right == HAS_CAMERA) return COVERED;
        return NOT_COVERED;
    }
}
