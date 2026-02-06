package ch04.learn;

import java.util.Arrays;
import java.util.Comparator;

/**
 * Example 02: Advanced Functions
 * ==============================
 * Chapter 4: Functions
 *
 * This file explores pass-by-value vs reference semantics, scope and
 * shadowing, method overloading for area calculations, and lambda
 * expressions (Java's version of anonymous functions).
 * Read through each section and run the file to see the output.
 *
 * Build and run:
 *   cd code/java
 *   javac ch04/learn/Example02AdvancedFunctions.java
 *   java ch04.learn.Example02AdvancedFunctions
 */
public class Example02AdvancedFunctions {

    // ── 1. Pass by Value: Primitives ─────────────────────────────────
    // Java ALWAYS passes by value. For primitives (int, double, etc.),
    // the method gets a COPY. Changing it inside doesn't affect outside.

    /** Tries to double x — but it won't change the caller's variable! */
    static void tryToDoubleIt(int x) {
        x = x * 2;
        System.out.println("  Inside method: x = " + x);
    }

    // ── 2. Pass by Value: References (Arrays/Objects) ────────────────
    // For arrays and objects, Java passes a COPY of the reference.
    // Both the caller and the method point to the SAME array in memory.
    // So modifying the array's CONTENTS changes it for everyone.

    /** Doubles every element in the array. This DOES change the original! */
    static void doubleArray(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            arr[i] = arr[i] * 2;
        }
    }

    /** Tries to reassign the array reference. This does NOT affect the caller. */
    static void tryToReassign(int[] arr) {
        arr = new int[]{99, 99, 99};  // only changes the local reference
        System.out.println("  Inside method: arr = " + Arrays.toString(arr));
    }

    // ── 3. Scope and Shadowing ───────────────────────────────────────
    // A "scope" is the region of code where a variable exists.
    // "Shadowing" happens when a local variable has the same name as
    // a field — the local one "shadows" (hides) the outer one.

    static int count = 100;  // class-level variable (field)

    static void showScope() {
        int count = 5;  // shadows the class-level 'count'
        System.out.println("  Local count: " + count);           // 5
        System.out.println("  Class count: " + Example02AdvancedFunctions.count);  // 100
    }

    // ── 4. Method Overloading for Area ───────────────────────────────
    // Same method name, different parameters — Java picks the right one.

    /** Area of a circle: pi * r^2 */
    static double area(double radius) {
        return Math.PI * radius * radius;
    }

    /** Area of a rectangle: width * height */
    static double area(double width, double height) {
        return width * height;
    }

    /** Area of a triangle: 0.5 * base * height */
    static double area(double base, double height, boolean isTriangle) {
        return 0.5 * base * height;
    }

    // ── 5. Lambda Expressions ────────────────────────────────────────
    // Lambdas let you write small anonymous functions inline.
    // They're often used with Comparators and functional interfaces.
    //
    // Python equivalent:  sorted(names, key=lambda x: len(x))
    // Java equivalent:    Arrays.sort(names, (a, b) -> a.length() - b.length())

    // ── Main ─────────────────────────────────────────────────────────

    public static void main(String[] args) {

        // 1. Primitives are passed by value (copied)
        System.out.println("=== 1. Pass by Value: Primitives ===");
        int num = 10;
        System.out.println("Before: num = " + num);
        tryToDoubleIt(num);
        System.out.println("After:  num = " + num);   // still 10!
        // Key insight: primitives are COPIED, so the method can't change
        // the caller's variable.
        System.out.println();

        // 2. Arrays/objects — reference is copied, but both point to same data
        System.out.println("=== 2. Pass by Value: References ===");
        int[] myArr = {1, 2, 3};
        System.out.println("Before doubleArray: " + Arrays.toString(myArr));
        doubleArray(myArr);
        System.out.println("After doubleArray:  " + Arrays.toString(myArr));
        // Changed! Because both references point to the same array.

        System.out.println();
        int[] myArr2 = {10, 20, 30};
        System.out.println("Before tryToReassign: " + Arrays.toString(myArr2));
        tryToReassign(myArr2);
        System.out.println("After tryToReassign:  " + Arrays.toString(myArr2));
        // NOT changed! Reassigning the local reference doesn't affect the caller.
        System.out.println();

        // 3. Scope and shadowing
        System.out.println("=== 3. Scope and Shadowing ===");
        showScope();
        System.out.println("  Outside: count = " + count);  // class-level: 100
        System.out.println();

        // 4. Method overloading for area
        System.out.println("=== 4. Overloaded area() Methods ===");
        System.out.printf("Circle (r=5):         %.2f%n", area(5.0));
        System.out.printf("Rectangle (4 x 6):    %.2f%n", area(4.0, 6.0));
        System.out.printf("Triangle (b=3, h=8):  %.2f%n", area(3.0, 8.0, true));
        // Java picks the right version based on the number/type of arguments.
        System.out.println();

        // 5. Lambda expressions with sorting
        System.out.println("=== 5. Lambda Expressions ===");

        // Sort strings by length using a lambda
        String[] names = {"Charlie", "Bo", "Alexandra", "Maya"};
        System.out.println("Before: " + Arrays.toString(names));

        Arrays.sort(names, (a, b) -> a.length() - b.length());
        System.out.println("Sorted by length: " + Arrays.toString(names));

        // Sort in reverse alphabetical order
        String[] fruits = {"banana", "apple", "cherry", "date"};
        Arrays.sort(fruits, (a, b) -> b.compareTo(a));
        System.out.println("Reverse alphabetical: " + Arrays.toString(fruits));

        // Using Comparator.comparingInt (cleaner than raw lambda)
        String[] words = {"elephant", "cat", "dog", "butterfly"};
        Arrays.sort(words, Comparator.comparingInt(String::length));
        System.out.println("By length (Comparator): " + Arrays.toString(words));

        // Lambda with explicit types (optional but sometimes clearer)
        Integer[] numbers = {5, 2, 8, 1, 9, 3};
        Arrays.sort(numbers, (Integer a, Integer b) -> b - a);  // descending
        System.out.println("Descending ints: " + Arrays.toString(numbers));
    }
}
