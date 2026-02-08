package ch12.solutions;

import java.util.*;

/**
 * Solution for Challenge 2: Two Numbers Appearing Odd Times
 * TIME: O(n)   SPACE: O(1)
 */
public class Challenge02Sol {
    public static int[] solve(int[] nums) {
        int xorAll = 0;
        for (int x : nums) xorAll ^= x;
        int diffBit = xorAll & (-xorAll);
        int a = 0, b = 0;
        for (int x : nums) {
            if ((x & diffBit) != 0) a ^= x;
            else b ^= x;
        }
        if (a > b) { int t = a; a = b; b = t; }
        return new int[]{a, b};
    }
}
