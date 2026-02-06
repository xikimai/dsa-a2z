package ch02.practice;

import java.util.Scanner;

/**
 * Warmup 01: Greeting
 * ==============================
 * Chapter 2: Your First Programs
 *
 * PROBLEM
 * -------
 * Given a person's name, return a greeting in the format "Hello, <name>!".
 *
 * INPUT FORMAT
 * ------------
 * A single line containing a name (a string, may include spaces).
 *
 * OUTPUT FORMAT
 * -------------
 * Print the greeting: Hello, <name>!
 *
 * CONSTRAINTS
 * -----------
 * 1 <= name.length() <= 100
 *
 * EXAMPLES
 * --------
 * Input:  Alex
 * Output: Hello, Alex!
 *
 * Input:  World
 * Output: Hello, World!
 *
 * Input:  Ada Lovelace
 * Output: Hello, Ada Lovelace!
 *
 * INSTRUCTIONS
 * ------------
 * Replace the "return "";" in the solve() method with your solution.
 * The main method handles input/output — don't change it.
 */
public class Warmup01Greeting {

    /**
     * Return a greeting for the given name.
     *
     * @param name the person's name
     * @return a string in the format "Hello, <name>!"
     */
    public static String solve(String name) {
        // TODO: Replace this with your solution
        return "";
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String name = scanner.nextLine();
        System.out.println(solve(name));
        scanner.close();
    }
}
