package ch13.solutions;
public class Warmup03Sol {
    public static int[] solve(String commands) {
        int x=0, y=0;
        for (char c : commands.toCharArray()) {
            if(c=='U')y++;else if(c=='D')y--;else if(c=='L')x--;else if(c=='R')x++;
        }
        return new int[]{x, y};
    }
    public static void main(String[] args) { int[] r = solve("RRRUUU"); System.out.println(r[0]+","+r[1]); }
}
