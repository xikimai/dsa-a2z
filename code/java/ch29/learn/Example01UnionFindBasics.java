package ch29.learn;

/**
 * Example 01: Union-Find Basics — Step-by-Step DSU
 * ==================================================
 * Chapter 29: Union-Find & Minimum Spanning Trees
 *
 * Demonstrates Union-Find with path compression and union by rank.
 */
public class Example01UnionFindBasics {

    static int[] parent, rank;

    static void init(int n) {
        parent = new int[n];
        rank = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;
    }

    static int find(int x) {
        if (parent[x] != x) parent[x] = find(parent[x]); // path compression
        return parent[x];
    }

    static boolean union(int x, int y) {
        int rx = find(x), ry = find(y);
        if (rx == ry) return false;
        if (rank[rx] < rank[ry]) parent[rx] = ry;
        else if (rank[rx] > rank[ry]) parent[ry] = rx;
        else { parent[ry] = rx; rank[rx]++; }
        return true;
    }

    public static void main(String[] args) {
        System.out.println("Union-Find Basics");

        // 5 nodes, connect some
        init(5);
        union(0, 1);
        union(1, 2);
        union(3, 4);

        System.out.printf("  find(0)=%d, find(2)=%d, same? %b%n",
            find(0), find(2), find(0) == find(2)); // true
        System.out.printf("  find(0)=%d, find(3)=%d, same? %b%n",
            find(0), find(3), find(0) == find(3)); // false

        // Count components
        int components = 5;
        init(5);
        int[][] edges = {{0,1},{1,2},{3,4}};
        for (int[] e : edges)
            if (union(e[0], e[1])) components--;
        System.out.printf("  Components after edges: %d%n", components); // 2
    }
}
