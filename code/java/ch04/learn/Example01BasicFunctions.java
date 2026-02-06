package ch04.learn;

/**
 * Example 01: Basic Functions
 * ===========================
 * Chapter 4: Functions
 *
 * This file shows you how Java defines and uses methods (functions).
 * You'll see basic method definitions, multiple parameters, return values,
 * method overloading, and functions calling functions.
 * Read through each section and run the file to see the output.
 *
 * Build and run:
 *   cd code/java
 *   javac ch04/learn/Example01BasicFunctions.java
 *   java ch04.learn.Example01BasicFunctions
 */
public class Example01BasicFunctions {

    // ── 1. Basic Method Definition ───────────────────────────────────
    // A method has: access modifier, return type, name, parameters, body.
    // 'static' means we can call it without creating an object.

    /** Prints a friendly greeting. No return value (void). */
    static void greet() {
        System.out.println("Hello from a method!");
    }

    // ── 2. Parameters and Return Values ──────────────────────────────
    // Parameters are the inputs; return type says what comes back.

    /** Returns the square of a number. */
    static int square(int n) {
        return n * n;
    }

    /** Adds two numbers and returns the result. */
    static int add(int a, int b) {
        return a + b;
    }

    // ── 3. Multiple Parameters and String Return ─────────────────────

    /** Builds a full name from first and last. */
    static String fullName(String first, String last) {
        return first + " " + last;
    }

    /** Checks if a number is in range [low, high] inclusive. */
    static boolean inRange(int value, int low, int high) {
        return value >= low && value <= high;
    }

    // ── 4. Method Overloading (Java's Way to Handle "Default" Params) ─
    // In Python, you can write def greet(name="World").
    // Java doesn't have default parameters, but you can define
    // multiple methods with the same name but different parameter lists.

    /** Greet a specific person. */
    static String greetPerson(String name) {
        return "Hello, " + name + "!";
    }

    /** Greet with a custom greeting. */
    static String greetPerson(String greeting, String name) {
        return greeting + ", " + name + "!";
    }

    /** Greet with greeting, name, and punctuation. */
    static String greetPerson(String greeting, String name, String punctuation) {
        return greeting + ", " + name + punctuation;
    }

    // ── 5. Functions Calling Functions ────────────────────────────────
    // Methods can call other methods. This is how you build complex
    // programs from simple building blocks.

    /** Calculate area of a rectangle. */
    static int rectangleArea(int width, int height) {
        return width * height;
    }

    /** Calculate area of a square (calls rectangleArea). */
    static int squareArea(int side) {
        return rectangleArea(side, side);   // reuse!
    }

    /** Calculate volume of a box (calls rectangleArea for the base). */
    static int boxVolume(int length, int width, int height) {
        int baseArea = rectangleArea(length, width);
        return baseArea * height;
    }

    // ── Main ─────────────────────────────────────────────────────────

    public static void main(String[] args) {

        // 1. Basic method call
        System.out.println("=== 1. Basic Method Definition ===");
        greet();
        System.out.println();

        // 2. Parameters and return values
        System.out.println("=== 2. Parameters and Return Values ===");
        System.out.println("square(5) = " + square(5));
        System.out.println("add(3, 7) = " + add(3, 7));

        // You can use the return value in expressions:
        int result = add(square(3), square(4));
        System.out.println("add(square(3), square(4)) = " + result);
        System.out.println();

        // 3. Multiple parameters
        System.out.println("=== 3. Multiple Parameters ===");
        System.out.println("fullName(\"Ada\", \"Lovelace\") = " + fullName("Ada", "Lovelace"));
        System.out.println("inRange(5, 1, 10) = " + inRange(5, 1, 10));
        System.out.println("inRange(15, 1, 10) = " + inRange(15, 1, 10));
        System.out.println();

        // 4. Method overloading
        System.out.println("=== 4. Method Overloading ===");
        System.out.println(greetPerson("Maya"));
        System.out.println(greetPerson("Hi", "Maya"));
        System.out.println(greetPerson("Hey", "Maya", "!!!"));
        // Java picks the right version based on what you pass in.
        // This is called "overloading" — same name, different signatures.
        System.out.println();

        // 5. Functions calling functions
        System.out.println("=== 5. Functions Calling Functions ===");
        System.out.println("rectangleArea(4, 5) = " + rectangleArea(4, 5));
        System.out.println("squareArea(4) = " + squareArea(4));
        System.out.println("boxVolume(3, 4, 5) = " + boxVolume(3, 4, 5));
    }
}
