package ch13.solutions;
import java.util.*;
public class Practice01Sol {
    public static List<List<Integer>> solve(int[] nums) {
        Arrays.sort(nums); int n=nums.length;
        List<List<Integer>> res = new ArrayList<>();
        for(int mask=0;mask<(1<<n);mask++){
            List<Integer> sub = new ArrayList<>();
            for(int i=0;i<n;i++) if((mask&(1<<i))!=0) sub.add(nums[i]);
            res.add(sub);
        }
        res.sort((a,b)->{if(a.size()!=b.size())return a.size()-b.size();for(int i=0;i<a.size();i++){int c=Integer.compare(a.get(i),b.get(i));if(c!=0)return c;}return 0;});
        return res;
    }
}
