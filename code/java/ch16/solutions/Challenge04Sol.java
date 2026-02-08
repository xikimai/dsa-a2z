package ch16.solutions;

public class Challenge04Sol {
    public static int solve(int[] nums1, int[] nums2, int k) {
        int m = nums1.length, n = nums2.length;
        // Ensure nums1 is the shorter array
        if (m > n) return solve(nums2, nums1, k);

        int lo = Math.max(0, k - n);
        int hi = Math.min(k, m);

        while (lo <= hi) {
            int i = lo + (hi - lo) / 2;
            int j = k - i;

            int left1 = (i > 0) ? nums1[i - 1] : Integer.MIN_VALUE;
            int left2 = (j > 0) ? nums2[j - 1] : Integer.MIN_VALUE;
            int right1 = (i < m) ? nums1[i] : Integer.MAX_VALUE;
            int right2 = (j < n) ? nums2[j] : Integer.MAX_VALUE;

            if (left1 <= right2 && left2 <= right1) {
                return Math.max(left1, left2);
            } else if (left1 > right2) {
                hi = i - 1;
            } else {
                lo = i + 1;
            }
        }
        return -1;
    }
}
