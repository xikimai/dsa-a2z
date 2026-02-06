package ch02.learn;

import java.util.Scanner;

/**
 * Example 02: Input/Output Patterns
 * ===================================
 * Chapter 2: Your First Programs — Speaking Three Languages
 *
 * This file shows you how to read input and print output in Java.
 * Java uses the Scanner class to read from the keyboard (System.in).
 *
 * Build and run:
 *   cd code/java
 *   javac ch02/learn/Example02IOPatterns.java
 *   java ch02.learn.Example02IOPatterns
 */
public class Example02IOPatterns {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // ── 1. Reading a String ─────────────────────────────────────
        System.out.println("=== Reading a String ===");
        System.out.print("Enter your name: ");
        String name = sc.nextLine();          // reads the entire line
        System.out.println("Hello, " + name + "!");
        System.out.println();

        // ── 2. Reading an Integer ───────────────────────────────────
        System.out.println("=== Reading an Integer ===");
        System.out.print("Enter your age: ");
        int age = sc.nextInt();               // reads one integer
        System.out.println("You are " + age + " years old.");
        System.out.println();

        // ── 3. Reading a Double ─────────────────────────────────────
        System.out.println("=== Reading a Double ===");
        System.out.print("Enter a temperature in Celsius: ");
        double celsius = sc.nextDouble();     // reads one double
        double fahrenheit = celsius * 9.0 / 5.0 + 32.0;
        System.out.println(celsius + " C = " + fahrenheit + " F");
        System.out.println();

        // ── 4. Reading Multiple Values on One Line ──────────────────
        System.out.println("=== Reading Two Integers ===");
        System.out.print("Enter two numbers (space-separated): ");
        int a = sc.nextInt();
        int b = sc.nextInt();
        System.out.println("Sum: " + (a + b));
        System.out.println();

        // ── 5. Common Gotcha: nextInt() + nextLine() ────────────────
        // After nextInt() or nextDouble(), the newline character stays
        // in the buffer. You need to call nextLine() to consume it
        // before reading the next line of text.
        //
        //   int x = sc.nextInt();
        //   sc.nextLine();              // <-- consume the leftover newline
        //   String line = sc.nextLine(); // <-- now this works correctly

        // ── 6. Formatted Output ─────────────────────────────────────
        System.out.println("=== Formatted Output ===");
        double pi = 3.14159265;
        System.out.printf("Pi to 2 decimals: %.2f%n", pi);   // 3.14
        System.out.printf("Pi to 4 decimals: %.4f%n", pi);   // 3.1416
        System.out.printf("%-10s %5d%n", "Score:", 100);      // left-align string, right-align number

        sc.close();
    }
}
