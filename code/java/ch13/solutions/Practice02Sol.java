package ch13.solutions;
import java.util.*;
public class Practice02Sol {
    public static int solve(int n) {
        int[] count={0}; Set<Integer> c=new HashSet<>(),d1=new HashSet<>(),d2=new HashSet<>();
        bt(0,n,c,d1,d2,count); return count[0];
    }
    static void bt(int row,int n,Set<Integer>c,Set<Integer>d1,Set<Integer>d2,int[]count){
        if(row==n){count[0]++;return;}
        for(int col=0;col<n;col++){
            if(c.contains(col)||d1.contains(row-col)||d2.contains(row+col))continue;
            c.add(col);d1.add(row-col);d2.add(row+col);bt(row+1,n,c,d1,d2,count);
            c.remove(col);d1.remove(row-col);d2.remove(row+col);
        }
    }
}
