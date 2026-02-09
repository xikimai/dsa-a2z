package ch34.learn;

/**
 * Example 01: Geometry Basics — Cross Product, Distance, Orientation
 * ==================================================================
 * Chapter 34: Computational Geometry & Sweep Line
 *
 * Demonstrates fundamental 2D geometry operations.
 */
public class Example01GeometryBasics {

    static long cross(int[] o, int[] a, int[] b) {
        return (long)(a[0] - o[0]) * (b[1] - o[1])
             - (long)(a[1] - o[1]) * (b[0] - o[0]);
    }

    static long dot(int[] o, int[] a, int[] b) {
        return (long)(a[0] - o[0]) * (b[0] - o[0])
             + (long)(a[1] - o[1]) * (b[1] - o[1]);
    }

    static double distance(int[] a, int[] b) {
        return Math.sqrt((double)(a[0]-b[0])*(a[0]-b[0])
                       + (double)(a[1]-b[1])*(a[1]-b[1]));
    }

    static int orientation(int[] a, int[] b, int[] c) {
        long cp = cross(a, b, c);
        if (cp > 0) return 1;   // counter-clockwise
        if (cp < 0) return -1;  // clockwise
        return 0;               // collinear
    }

    public static void main(String[] args) {
        System.out.println("=".repeat(60));
        System.out.println("GEOMETRY BASICS: Cross Product, Distance, Orientation");
        System.out.println("=".repeat(60));

        // Cross product demo
        int[] o = {0, 0}, a = {4, 4};
        System.out.println("\n--- Cross Product ---");
        System.out.println("  cross(O, A, (1,2)) = " + cross(o, a, new int[]{1, 2}));   // 4
        System.out.println("  cross(O, A, (1,0)) = " + cross(o, a, new int[]{1, 0}));   // -4
        System.out.println("  cross(O, A, (2,2)) = " + cross(o, a, new int[]{2, 2}));   // 0

        // Orientation demo
        System.out.println("\n--- Orientation ---");
        String[] labels = {"Collinear", "Counter-Clockwise", "Clockwise"};
        int r1 = orientation(new int[]{0,0}, new int[]{4,4}, new int[]{1,2});
        int r2 = orientation(new int[]{0,0}, new int[]{4,4}, new int[]{1,0});
        System.out.println("  (0,0)-(4,4)-(1,2): " + (r1 > 0 ? "CCW" : r1 < 0 ? "CW" : "Collinear"));
        System.out.println("  (0,0)-(4,4)-(1,0): " + (r2 > 0 ? "CCW" : r2 < 0 ? "CW" : "Collinear"));

        // Distance demo
        System.out.println("\n--- Distance ---");
        System.out.println("  distance((0,0), (3,4)) = " + distance(new int[]{0,0}, new int[]{3,4}));
    }
}
