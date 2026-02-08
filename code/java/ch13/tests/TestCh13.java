package ch13.tests;

import java.util.*;

/**
 * Tests for Chapter 13: Bronze Battle Plan — Complete Search & Simulation
 *
 * Build and run:
 *   cd code/java
 *   javac ch13/tests/TestCh13.java
 *   java -ea ch13.tests.TestCh13
 */
public class TestCh13 {

    static int passed = 0;
    static int failed = 0;

    static void assertEquals(int expected, int actual, String msg) {
        if (expected == actual) { passed++; }
        else { failed++; System.out.println("FAIL: " + msg + " — expected " + expected + ", got " + actual); }
    }

    static void assertBoolEquals(boolean expected, boolean actual, String msg) {
        if (expected == actual) { passed++; }
        else { failed++; System.out.println("FAIL: " + msg + " — expected " + expected + ", got " + actual); }
    }

    static void assertStringEquals(String expected, String actual, String msg) {
        if (expected.equals(actual)) { passed++; }
        else { failed++; System.out.println("FAIL: " + msg + " — expected \"" + expected + "\", got \"" + actual + "\""); }
    }

    static void assertListEquals(List<?> expected, List<?> actual, String msg) {
        if (expected.equals(actual)) { passed++; }
        else { failed++; System.out.println("FAIL: " + msg + " — expected " + expected + ", got " + actual); }
    }

    static void assertArrayEquals(int[] expected, int[] actual, String msg) {
        if (Arrays.equals(expected, actual)) { passed++; }
        else { failed++; System.out.println("FAIL: " + msg + " — expected " + Arrays.toString(expected) + ", got " + Arrays.toString(actual)); }
    }

    // ── W1: Generate All Permutations ──
    static List<List<Integer>> refW1(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> results = new ArrayList<>();
        boolean[] used = new boolean[nums.length];
        btW1(nums, used, new ArrayList<>(), results);
        return results;
    }
    static void btW1(int[] nums, boolean[] used, List<Integer> cur, List<List<Integer>> res) {
        if (cur.size() == nums.length) { res.add(new ArrayList<>(cur)); return; }
        for (int i = 0; i < nums.length; i++) {
            if (used[i]) continue;
            used[i] = true; cur.add(nums[i]);
            btW1(nums, used, cur, res);
            cur.remove(cur.size()-1); used[i] = false;
        }
    }

    // ── W2: Generate All Subsets ──
    static List<List<Integer>> refW2(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();
        btW2(nums, 0, new ArrayList<>(), res);
        res.sort((a,b) -> { if (a.size()!=b.size()) return a.size()-b.size(); for(int i=0;i<a.size();i++){int c=Integer.compare(a.get(i),b.get(i));if(c!=0)return c;} return 0; });
        return res;
    }
    static void btW2(int[] nums, int idx, List<Integer> cur, List<List<Integer>> res) {
        if (idx == nums.length) { res.add(new ArrayList<>(cur)); return; }
        btW2(nums, idx+1, cur, res);
        cur.add(nums[idx]); btW2(nums, idx+1, cur, res); cur.remove(cur.size()-1);
    }

    // ── W3: Simulate Robot ──
    static int[] refW3(String commands) {
        int x=0, y=0;
        for (char c : commands.toCharArray()) {
            if (c=='U') y++; else if (c=='D') y--; else if (c=='L') x--; else if (c=='R') x++;
        }
        return new int[]{x, y};
    }

    // ── W4: Count Binary Strings ──
    static int refW4(int n) {
        if (n==1) return 2;
        int a=1, b=1;
        for (int i=2; i<=n; i++) { int na=a+b; b=a; a=na; }
        return a+b;
    }

