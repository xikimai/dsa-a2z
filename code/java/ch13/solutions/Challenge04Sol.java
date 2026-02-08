package ch13.solutions;
import java.util.*;
public class Challenge04Sol {
    public static int solve(int[][] fences) {
        if(fences.length==0)return 0;
        Arrays.sort(fences,(a,b)->Integer.compare(a[0],b[0]));
        int total=0,cs=fences[0][0],ce=fences[0][1];
        for(int i=1;i<fences.length;i++){
            if(fences[i][0]<=ce)ce=Math.max(ce,fences[i][1]);
            else{total+=ce-cs;cs=fences[i][0];ce=fences[i][1];}
        }
        total+=ce-cs;return total;
    }
}
