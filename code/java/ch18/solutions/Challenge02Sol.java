package ch18.solutions;

public class Challenge02Sol {
    public static int solve(int[] gas, int[] cost) {
        int totalGas = 0, totalCost = 0;
        for (int i = 0; i < gas.length; i++) {
            totalGas += gas[i];
            totalCost += cost[i];
        }
        if (totalGas < totalCost) return -1;
        int start = 0, tank = 0;
        for (int i = 0; i < gas.length; i++) {
            tank += gas[i] - cost[i];
            if (tank < 0) { start = i + 1; tank = 0; }
        }
        return start;
    }
}