    // ── W5: Tic-Tac-Toe ──
    static String refW5(char[][] board) {
        for (int i=0;i<3;i++) {
            if (board[i][0]==board[i][1]&&board[i][1]==board[i][2]&&board[i][0]!='.') return ""+board[i][0];
            if (board[0][i]==board[1][i]&&board[1][i]==board[2][i]&&board[0][i]!='.') return ""+board[0][i];
        }
        if (board[0][0]==board[1][1]&&board[1][1]==board[2][2]&&board[0][0]!='.') return ""+board[0][0];
        if (board[0][2]==board[1][1]&&board[1][1]==board[2][0]&&board[0][2]!='.') return ""+board[0][2];
        for (char[] r:board) for (char c:r) if (c=='.') return "Ongoing";
        return "Draw";
    }

    // ── P1: Subsets Bitmask ──
    static List<List<Integer>> refP1(int[] nums) {
        Arrays.sort(nums);
        int n=nums.length;
        List<List<Integer>> res = new ArrayList<>();
        for (int mask=0; mask<(1<<n); mask++) {
            List<Integer> sub = new ArrayList<>();
            for (int i=0;i<n;i++) if ((mask&(1<<i))!=0) sub.add(nums[i]);
            res.add(sub);
        }
        res.sort((a,b) -> { if (a.size()!=b.size()) return a.size()-b.size(); for(int i=0;i<a.size();i++){int c=Integer.compare(a.get(i),b.get(i));if(c!=0)return c;} return 0; });
        return res;
    }

    // ── P2: N-Queens Count ──
    static int refP2(int n) {
        int[] count = {0};
        Set<Integer> cols=new HashSet<>(), d1=new HashSet<>(), d2=new HashSet<>();
        btP2(0,n,cols,d1,d2,count);
        return count[0];
    }
    static void btP2(int row,int n,Set<Integer>cols,Set<Integer>d1,Set<Integer>d2,int[]count){
        if(row==n){count[0]++;return;}
        for(int c=0;c<n;c++){
            if(cols.contains(c)||d1.contains(row-c)||d2.contains(row+c))continue;
            cols.add(c);d1.add(row-c);d2.add(row+c);
            btP2(row+1,n,cols,d1,d2,count);
            cols.remove(c);d1.remove(row-c);d2.remove(row+c);
        }
    }

    // ── P3: Rat in Maze ──
    static List<String> refP3(int[][] maze) {
        int n=maze.length;
        if(n==0||maze[0][0]==0) return new ArrayList<>();
        List<String> res = new ArrayList<>();
        boolean[][] vis = new boolean[n][n];
        vis[0][0]=true;
        btP3(maze,0,0,n,"",vis,res);
        return res;
    }
    static void btP3(int[][] maze,int r,int c,int n,String path,boolean[][] vis,List<String> res){
        if(r==n-1&&c==n-1){res.add(path);return;}
        int[][] dirs={{1,0},{0,-1},{0,1},{-1,0}};
        char[] dn={'D','L','R','U'};
        for(int d=0;d<4;d++){
            int nr=r+dirs[d][0],nc=c+dirs[d][1];
            if(nr>=0&&nr<n&&nc>=0&&nc<n&&maze[nr][nc]==1&&!vis[nr][nc]){
                vis[nr][nc]=true;
                btP3(maze,nr,nc,n,path+dn[d],vis,res);
                vis[nr][nc]=false;
            }
        }
    }

