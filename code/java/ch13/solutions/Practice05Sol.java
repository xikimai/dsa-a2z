package ch13.solutions;
import java.util.*;
public class Practice05Sol {
    public static List<List<Integer>> solve(int[] cands, int target) {
        Arrays.sort(cands); List<List<Integer>> res=new ArrayList<>();
        bt(cands,target,0,new ArrayList<>(),0,res); return res;
    }
    static void bt(int[] c,int t,int s,List<Integer>cur,int sum,List<List<Integer>>res){
        if(sum==t){res.add(new ArrayList<>(cur));return;}
        for(int i=s;i<c.length;i++){if(sum+c[i]>t)break;cur.add(c[i]);bt(c,t,i,cur,sum+c[i],res);cur.remove(cur.size()-1);}
    }
}
