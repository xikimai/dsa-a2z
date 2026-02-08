package ch13.solutions;
import java.util.*;
public class Practice04Sol {
    public static List<String> solve(String digits) {
        if(digits.isEmpty())return new ArrayList<>();
        String[] map={"","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};
        List<String> res=new ArrayList<>(); bt(digits,0,"",map,res); return res;
    }
    static void bt(String d,int idx,String cur,String[] map,List<String> res){
        if(idx==d.length()){res.add(cur);return;}
        for(char c:map[d.charAt(idx)-'0'].toCharArray()) bt(d,idx+1,cur+c,map,res);
    }
}
