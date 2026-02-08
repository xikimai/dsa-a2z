package ch18.solutions;

import java.util.*;

public class Warmup01Sol {
    public static int solve(int[] greed, int[] cookies) {
        Arrays.sort(greed);
        Arrays.sort(cookies);
        int child = 0, cookie = 0;
        while (child < greed.length && cookie < cookies.length) {
            if (cookies[cookie] >= greed[child]) child++;
            cookie++;
        }
        return child;
    }
}
