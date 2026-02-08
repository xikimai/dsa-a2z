package ch13.solutions;
import java.util.*;
public class Warmup02Sol {
    public static List<List<Integer>> solve(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();
        bt(nums, 0, new ArrayList<>(), res);
        res.sort((a,b) -> {if(a.size()!=b.size())return a.size()-b.size();for(int i=0;i<a.size();i++){int c=Integer.compare(a.get(i),b.get(i));if(c!=0)return c;}return 0;});
        return res;
    }
    static void bt(int[] nums, int idx, List<Integer> cur, List<List<Integer>> res) {
        if (idx == nums.length) { res.add(new ArrayList<>(cur)); return; }
        bt(nums, idx+1, cur, res);
        cur.add(nums[idx]); bt(nums, idx+1, cur, res); cur.remove(cur.size()-1);
    }
    public static void main(String[] args) { System.out.println(solve(new int[]{1,2,3})); }
}
