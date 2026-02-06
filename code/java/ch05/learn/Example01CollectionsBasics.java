package ch05.learn;

import java.util.*;

/**
 * Example 01: Collections Basics
 * ==============================
 * Chapter 5: Collections
 *
 * This file shows you how Java handles collections: ArrayList, arrays,
 * and String operations. These are the building blocks you'll use in
 * almost every program you write.
 * Read through each section and run the file to see the output.
 *
 * Build and run:
 *   cd code/java
 *   javac ch05/learn/Example01CollectionsBasics.java
 *   java ch05.learn.Example01CollectionsBasics
 */
public class Example01CollectionsBasics {

    // ── 1. Creating ArrayLists and Arrays ──────────────────────────────
    // Arrays have a fixed size; ArrayLists can grow and shrink.
    // Arrays use [], ArrayLists use .get() and .set().

    static void demoCreating() {
        // Array: fixed size, declared with type[]
        int[] scores = {90, 85, 77, 92, 88};
        System.out.println("Array: " + Arrays.toString(scores));
        System.out.println("Array length: " + scores.length);

        // You can also create an empty array of a specific size
        int[] zeros = new int[5];  // all zeros by default
        System.out.println("Empty int array: " + Arrays.toString(zeros));

        // ArrayList: dynamic size, uses generics <Type>
        ArrayList<Integer> grades = new ArrayList<>();
        grades.add(90);
        grades.add(85);
        grades.add(77);
        System.out.println("ArrayList: " + grades);
        System.out.println("ArrayList size: " + grades.size());

        // Quick way to create an ArrayList with initial values
        ArrayList<String> fruits = new ArrayList<>(Arrays.asList("apple", "banana", "cherry"));
        System.out.println("Fruits: " + fruits);
    }

    // ── 2. Accessing and Modifying ─────────────────────────────────────
    // Arrays use [index], ArrayLists use .get(index) and .set(index, value).

    static void demoAccessing() {
        int[] nums = {10, 20, 30, 40, 50};

        // Reading elements
        System.out.println("First: " + nums[0]);
        System.out.println("Last:  " + nums[nums.length - 1]);

        // Modifying elements
        nums[2] = 99;
        System.out.println("After change: " + Arrays.toString(nums));

        // ArrayList version
        ArrayList<String> colors = new ArrayList<>(Arrays.asList("red", "green", "blue"));
        System.out.println("Second color: " + colors.get(1));

        colors.set(1, "yellow");         // replace
        System.out.println("After set: " + colors);

        colors.add("purple");            // append
        System.out.println("After add: " + colors);

        colors.add(1, "orange");         // insert at index
        System.out.println("After insert: " + colors);

        colors.remove(0);                // remove by index
        System.out.println("After remove: " + colors);

        // Checking membership
        System.out.println("Contains 'blue'? " + colors.contains("blue"));
        System.out.println("Index of 'blue': " + colors.indexOf("blue"));
    }

    // ── 3. String Operations ───────────────────────────────────────────
    // Strings in Java are immutable — every operation creates a new string.

    static void demoStrings() {
        String s = "Hello, World!";

        // Basic info
        System.out.println("Length: " + s.length());
        System.out.println("Char at 0: " + s.charAt(0));
        System.out.println("Substring(0,5): " + s.substring(0, 5));

        // Searching
        System.out.println("Contains 'World': " + s.contains("World"));
        System.out.println("Starts with 'Hello': " + s.startsWith("Hello"));
        System.out.println("Index of 'o': " + s.indexOf('o'));

        // Transforming (returns NEW strings — original is unchanged)
        System.out.println("Upper: " + s.toUpperCase());
        System.out.println("Lower: " + s.toLowerCase());
        System.out.println("Replace: " + s.replace("World", "Java"));
        System.out.println("Trim: " + "  spaces  ".trim());

        // Splitting and joining
        String csv = "one,two,three,four";
        String[] parts = csv.split(",");
        System.out.println("Split: " + Arrays.toString(parts));
        String joined = String.join(" - ", parts);
        System.out.println("Joined: " + joined);

        // Converting between char[] and String
        char[] chars = s.toCharArray();
        System.out.println("Char array: " + Arrays.toString(chars));
        String back = new String(chars);
        System.out.println("Back to string: " + back);
    }

    // ── 4. Iterating Collections ───────────────────────────────────────
    // Multiple ways to loop through arrays and lists.

    static void demoIterating() {
        int[] nums = {10, 20, 30, 40, 50};

        // 1. Classic for loop (use when you need the index)
        System.out.print("For loop:     ");
        for (int i = 0; i < nums.length; i++) {
            System.out.print(nums[i] + " ");
        }
        System.out.println();

        // 2. Enhanced for loop / "for-each" (cleaner when you don't need index)
        System.out.print("For-each:     ");
        for (int n : nums) {
            System.out.print(n + " ");
        }
        System.out.println();

        // 3. ArrayList iteration (same two styles work)
        ArrayList<String> words = new ArrayList<>(Arrays.asList("alpha", "beta", "gamma"));
        System.out.print("List for-each: ");
        for (String w : words) {
            System.out.print(w + " ");
        }
        System.out.println();

        // 4. Iterating with index on ArrayList
        System.out.print("List indexed:  ");
        for (int i = 0; i < words.size(); i++) {
            System.out.print(i + ":" + words.get(i) + " ");
        }
        System.out.println();
    }

    // ── Main ───────────────────────────────────────────────────────────

    public static void main(String[] args) {

        System.out.println("=== 1. Creating ArrayLists and Arrays ===");
        demoCreating();
        System.out.println();

        System.out.println("=== 2. Accessing and Modifying ===");
        demoAccessing();
        System.out.println();

        System.out.println("=== 3. String Operations ===");
        demoStrings();
        System.out.println();

        System.out.println("=== 4. Iterating Collections ===");
        demoIterating();
    }
}
