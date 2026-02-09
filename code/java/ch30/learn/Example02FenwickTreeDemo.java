package ch30.learn;

/**
 * Example 02: Fenwick Tree (BIT) Demo
 * Chapter 30: Segment Trees & Range Queries
 *
 * Demonstrates BIT for prefix sum queries with point updates.
 */
public class Example02FenwickTreeDemo {
    static int[] bit;
    static int n;

    static void update(int i, int delta) {
        for (; i <= n; i += i & (-i)) bit[i] += delta;
    }

    static int prefixSum(int i) {
        int sum = 0;
        for (; i > 0; i -= i & (-i)) sum += bit[i];
        return sum;
    }

    static int rangeSum(int l, int r) {
        return prefixSum(r) - prefixSum(l - 1);
    }

    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        n = arr.length;
        bit = new int[n + 1];
        for (int i = 0; i < n; i++) update(i + 1, arr[i]);

        System.out.println("Fenwick Tree Demo");
        System.out.println("Array: [1, 2, 3, 4, 5]");
        System.out.println("Prefix(3) = " + prefixSum(3)); // 6
        System.out.println("Range(2,4) = " + rangeSum(2, 4)); // 9
        update(3, 5); // add 5 to index 3
        System.out.println("After adding 5 to index 3:");
        System.out.println("Prefix(3) = " + prefixSum(3)); // 11
    }
}