    // ── P4: Letter Combinations ──
    static List<String> refP4(String digits) {
        if(digits.isEmpty()) return new ArrayList<>();
        String[] map={"","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};
        List<String> res = new ArrayList<>();
        btP4(digits,0,"",map,res);
        return res;
    }
    static void btP4(String digits,int idx,String cur,String[] map,List<String> res){
        if(idx==digits.length()){res.add(cur);return;}
        for(char c:map[digits.charAt(idx)-'0'].toCharArray()) btP4(digits,idx+1,cur+c,map,res);
    }

    // ── P5: Combination Sum ──
    static List<List<Integer>> refP5(int[] cands, int target) {
        Arrays.sort(cands);
        List<List<Integer>> res = new ArrayList<>();
        btP5(cands,target,0,new ArrayList<>(),0,res);
        return res;
    }
    static void btP5(int[] cands,int target,int start,List<Integer>cur,int sum,List<List<Integer>>res){
        if(sum==target){res.add(new ArrayList<>(cur));return;}
        for(int i=start;i<cands.length;i++){
            if(sum+cands[i]>target)break;
            cur.add(cands[i]);
            btP5(cands,target,i,cur,sum+cands[i],res);
            cur.remove(cur.size()-1);
        }
    }

    // ── C1: Sudoku Solver ──
    static int[][] refC1(int[][] board) {
        btC1(board); return board;
    }
    static boolean btC1(int[][] board) {
        for(int r=0;r<9;r++) for(int c=0;c<9;c++) if(board[r][c]==0){
            for(int num=1;num<=9;num++) if(validC1(board,r,c,num)){
                board[r][c]=num;
                if(btC1(board)) return true;
                board[r][c]=0;
            }
            return false;
        }
        return true;
    }
    static boolean validC1(int[][] b,int r,int c,int num){
        for(int i=0;i<9;i++){if(b[r][i]==num||b[i][c]==num)return false;}
        int br=3*(r/3),bc=3*(c/3);
        for(int i=br;i<br+3;i++) for(int j=bc;j<bc+3;j++) if(b[i][j]==num) return false;
        return true;
    }
    static boolean isValidSudoku(int[][] board) {
        for(int i=0;i<9;i++){
            Set<Integer> row=new HashSet<>(), col=new HashSet<>();
            for(int j=0;j<9;j++){row.add(board[i][j]);col.add(board[j][i]);}
            if(!row.equals(new HashSet<>(Arrays.asList(1,2,3,4,5,6,7,8,9))))return false;
            if(!col.equals(new HashSet<>(Arrays.asList(1,2,3,4,5,6,7,8,9))))return false;
        }
        return true;
    }

    // ── C2: Word Search ──
    static boolean refC2(char[][] board, String word) {
        int rows=board.length, cols=board[0].length;
        for(int r=0;r<rows;r++) for(int c=0;c<cols;c++)
            if(btC2(board,word,r,c,0)) return true;
        return false;
    }
    static boolean btC2(char[][] b,String w,int r,int c,int idx){
        if(idx==w.length()) return true;
        if(r<0||r>=b.length||c<0||c>=b[0].length||b[r][c]!=w.charAt(idx)) return false;
        char tmp=b[r][c]; b[r][c]='#';
        int[][] dirs={{-1,0},{1,0},{0,-1},{0,1}};
        for(int[] d:dirs) if(btC2(b,w,r+d[0],c+d[1],idx+1)){b[r][c]=tmp;return true;}
        b[r][c]=tmp; return false;
    }

    // ── C3: N-Queens All Solutions ──
    static List<List<String>> refC3(int n) {
        List<List<String>> res = new ArrayList<>();
        Set<Integer> cols=new HashSet<>(),d1=new HashSet<>(),d2=new HashSet<>();
        btC3(0,n,new ArrayList<>(),cols,d1,d2,res);
        res.sort((a,b)->{for(int i=0;i<a.size();i++){int c=a.get(i).compareTo(b.get(i));if(c!=0)return c;}return 0;});
        return res;
    }
    static void btC3(int row,int n,List<Integer> queens,Set<Integer>cols,Set<Integer>d1,Set<Integer>d2,List<List<String>>res){
        if(row==n){
            List<String> board = new ArrayList<>();
            for(int q:queens){char[]r=new char[n];Arrays.fill(r,'.');r[q]='Q';board.add(new String(r));}
            res.add(board); return;
        }
        for(int c=0;c<n;c++){
            if(cols.contains(c)||d1.contains(row-c)||d2.contains(row+c))continue;
            cols.add(c);d1.add(row-c);d2.add(row+c);queens.add(c);
            btC3(row+1,n,queens,cols,d1,d2,res);
            queens.remove(queens.size()-1);cols.remove(c);d1.remove(row-c);d2.remove(row+c);
        }
    }

    // ── C4: Fence Painting ──
    static int refC4(int[][] fences) {
        if(fences.length==0) return 0;
        Arrays.sort(fences,(a,b)->Integer.compare(a[0],b[0]));
        int total=0,cs=fences[0][0],ce=fences[0][1];
        for(int i=1;i<fences.length;i++){
            if(fences[i][0]<=ce) ce=Math.max(ce,fences[i][1]);
            else{total+=ce-cs;cs=fences[i][0];ce=fences[i][1];}
        }
        total+=ce-cs; return total;
    }

    // ── Test methods ──

    static void testW1() {
        assertListEquals(Arrays.asList(Arrays.asList(1,2,3),Arrays.asList(1,3,2),Arrays.asList(2,1,3),Arrays.asList(2,3,1),Arrays.asList(3,1,2),Arrays.asList(3,2,1)),
            refW1(new int[]{1,2,3}), "W1: [1,2,3]");
        assertEquals(1, refW1(new int[]{1}).size(), "W1: [1] size");
        assertEquals(24, refW1(new int[]{1,2,3,4}).size(), "W1: [1,2,3,4] size");
    }

    static void testW2() {
        assertEquals(8, refW2(new int[]{1,2,3}).size(), "W2: [1,2,3] size");
        assertEquals(1, refW2(new int[]{}).size(), "W2: [] size");
        assertEquals(2, refW2(new int[]{5}).size(), "W2: [5] size");
    }

    static void testW3() {
        assertArrayEquals(new int[]{0,0}, refW3("UUDDLR"), "W3: UUDDLR");
        assertArrayEquals(new int[]{3,3}, refW3("RRRUUU"), "W3: RRRUUU");
        assertArrayEquals(new int[]{0,0}, refW3(""), "W3: empty");
        assertArrayEquals(new int[]{-4,0}, refW3("LLLL"), "W3: LLLL");
    }

    static void testW4() {
        assertEquals(2, refW4(1), "W4: n=1");
        assertEquals(3, refW4(2), "W4: n=2");
        assertEquals(5, refW4(3), "W4: n=3");
        assertEquals(8, refW4(4), "W4: n=4");
        assertEquals(13, refW4(5), "W4: n=5");
        assertEquals(144, refW4(10), "W4: n=10");
    }

    static void testW5() {
        assertStringEquals("X", refW5(new char[][]{{'X','X','X'},{'O','O','.'},{'.','.','.'}}), "W5: X row");
        assertStringEquals("O", refW5(new char[][]{{'X','O','.'},{'X','O','.'},{'.',  'O','X'}}), "W5: O col");
        assertStringEquals("Draw", refW5(new char[][]{{'X','O','X'},{'O','X','O'},{'O','X','O'}}), "W5: Draw");
        assertStringEquals("Ongoing", refW5(new char[][]{{'X','O','.'},{'O','X','.'},{'.','.','.'}}), "W5: Ongoing");
    }

    static void testP1() {
        assertEquals(8, refP1(new int[]{1,2,3}).size(), "P1: [1,2,3] size");
        assertEquals(1, refP1(new int[]{}).size(), "P1: [] size");
        assertEquals(16, refP1(new int[]{4,2,3,1}).size(), "P1: [4,2,3,1] size");
    }

    static void testP2() {
        assertEquals(1, refP2(1), "P2: n=1");
        assertEquals(0, refP2(2), "P2: n=2");
        assertEquals(2, refP2(4), "P2: n=4");
        assertEquals(10, refP2(5), "P2: n=5");
        assertEquals(92, refP2(8), "P2: n=8");
    }

    static void testP3() {
        List<String> r = refP3(new int[][]{{1,0,0,0},{1,1,0,1},{1,1,0,0},{0,1,1,1}});
        assertListEquals(Arrays.asList("DDRDRR","DRDDRR"), r, "P3: 4x4 maze");
        assertListEquals(Arrays.asList(""), refP3(new int[][]{{1}}), "P3: 1x1");
        assertListEquals(new ArrayList<>(), refP3(new int[][]{{1,0},{0,1}}), "P3: no path");
    }

    static void testP4() {
        assertListEquals(Arrays.asList("ad","ae","af","bd","be","bf","cd","ce","cf"),
            refP4("23"), "P4: 23");
        assertListEquals(Arrays.asList("a","b","c"), refP4("2"), "P4: 2");
        assertListEquals(new ArrayList<>(), refP4(""), "P4: empty");
        assertEquals(27, refP4("234").size(), "P4: 234 size");
    }

    static void testP5() {
        assertListEquals(Arrays.asList(Arrays.asList(2,2,3),Arrays.asList(7)),
            refP5(new int[]{2,3,6,7}, 7), "P5: [2,3,6,7] t=7");
        assertListEquals(Arrays.asList(Arrays.asList(2,2,2,2),Arrays.asList(2,3,3),Arrays.asList(3,5)),
            refP5(new int[]{2,3,5}, 8), "P5: [2,3,5] t=8");
        assertListEquals(new ArrayList<>(), refP5(new int[]{2}, 1), "P5: [2] t=1");
    }

    static void testC1() {
        int[][] board = {
            {5,3,0,0,7,0,0,0,0},{6,0,0,1,9,5,0,0,0},{0,9,8,0,0,0,0,6,0},
            {8,0,0,0,6,0,0,0,3},{4,0,0,8,0,3,0,0,1},{7,0,0,0,2,0,0,0,6},
            {0,6,0,0,0,0,2,8,0},{0,0,0,4,1,9,0,0,5},{0,0,0,0,8,0,0,7,9}
        };
        int[][] result = refC1(board);
        assertBoolEquals(true, isValidSudoku(result), "C1: standard sudoku");
        assertEquals(5, result[0][0], "C1: preserves given");
    }

    static void testC2() {
        char[][] board = {{'A','B','C','E'},{'S','F','C','S'},{'A','D','E','E'}};
        assertBoolEquals(true, refC2(board, "ABCCED"), "C2: ABCCED");
        board = new char[][]{{'A','B','C','E'},{'S','F','C','S'},{'A','D','E','E'}};
        assertBoolEquals(true, refC2(board, "SEE"), "C2: SEE");
        board = new char[][]{{'A','B','C','E'},{'S','F','C','S'},{'A','D','E','E'}};
        assertBoolEquals(false, refC2(board, "ABCB"), "C2: ABCB");
        assertBoolEquals(true, refC2(new char[][]{{'A'}}, "A"), "C2: single match");
        assertBoolEquals(false, refC2(new char[][]{{'A'}}, "B"), "C2: single no match");
    }

    static void testC3() {
        assertEquals(1, refC3(1).size(), "C3: n=1 size");
        assertEquals(0, refC3(2).size(), "C3: n=2 size");
        assertEquals(2, refC3(4).size(), "C3: n=4 size");
        assertEquals(10, refC3(5).size(), "C3: n=5 size");
    }

    static void testC4() {
        assertEquals(7, refC4(new int[][]{{1,5},{3,8}}), "C4: overlapping");
        assertEquals(4, refC4(new int[][]{{1,3},{5,7}}), "C4: non-overlapping");
        assertEquals(9, refC4(new int[][]{{1,10},{2,5},{3,7}}), "C4: contained");
        assertEquals(5, refC4(new int[][]{{0,5}}), "C4: single");
        assertEquals(4, refC4(new int[][]{{1,3},{3,5}}), "C4: adjacent");
        assertEquals(4, refC4(new int[][]{{1,5},{1,5}}), "C4: fully overlapping");
    }

    public static void main(String[] args) {
        System.out.println("Chapter 13: Bronze Battle Plan — Complete Search & Simulation");
        System.out.println("=============================================================\n");

        testW1(); testW2(); testW3(); testW4(); testW5();
        testP1(); testP2(); testP3(); testP4(); testP5();
        testC1(); testC2(); testC3(); testC4();

        System.out.println();
        if (failed == 0) {
            System.out.println("All " + passed + " tests passed!");
        } else {
            System.out.println(passed + " passed, " + failed + " failed.");
            System.exit(1);
        }
    }
}
