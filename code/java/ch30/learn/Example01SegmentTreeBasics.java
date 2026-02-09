package ch30.learn;

/**
 * Example 01: Segment Tree Basics — Build, Query, Update
 * Chapter 30: Segment Trees & Range Queries
 *
 * Demonstrates segment tree for range sum with point update.
 */
public class Example01SegmentTreeBasics {
    static int[] tree;

    static void build(int[] arr, int node, int start, int end) {
        if (start == end) { tree[node] = arr[start]; return; }
        int mid = (start + end) / 2;
        build(arr, 2 * node, start, mid);
        build(arr, 2 * node + 1, mid + 1, end);
        tree[node] = tree[2 * node] + tree[2 * node + 1];
    }

    static int query(int node, int start, int end, int l, int r) {
        if (r < start || end < l) return 0;
        if (l <= start && end <= r) return tree[node];
        int mid = (start + end) / 2;
        return query(2 * node, start, mid, l, r)
             + query(2 * node + 1, mid + 1, end, l, r);
    }

    static void update(int node, int start, int end, int idx, int val) {
        if (start == end) { tree[node] = val; return; }
        int mid = (start + end) / 2;
        if (idx <= mid) update(2 * node, start, mid, idx, val);
        else update(2 * node + 1, mid + 1, end, idx, val);
        tree[node] = tree[2 * node] + tree[2 * node + 1];
    }

    public static void main(String[] args) {
        int[] arr = {1, 3, 5, 7, 9, 11};
        int n = arr.length;
        tree = new int[4 * n];
        build(arr, 1, 0, n - 1);

        System.out.println("Segment Tree Basics Demo");
        System.out.println("Array: [1, 3, 5, 7, 9, 11]");
        System.out.println("Sum(1,3) = " + query(1, 0, n - 1, 1, 3)); // 15
        update(1, 0, n - 1, 1, 10);
        System.out.println("After update arr[1]=10:");
        System.out.println("Sum(1,3) = " + query(1, 0, n - 1, 1, 3)); // 22
    }
}
