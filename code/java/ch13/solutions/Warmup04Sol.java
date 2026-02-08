package ch13.solutions;
public class Warmup04Sol {
    public static int solve(int n) {
        if (n==1) return 2;
        int a=1, b=1;
        for(int i=2;i<=n;i++){int na=a+b;b=a;a=na;}
        return a+b;
    }
    public static void main(String[] args) { System.out.println(solve(5)); }
}
