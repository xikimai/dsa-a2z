package ch02.learn;

/**
 * Example 01: Variables and Data Types
 * =====================================
 * Chapter 2: Your First Programs — Speaking Three Languages
 *
 * This file shows you how Java handles variables, data types, and type casting.
 * Read through each section and run the file to see the output.
 *
 * Build and run:
 *   cd code/java
 *   javac ch02/learn/Example01VariablesTypes.java
 *   java ch02.learn.Example01VariablesTypes
 */
public class Example01VariablesTypes {

    public static void main(String[] args) {

        // ── 1. Primitive Data Types ──────────────────────────────────
        System.out.println("=== Primitive Data Types ===");

        // Integer types (whole numbers)
        byte   smallNum   = 127;          // -128 to 127
        short  mediumNum  = 32000;        // -32,768 to 32,767
        int    normalNum  = 2_000_000;    // -2 billion to 2 billion (most common)
        long   bigNum     = 9_000_000_000L; // needs 'L' suffix for large values

        System.out.println("byte:  " + smallNum);
        System.out.println("short: " + mediumNum);
        System.out.println("int:   " + normalNum);
        System.out.println("long:  " + bigNum);
        System.out.println();

        // Floating-point types (decimals)
        float  pi_approx = 3.14f;        // needs 'f' suffix, ~7 digits precision
        double pi_better  = 3.14159265;  // ~15 digits precision (most common)

        System.out.println("float:  " + pi_approx);
        System.out.println("double: " + pi_better);
        System.out.println();

        // Boolean and char
        boolean isLearning = true;        // true or false only
        char    grade      = 'A';         // single character in single quotes

        System.out.println("boolean: " + isLearning);
        System.out.println("char:    " + grade);
        System.out.println();

        // ── 2. String (Reference Type) ──────────────────────────────
        System.out.println("=== Strings ===");

        String name = "Alex";             // double quotes for strings
        String greeting = "Hello, " + name + "!";  // string concatenation

        System.out.println("name:     " + name);
        System.out.println("greeting: " + greeting);
        System.out.println("length:   " + name.length());
        System.out.println();

        // ── 3. Type Casting ─────────────────────────────────────────
        System.out.println("=== Type Casting ===");

        // Widening (automatic) — small type to larger type, no data loss
        int    myInt    = 42;
        double myDouble = myInt;          // int -> double is safe
        System.out.println("int to double: " + myInt + " -> " + myDouble);

        // Narrowing (manual) — larger type to smaller type, may lose data!
        double score   = 95.7;
        int    rounded = (int) score;     // cast with (int) — TRUNCATES, does not round
        System.out.println("double to int: " + score + " -> " + rounded);
        System.out.println("  (notice: 95.7 becomes 95, not 96 — it truncates!)");
        System.out.println();

        // Integer division vs double division
        System.out.println("=== Integer vs Double Division ===");
        int a = 7;
        int b = 2;
        System.out.println("7 / 2 (int)    = " + (a / b));        // 3 (truncates)
        System.out.println("7.0 / 2 (double) = " + (7.0 / 2));   // 3.5
        System.out.println("(double) 7 / 2   = " + ((double) a / b)); // 3.5
        System.out.println();

        // ── 4. Constants ────────────────────────────────────────────
        System.out.println("=== Constants ===");

        final double SPEED_OF_LIGHT = 299_792_458.0; // 'final' means it can't change
        System.out.println("Speed of light: " + SPEED_OF_LIGHT + " m/s");
        // SPEED_OF_LIGHT = 100; // <-- This would cause a compile error!
        System.out.println();

        // ── 5. Operators ────────────────────────────────────────────
        System.out.println("=== Arithmetic Operators ===");
        System.out.println("10 + 3 = " + (10 + 3));   // addition
        System.out.println("10 - 3 = " + (10 - 3));   // subtraction
        System.out.println("10 * 3 = " + (10 * 3));   // multiplication
        System.out.println("10 / 3 = " + (10 / 3));   // integer division
        System.out.println("10 % 3 = " + (10 % 3));   // modulo (remainder)
        System.out.println();

        System.out.println("=== Comparison Operators ===");
        System.out.println("5 == 5: " + (5 == 5));    // equal to
        System.out.println("5 != 3: " + (5 != 3));    // not equal
        System.out.println("5 > 3:  " + (5 > 3));     // greater than
        System.out.println("5 < 3:  " + (5 < 3));     // less than
        System.out.println("5 >= 5: " + (5 >= 5));    // greater than or equal
        System.out.println("5 <= 3: " + (5 <= 3));    // less than or equal
    }
}
