package ch16.solutions;

public class Warmup02Sol {
    public static int[] solve(int[] arr, int target) {
        if (arr.length == 0) return new int[]{-1, -1};
        int first = -1, last = -1;

        // Find first
        int lo = 0, hi = arr.length - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (arr[mid] == target) { first = mid; hi = mid - 1; }
            else if (arr[mid] < target) lo = mid + 1;
            else hi = mid - 1;
        }
        if (first == -1) return new int[]{-1, -1};

        // Find last
        lo = first; hi = arr.length - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (arr[mid] == target) { last = mid; lo = mid + 1; }
            else if (arr[mid] < target) lo = mid + 1;
            else hi = mid - 1;
        }
        return new int[]{first, last};
    }
}
