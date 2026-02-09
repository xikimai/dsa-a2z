package ch26.solutions;

/**
 * Solution: Boundary Traversal — Chapter 26: Trees — Branches of Logic
 */
public class Challenge03Sol {
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

    public static java.util.List<Integer> solve(TreeNode root) {
        java.util.List<Integer> result = new java.util.ArrayList<>();
        if (root == null) return result;
        if (!isLeaf(root)) result.add(root.val);
        addLeftBoundary(root, result);
        addLeaves(root, result);
        addRightBoundary(root, result);
        return result;
    }
    private static boolean isLeaf(TreeNode node) {
        return node != null && node.left == null && node.right == null;
    }
    private static void addLeftBoundary(TreeNode root, java.util.List<Integer> result) {
        TreeNode node = root.left;
        while (node != null) {
            if (!isLeaf(node)) result.add(node.val);
            node = node.left != null ? node.left : node.right;
        }
    }
    private static void addLeaves(TreeNode node, java.util.List<Integer> result) {
        if (node == null) return;
        if (isLeaf(node)) { result.add(node.val); return; }
        addLeaves(node.left, result);
        addLeaves(node.right, result);
    }
    private static void addRightBoundary(TreeNode root, java.util.List<Integer> result) {
        java.util.List<Integer> temp = new java.util.ArrayList<>();
        TreeNode node = root.right;
        while (node != null) {
            if (!isLeaf(node)) temp.add(node.val);
            node = node.right != null ? node.right : node.left;
        }
        for (int i = temp.size() - 1; i >= 0; i--) result.add(temp.get(i));
    }
}
