package ch34.solutions;

public class Warmup01Sol {
    // Cross Product and Orientation
    public static int[] solve(int[][][] queries) {
        int[] result = new int[queries.length];
        for (int q = 0; q < queries.length; q++) {
            int[] a = queries[q][0], b = queries[q][1], c = queries[q][2];
            long cp = (long)(b[0] - a[0]) * (c[1] - a[1])
                    - (long)(b[1] - a[1]) * (c[0] - a[0]);
            if (cp > 0) result[q] = 1;
            else if (cp < 0) result[q] = -1;
            else result[q] = 0;
        }
        return result;
    }
}
