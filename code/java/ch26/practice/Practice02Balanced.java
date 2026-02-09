package ch26.practice;

import java.util.*;

/**
 * Practice 2: Balanced Binary Tree — Chapter 26: Trees — Branches of Logic
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Practice02Balanced {
    static class TreeNode {
        int val;
        TreeNode left, right;
        TreeNode(int v) { val = v; }
    }

    static TreeNode buildTree(Integer[] values) {
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

    public static boolean solve(TreeNode root) {
        // TODO: Replace this with your solution
        return false;
    }

    public static void main(String[] args) { Scanner sc = new Scanner(System.in); sc.close(); }
}
