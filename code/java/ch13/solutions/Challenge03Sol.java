package ch13.solutions;
import java.util.*;
public class Challenge03Sol {
    public static List<List<String>> solve(int n) {
        List<List<String>> res=new ArrayList<>();
        Set<Integer> c=new HashSet<>(),d1=new HashSet<>(),d2=new HashSet<>();
        bt(0,n,new ArrayList<>(),c,d1,d2,res);
        res.sort((a,b)->{for(int i=0;i<a.size();i++){int cmp=a.get(i).compareTo(b.get(i));if(cmp!=0)return cmp;}return 0;});
        return res;
    }
    static void bt(int row,int n,List<Integer>queens,Set<Integer>c,Set<Integer>d1,Set<Integer>d2,List<List<String>>res){
        if(row==n){List<String>board=new ArrayList<>();for(int q:queens){char[]r=new char[n];Arrays.fill(r,'.');r[q]='Q';board.add(new String(r));}res.add(board);return;}
        for(int col=0;col<n;col++){if(c.contains(col)||d1.contains(row-col)||d2.contains(row+col))continue;
            c.add(col);d1.add(row-col);d2.add(row+col);queens.add(col);bt(row+1,n,queens,c,d1,d2,res);
            queens.remove(queens.size()-1);c.remove(col);d1.remove(row-col);d2.remove(row+col);}
    }
}
