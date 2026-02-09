package ch32.learn;

import java.util.*;

/**
 * Example 01: Trie Basics — Building a Prefix Tree
 * Chapter 32: String Algorithms — Beyond Brute Force
 */
public class Example01TrieBasics {

    static int[][] children = new int[100001][26];
    static boolean[] isEnd = new boolean[100001];
    static int[] prefixCount = new int[100001];
    static int nodeCount = 0;

    static int newNode() {
        int id = ++nodeCount;
        Arrays.fill(children[id], 0);
        isEnd[id] = false;
        prefixCount[id] = 0;
        return id;
    }

    static void insert(int root, String word) {
        int node = root;
        for (char ch : word.toCharArray()) {
            int idx = ch - 'a';
            if (children[node][idx] == 0)
                children[node][idx] = newNode();
            node = children[node][idx];
            prefixCount[node]++;
        }
        isEnd[node] = true;
    }

    static boolean search(int root, String word) {
        int node = root;
        for (char ch : word.toCharArray()) {
            int idx = ch - 'a';
            if (children[node][idx] == 0) return false;
            node = children[node][idx];
        }
        return isEnd[node];
    }

    static int startsWith(int root, String prefix) {
        int node = root;
        for (char ch : prefix.toCharArray()) {
            int idx = ch - 'a';
            if (children[node][idx] == 0) return 0;
            node = children[node][idx];
        }
        return prefixCount[node];
    }

    public static void main(String[] args) {
        System.out.println("TRIE BASICS: Insert, Search, Prefix Operations");
        int root = newNode();
        String[] words = {"apple", "app", "application", "apt", "banana"};
        for (String w : words) insert(root, w);

        System.out.println("  search('app') = " + search(root, "app"));
        System.out.println("  search('ban') = " + search(root, "ban"));
        System.out.println("  startsWith('app') = " + startsWith(root, "app"));
        System.out.println("  startsWith('a') = " + startsWith(root, "a"));
    }
}
