package ch18.solutions;

public class Challenge04Sol {
    public static int solve(int[] ratings) {
        int n = ratings.length;
        if (n == 0) return 0;
        int[] candies = new int[n];
        java.util.Arrays.fill(candies, 1);
        for (int i = 1; i < n; i++) {
            if (ratings[i] > ratings[i - 1]) candies[i] = candies[i - 1] + 1;
        }
        for (int i = n - 2; i >= 0; i--) {
            if (ratings[i] > ratings[i + 1])
                candies[i] = Math.max(candies[i], candies[i + 1] + 1);
        }
        int sum = 0;
        for (int c : candies) sum += c;
        return sum;
    }
}
