package ch03.learn;

/**
 * Example 01: Conditionals
 * ========================
 * Chapter 3: Decisions and Loops
 *
 * This file shows you how Java makes decisions with if/else, ternary
 * operators, switch statements, and logical operators.
 * Read through each section and run the file to see the output.
 *
 * Build and run:
 *   cd code/java
 *   javac ch03/learn/Example01Conditionals.java
 *   java ch03.learn.Example01Conditionals
 */
public class Example01Conditionals {

    public static void main(String[] args) {

        // ── 1. Basic if / else ─────────────────────────────────────────
        System.out.println("=== Basic if / else ===");

        int age = 14;

        if (age >= 18) {
            System.out.println("You can vote!");
        } else if (age >= 13) {
            System.out.println("You're a teenager.");
        } else {
            System.out.println("You're a kid.");
        }
        System.out.println();

        // ── 2. Comparison Operators ────────────────────────────────────
        System.out.println("=== Comparison Operators ===");
        System.out.println("10 == 10: " + (10 == 10));   // equal
        System.out.println("10 != 5:  " + (10 != 5));    // not equal
        System.out.println("10 > 5:   " + (10 > 5));     // greater than
        System.out.println("10 < 5:   " + (10 < 5));     // less than
        System.out.println("10 >= 10: " + (10 >= 10));   // greater or equal
        System.out.println("10 <= 5:  " + (10 <= 5));    // less or equal
        System.out.println();

        // ── 3. Logical Operators ───────────────────────────────────────
        System.out.println("=== Logical Operators ===");

        boolean hasTicket = true;
        boolean isVIP = false;

        // && means AND — both must be true
        System.out.println("hasTicket && isVIP: " + (hasTicket && isVIP));

        // || means OR — at least one must be true
        System.out.println("hasTicket || isVIP: " + (hasTicket || isVIP));

        // ! means NOT — flips true to false and vice versa
        System.out.println("!isVIP: " + (!isVIP));
        System.out.println();

        // Short-circuit evaluation: Java stops early if it already knows the answer
        // In (false && ...), Java doesn't even check the second part
        // In (true || ...), Java doesn't even check the second part
        System.out.println("Short-circuit: false && (1/0 > 0) won't crash!");
        System.out.println("Result: " + (false && (1 / 0 > 0)));  // safe!
        System.out.println();

        // ── 4. Ternary Operator ────────────────────────────────────────
        System.out.println("=== Ternary Operator ===");

        // condition ? valueIfTrue : valueIfFalse
        int score = 85;
        String grade = (score >= 90) ? "A" : (score >= 80) ? "B" : "C";
        System.out.println("Score " + score + " -> Grade " + grade);

        // Same thing using if/else:
        // String grade;
        // if (score >= 90) grade = "A";
        // else if (score >= 80) grade = "B";
        // else grade = "C";

        // Ternary is great for simple one-liners, but don't nest too deep!
        String parity = (42 % 2 == 0) ? "Even" : "Odd";
        System.out.println("42 is " + parity);
        System.out.println();

        // ── 5. Switch Statement ────────────────────────────────────────
        System.out.println("=== Switch Statement ===");

        int dayNumber = 3;
        String dayName;

        switch (dayNumber) {
            case 1:  dayName = "Monday";    break;
            case 2:  dayName = "Tuesday";   break;
            case 3:  dayName = "Wednesday"; break;
            case 4:  dayName = "Thursday";  break;
            case 5:  dayName = "Friday";    break;
            case 6:  dayName = "Saturday";  break;
            case 7:  dayName = "Sunday";    break;
            default: dayName = "Invalid";   break;
        }
        System.out.println("Day " + dayNumber + " is " + dayName);

        // Fall-through warning: without 'break', execution falls into the next case!
        System.out.println();
        System.out.println("Fall-through demo (weekend check):");
        switch (dayNumber) {
            case 6:
            case 7:
                System.out.println("  It's the weekend!");
                break;
            default:
                System.out.println("  It's a weekday.");
                break;
        }
        System.out.println();

        // ── 6. Nested Conditions ───────────────────────────────────────
        System.out.println("=== Nested Conditions ===");

        int temperature = 72;
        boolean isRaining = false;

        if (temperature > 60) {
            if (!isRaining) {
                System.out.println("Nice day for a walk!");
            } else {
                System.out.println("Warm but rainy — bring an umbrella.");
            }
        } else {
            System.out.println("It's cold — stay inside.");
        }

        // Tip: You can often flatten nested ifs using &&
        if (temperature > 60 && !isRaining) {
            System.out.println("(Same result with && instead of nesting)");
        }
    }
}
