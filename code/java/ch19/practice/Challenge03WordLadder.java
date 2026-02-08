package ch19.practice;

import java.util.*;

/**
 * Challenge 3: Word Ladder
 * Chapter 19: Graphs I — Exploring Networks
 *
 * PROBLEM: Find shortest transformation from beginWord to endWord,
 *          changing one letter at a time. Return the length (number of words).
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Challenge03WordLadder {
    public static int solve(String beginWord, String endWord, List<String> wordList) {
        // TODO: Replace this with your solution
        return 0;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String beginWord = sc.next();
        String endWord = sc.next();
        List<String> wordList = new ArrayList<>();
        while (sc.hasNext()) wordList.add(sc.next());
        System.out.println(solve(beginWord, endWord, wordList));
        sc.close();
    }
}
