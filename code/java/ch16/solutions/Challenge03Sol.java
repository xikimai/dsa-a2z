package ch16.solutions;

public class Challenge03Sol {
    public static double solve(int[] nums1, int[] nums2) {
        // Ensure nums1 is the shorter array
        if (nums1.length > nums2.length) return solve(nums2, nums1);

        int m = nums1.length, n = nums2.length;
        int half = (m + n + 1) / 2;

        int lo = 0, hi = m;
        while (lo <= hi) {
            int i = lo + (hi - lo) / 2;
            int j = half - i;

            int left1 = (i > 0) ? nums1[i - 1] : Integer.MIN_VALUE;
            int left2 = (j > 0) ? nums2[j - 1] : Integer.MIN_VALUE;
            int right1 = (i < m) ? nums1[i] : Integer.MAX_VALUE;
            int right2 = (j < n) ? nums2[j] : Integer.MAX_VALUE;

            if (left1 <= right2 && left2 <= right1) {
                if ((m + n) % 2 == 1) return Math.max(left1, left2);
                else return (Math.max(left1, left2) + Math.min(right1, right2)) / 2.0;
            } else if (left1 > right2) {
                hi = i - 1;
            } else {
                lo = i + 1;
            }
        }
        return 0.0;
    }
}
