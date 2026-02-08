package ch13.solutions;
import java.util.*;
public class Warmup01Sol {
    public static List<List<Integer>> solve(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> results = new ArrayList<>();
        boolean[] used = new boolean[nums.length];
        bt(nums, used, new ArrayList<>(), results);
        return results;
    }
    static void bt(int[] nums, boolean[] used, List<Integer> cur, List<List<Integer>> res) {
        if (cur.size() == nums.length) { res.add(new ArrayList<>(cur)); return; }
        for (int i = 0; i < nums.length; i++) {
            if (used[i]) continue;
            used[i] = true; cur.add(nums[i]); bt(nums, used, cur, res);
            cur.remove(cur.size()-1); used[i] = false;
        }
    }
    public static void main(String[] args) { System.out.println(solve(new int[]{1,2,3})); }
}
