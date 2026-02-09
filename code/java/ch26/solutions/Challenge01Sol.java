package ch26.solutions;

/**
 * Solution: Construct from Preorder+Inorder — Chapter 26: Trees — Branches of Logic
 */
public class Challenge01Sol {
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

    public static java.util.List<Integer> solve(int[] preorder, int[] inorder) {
        if (preorder.length == 0) return new java.util.ArrayList<>();
        java.util.Map<Integer,Integer> inMap = new java.util.HashMap<>();
        for (int i = 0; i < inorder.length; i++) inMap.put(inorder[i], i);
        TreeNode root = build(preorder, 0, preorder.length - 1, 0, inorder.length - 1, inMap);
        return treeToList(root);
    }
    private static TreeNode build(int[] pre, int ps, int pe, int is2, int ie, java.util.Map<Integer,Integer> inMap) {
        if (ps > pe) return null;
        TreeNode root = new TreeNode(pre[ps]);
        int inIdx = inMap.get(pre[ps]);
        int leftSize = inIdx - is2;
        root.left = build(pre, ps + 1, ps + leftSize, is2, inIdx - 1, inMap);
        root.right = build(pre, ps + leftSize + 1, pe, inIdx + 1, ie, inMap);
        return root;
    }
    private static java.util.List<Integer> treeToList(TreeNode root) {
        java.util.List<Integer> result = new java.util.ArrayList<>();
        if (root == null) return result;
        java.util.Queue<TreeNode> q = new java.util.LinkedList<>();
        q.add(root);
        while (!q.isEmpty()) {
            TreeNode node = q.poll();
            if (node != null) {
                result.add(node.val);
                q.add(node.left);
                q.add(node.right);
            } else {
                result.add(null);
            }
        }
        while (!result.isEmpty() && result.get(result.size()-1) == null) result.remove(result.size()-1);
        return result;
    }
}
