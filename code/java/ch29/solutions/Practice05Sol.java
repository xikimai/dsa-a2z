package ch29.solutions;

public class Practice05Sol {
    // Satisfiability of Equality Equations
    static int[] parent, rank;

    static int find(int x) {
        if (parent[x] != x) parent[x] = find(parent[x]);
        return parent[x];
    }

    static void union(int x, int y) {
        int rx = find(x), ry = find(y);
        if (rx == ry) return;
        if (rank[rx] < rank[ry]) parent[rx] = ry;
        else if (rank[rx] > rank[ry]) parent[ry] = rx;
        else { parent[ry] = rx; rank[rx]++; }
    }

    public static boolean solve(String[] equations) {
        parent = new int[26];
        rank = new int[26];
        for (int i = 0; i < 26; i++) parent[i] = i;

        // First pass: union all "==" pairs
        for (String eq : equations)
            if (eq.charAt(1) == '=')
                union(eq.charAt(0) - 'a', eq.charAt(3) - 'a');

        // Second pass: check all "!=" pairs
        for (String eq : equations)
            if (eq.charAt(1) == '!')
                if (find(eq.charAt(0) - 'a') == find(eq.charAt(3) - 'a'))
                    return false;

        return true;
    }
}
