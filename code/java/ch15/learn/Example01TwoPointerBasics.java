package ch15.learn;

/**
 * Example 01: Two-Pointer Basics
 * ===============================
 * Chapter 15: Two Pointers & Sliding Window — The Caterpillar Method
 *
 * Demonstrates converging two pointers and same-direction pointers.
 */
public class Example01TwoPointerBasics {

    public static void main(String[] args) {
        // Part 1: Converging two pointers — pair sum
        System.out.println("=== Part 1: Converging Two Pointers ===");
        int[] arr = {1, 3, 5, 8, 12, 15, 20};
        int target = 13;
        System.out.println("Array: [1,3,5,8,12,15,20], Target: " + target);

        int left = 0, right = arr.length - 1;
        while (left < right) {
            int sum = arr[left] + arr[right];
            System.out.printf("  arr[%d]=%d + arr[%d]=%d = %d", left, arr[left], right, arr[right], sum);
            if (sum == target) {
                System.out.println("  == " + target + " FOUND!");
                break;
            } else if (sum < target) {
                System.out.println("  < " + target + " -> move left right");
                left++;
            } else {
                System.out.println("  > " + target + " -> move right left");
                right--;
            }
        }

        // Part 2: Same-direction pointers — move zeros
        System.out.println("\n=== Part 2: Same-Direction Pointers ===");
        int[] zeros = {0, 1, 0, 3, 12, 0, 5};
        System.out.print("Input: ");
        for (int x : zeros) System.out.print(x + " ");
        System.out.println();

        int slow = 0;
        for (int fast = 0; fast < zeros.length; fast++) {
            if (zeros[fast] != 0) {
                int temp = zeros[slow];
                zeros[slow] = zeros[fast];
                zeros[fast] = temp;
                slow++;
            }
        }

        System.out.print("Result: ");
        for (int x : zeros) System.out.print(x + " ");
        System.out.println("\nAll zeros moved to the end!");
    }
}
