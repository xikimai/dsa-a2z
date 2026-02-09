package ch26.learn;

import java.util.*;

/**
 * Example 02: BST Operations — Search, Insert, Delete, Validate
 * Chapter 26: Trees — Branches of Logic
 */
public class Example02BstOperations {

    static class TreeNode {
        int val;
        TreeNode left, right;
        TreeNode(int v) { val = v; }
    }

    static TreeNode buildTree(Integer[] values) {
        if (values == null || values.length == 0 || values[0] == null) return null;
        TreeNode root = new TreeNode(values[0]);
        Queue<TreeNode> queue = new LinkedList<>();
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

    static TreeNode bstSearch(TreeNode root, int target) {
        if (root == null || root.val == target) return root;
        return target < root.val ? bstSearch(root.left, target) : bstSearch(root.right, target);
    }

    static TreeNode bstInsert(TreeNode root, int val) {
        if (root == null) return new TreeNode(val);
        if (val < root.val) root.left = bstInsert(root.left, val);
        else if (val > root.val) root.right = bstInsert(root.right, val);
        return root;
    }

    static boolean isValidBST(TreeNode root, long lo, long hi) {
        if (root == null) return true;
        if (root.val <= lo || root.val >= hi) return false;
        return isValidBST(root.left, lo, root.val) && isValidBST(root.right, root.val, hi);
    }

    static List<Integer> inorder(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        inorderHelper(root, res);
        return res;
    }
    static void inorderHelper(TreeNode node, List<Integer> res) {
        if (node == null) return;
        inorderHelper(node.left, res);
        res.add(node.val);
        inorderHelper(node.right, res);
    }

    public static void main(String[] args) {
        TreeNode bst = buildTree(new Integer[]{4, 2, 6, 1, 3, 5, 7});
        System.out.println("BST inorder: " + inorder(bst));
        System.out.println("Search 5: " + (bstSearch(bst, 5) != null ? "Found" : "Not found"));
        System.out.println("Valid BST: " + isValidBST(bst, Long.MIN_VALUE, Long.MAX_VALUE));
    }
}
