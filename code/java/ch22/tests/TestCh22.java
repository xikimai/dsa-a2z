package ch22.tests;

import java.util.*;

/**
 * Tests for Chapter 22: Stacks & Queues — Order Matters
 *
 * Build and run:
 *   cd code/java
 *   javac ch22/tests/TestCh22.java
 *   java -ea ch22.tests.TestCh22
 */
public class TestCh22 {

    // ── Helper methods ──────────────────────────────────────────────

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

    static void assertArrayEquals(int[] expected, int[] actual, String msg) {
        if (Arrays.equals(expected, actual)) { passed++; }
        else { failed++; System.out.println("FAIL: " + msg + " — expected " + Arrays.toString(expected) + ", got " + Arrays.toString(actual)); }
    }

    static void assertListEquals(List<Integer> expected, List<Integer> actual, String msg) {
        if (expected.equals(actual)) { passed++; }
        else { failed++; System.out.println("FAIL: " + msg + " — expected " + expected + ", got " + actual); }
    }

    // ── Reference solutions ─────────────────────────────────────────

    // W1: Valid Parentheses
    static boolean refValidParens(String s) {
        Deque<Character> stack = new ArrayDeque<>();
        for (char ch : s.toCharArray()) {
            if (ch == '(' || ch == '[' || ch == '{') { stack.push(ch); }
            else {
                if (stack.isEmpty()) return false;
                char top = stack.pop();
                if ((ch == ')' && top != '(') || (ch == ']' && top != '[') || (ch == '}' && top != '{')) return false;
            }
        }
        return stack.isEmpty();
    }

    // W2: Implement Stack
    static List<Integer> refStack(String[][] ops) {
        List<Integer> data = new ArrayList<>();
        List<Integer> results = new ArrayList<>();
        for (String[] op : ops) {
            switch (op[0]) {
                case "push": data.add(Integer.parseInt(op[1])); break;
                case "pop": results.add(data.isEmpty() ? -1 : data.remove(data.size() - 1)); break;
                case "top": results.add(data.isEmpty() ? -1 : data.get(data.size() - 1)); break;
                case "is_empty": results.add(data.isEmpty() ? 1 : 0); break;
            }
        }
        return results;
    }

    // W3: Implement Queue
    static List<Integer> refQueue(String[][] ops) {
        Deque<Integer> q = new ArrayDeque<>();
        List<Integer> results = new ArrayList<>();
        for (String[] op : ops) {
            switch (op[0]) {
                case "enqueue": q.offerLast(Integer.parseInt(op[1])); break;
                case "dequeue": results.add(q.isEmpty() ? -1 : q.pollFirst()); break;
                case "front": results.add(q.isEmpty() ? -1 : q.peekFirst()); break;
                case "is_empty": results.add(q.isEmpty() ? 1 : 0); break;
            }
        }
        return results;
    }

    // W4: Next Greater Element
    static int[] refNextGreater(int[] arr) {
        int n = arr.length;
        int[] result = new int[n];
        Arrays.fill(result, -1);
        Deque<Integer> stack = new ArrayDeque<>();
        for (int i = n - 1; i >= 0; i--) {
            while (!stack.isEmpty() && arr[stack.peek()] <= arr[i]) stack.pop();
            if (!stack.isEmpty()) result[i] = arr[stack.peek()];
            stack.push(i);
        }
        return result;
    }

    // W5: Min Stack
    static List<Integer> refMinStack(String[][] ops) {
        Deque<Integer> stack = new ArrayDeque<>(), minStack = new ArrayDeque<>();
        List<Integer> results = new ArrayList<>();
        for (String[] op : ops) {
            switch (op[0]) {
                case "push": {
                    int x = Integer.parseInt(op[1]);
                    stack.push(x);
                    minStack.push(minStack.isEmpty() || x <= minStack.peek() ? x : minStack.peek());
                    break;
                }
                case "pop": stack.pop(); minStack.pop(); break;
                case "top": results.add(stack.peek()); break;
                case "getMin": results.add(minStack.peek()); break;
            }
        }
        return results;
    }

    // P1: Daily Temperatures
    static int[] refDailyTemps(int[] temps) {
        int n = temps.length;
        int[] result = new int[n];
        Deque<Integer> stack = new ArrayDeque<>();
        for (int i = 0; i < n; i++) {
            while (!stack.isEmpty() && temps[stack.peek()] < temps[i]) {
                int j = stack.pop(); result[j] = i - j;
            }
            stack.push(i);
        }
        return result;
    }

    // P2: Evaluate RPN
    static int refEvalRPN(String[] tokens) {
        Deque<Integer> stack = new ArrayDeque<>();
        for (String t : tokens) {
            switch (t) {
                case "+": { int b = stack.pop(), a = stack.pop(); stack.push(a + b); break; }
                case "-": { int b = stack.pop(), a = stack.pop(); stack.push(a - b); break; }
                case "*": { int b = stack.pop(), a = stack.pop(); stack.push(a * b); break; }
                case "/": { int b = stack.pop(), a = stack.pop(); stack.push(a / b); break; }
                default: stack.push(Integer.parseInt(t));
            }
        }
        return stack.pop();
    }

    // P3: Sliding Window Maximum
    static int[] refSlidingWindowMax(int[] nums, int k) {
        Deque<Integer> dq = new ArrayDeque<>();
        int[] result = new int[nums.length - k + 1];
        int ri = 0;
        for (int i = 0; i < nums.length; i++) {
            while (!dq.isEmpty() && dq.peekFirst() < i - k + 1) dq.pollFirst();
            while (!dq.isEmpty() && nums[dq.peekLast()] <= nums[i]) dq.pollLast();
            dq.offerLast(i);
            if (i >= k - 1) result[ri++] = nums[dq.peekFirst()];
        }
        return result;
    }

    // P4: Queue Using Two Stacks
    static List<Integer> refQueueUsingStacks(String[][] ops) {
        Deque<Integer> in = new ArrayDeque<>(), out = new ArrayDeque<>();
        List<Integer> results = new ArrayList<>();
        for (String[] op : ops) {
            switch (op[0]) {
                case "enqueue": in.push(Integer.parseInt(op[1])); break;
                case "dequeue":
                    if (out.isEmpty()) while (!in.isEmpty()) out.push(in.pop());
                    results.add(out.pop()); break;
                case "peek":
                    if (out.isEmpty()) while (!in.isEmpty()) out.push(in.pop());
                    results.add(out.peek()); break;
                case "empty": results.add(in.isEmpty() && out.isEmpty() ? 1 : 0); break;
            }
        }
        return results;
    }

    // P5: Remove Adjacent Duplicates
    static String refRemoveAdjacentDups(String s) {
        Deque<Character> stack = new ArrayDeque<>();
        for (char ch : s.toCharArray()) {
            if (!stack.isEmpty() && stack.peek() == ch) stack.pop();
            else stack.push(ch);
        }
        StringBuilder sb = new StringBuilder();
        while (!stack.isEmpty()) sb.append(stack.pollLast());
        return sb.toString();
    }

    // C1: Largest Rectangle in Histogram
    static int refLargestRectangle(int[] heights) {
        Deque<Integer> stack = new ArrayDeque<>();
        int maxArea = 0, n = heights.length;
        for (int i = 0; i <= n; i++) {
            int curr = (i == n) ? 0 : heights[i];
            while (!stack.isEmpty() && heights[stack.peek()] > curr) {
                int h = heights[stack.pop()];
                int w = stack.isEmpty() ? i : i - stack.peek() - 1;
                maxArea = Math.max(maxArea, h * w);
            }
            stack.push(i);
        }
        return maxArea;
    }

    // C2: Trapping Rain Water
    static int refTrappingRain(int[] height) {
        if (height.length < 3) return 0;
        int left = 0, right = height.length - 1;
        int leftMax = height[left], rightMax = height[right], water = 0;
        while (left < right) {
            if (leftMax <= rightMax) {
                left++; leftMax = Math.max(leftMax, height[left]);
                water += leftMax - height[left];
            } else {
                right--; rightMax = Math.max(rightMax, height[right]);
                water += rightMax - height[right];
            }
        }
        return water;
    }

    // C3: Online Stock Span
    static int[] refStockSpan(int[] prices) {
        Deque<int[]> stack = new ArrayDeque<>();
        int[] result = new int[prices.length];
        for (int i = 0; i < prices.length; i++) {
            int span = 1;
            while (!stack.isEmpty() && stack.peek()[0] <= prices[i]) span += stack.pop()[1];
            stack.push(new int[]{prices[i], span});
            result[i] = span;
        }
        return result;
    }

    // C4: LRU Cache
    static List<Integer> refLRUCache(int capacity, String[][] ops) {
        LinkedHashMap<Integer, Integer> cache = new LinkedHashMap<>(capacity, 0.75f, true) {
            protected boolean removeEldestEntry(Map.Entry<Integer, Integer> eldest) {
                return size() > capacity;
            }
        };
        List<Integer> results = new ArrayList<>();
        for (String[] op : ops) {
            if (op[0].equals("get")) {
                int key = Integer.parseInt(op[1]);
                results.add(cache.getOrDefault(key, -1));
            } else if (op[0].equals("put")) {
                cache.put(Integer.parseInt(op[1]), Integer.parseInt(op[2]));
            }
        }
        return results;
    }

    // ── Test methods ────────────────────────────────────────────────

    static void testW1() {
        assertBoolEquals(true, refValidParens("()"), "W1: ()");
        assertBoolEquals(true, refValidParens("()[]{}"), "W1: ()[]{}");
        assertBoolEquals(true, refValidParens("{[]}"), "W1: {[]}");
        assertBoolEquals(false, refValidParens("([)]"), "W1: ([)]");
        assertBoolEquals(false, refValidParens("((("), "W1: (((");
        assertBoolEquals(true, refValidParens(""), "W1: empty");
        assertBoolEquals(false, refValidParens(")"), "W1: )");
        assertBoolEquals(true, refValidParens("({[(){}]})"), "W1: complex");
    }

    static void testW2() {
        assertListEquals(Arrays.asList(2, 2, 0), refStack(new String[][]{
            {"push","1"},{"push","2"},{"top","0"},{"pop","0"},{"is_empty","0"}}), "W2: basic");
        assertListEquals(Arrays.asList(-1, -1, 1), refStack(new String[][]{
            {"pop","0"},{"top","0"},{"is_empty","0"}}), "W2: empty ops");
        assertListEquals(Arrays.asList(30, 20, 10, 1), refStack(new String[][]{
            {"push","10"},{"push","20"},{"push","30"},
            {"pop","0"},{"pop","0"},{"pop","0"},{"is_empty","0"}}), "W2: push-pop all");
    }

    static void testW3() {
        assertListEquals(Arrays.asList(1, 1, 0), refQueue(new String[][]{
            {"enqueue","1"},{"enqueue","2"},{"front","0"},{"dequeue","0"},{"is_empty","0"}}), "W3: basic");
        assertListEquals(Arrays.asList(-1, -1, 1), refQueue(new String[][]{
            {"dequeue","0"},{"front","0"},{"is_empty","0"}}), "W3: empty ops");
        assertListEquals(Arrays.asList(10, 20, 30, 1), refQueue(new String[][]{
            {"enqueue","10"},{"enqueue","20"},{"enqueue","30"},
            {"dequeue","0"},{"dequeue","0"},{"dequeue","0"},{"is_empty","0"}}), "W3: FIFO order");
    }

    static void testW4() {
        assertArrayEquals(new int[]{5,10,10,-1,-1}, refNextGreater(new int[]{4,5,2,10,8}), "W4: basic");
        assertArrayEquals(new int[]{-1,-1,-1}, refNextGreater(new int[]{3,2,1}), "W4: decreasing");
        assertArrayEquals(new int[]{2,3,-1}, refNextGreater(new int[]{1,2,3}), "W4: increasing");
        assertArrayEquals(new int[]{-1}, refNextGreater(new int[]{5}), "W4: single");
        assertArrayEquals(new int[]{4,2,4,-1,-1}, refNextGreater(new int[]{2,1,2,4,3}), "W4: duplicates");
    }

    static void testW5() {
        assertListEquals(Arrays.asList(-3, 0, -2), refMinStack(new String[][]{
            {"push","-2"},{"push","0"},{"push","-3"},
            {"getMin","0"},{"pop","0"},{"top","0"},{"getMin","0"}}), "W5: basic");
        assertListEquals(Arrays.asList(5, 5), refMinStack(new String[][]{
            {"push","5"},{"top","0"},{"getMin","0"}}), "W5: single");
        assertListEquals(Arrays.asList(1, 2, 3), refMinStack(new String[][]{
            {"push","3"},{"push","2"},{"push","1"},
            {"getMin","0"},{"pop","0"},{"getMin","0"},{"pop","0"},{"getMin","0"}}), "W5: decreasing");
    }

    static void testP1() {
        assertArrayEquals(new int[]{1,1,4,2,1,1,0,0}, refDailyTemps(new int[]{73,74,75,71,69,72,76,73}), "P1: basic");
        assertArrayEquals(new int[]{1,1,1,0}, refDailyTemps(new int[]{30,40,50,60}), "P1: increasing");
        assertArrayEquals(new int[]{0,0,0}, refDailyTemps(new int[]{30,30,30}), "P1: all same");
        assertArrayEquals(new int[]{0,0,0,0}, refDailyTemps(new int[]{90,80,70,60}), "P1: decreasing");
        assertArrayEquals(new int[]{0}, refDailyTemps(new int[]{50}), "P1: single");
    }

    static void testP2() {
        assertEquals(9, refEvalRPN(new String[]{"2","1","+","3","*"}), "P2: (2+1)*3");
        assertEquals(6, refEvalRPN(new String[]{"4","13","5","/","+"}), "P2: 4+(13/5)");
        assertEquals(22, refEvalRPN(new String[]{"10","6","9","3","+","-11","*","/","*","17","+","5","+"}), "P2: complex");
        assertEquals(42, refEvalRPN(new String[]{"42"}), "P2: single");
        assertEquals(2, refEvalRPN(new String[]{"5","3","-"}), "P2: subtraction");
    }

    static void testP3() {
        assertArrayEquals(new int[]{3,3,5,5,6,7}, refSlidingWindowMax(new int[]{1,3,-1,-3,5,3,6,7}, 3), "P3: basic");
        assertArrayEquals(new int[]{1}, refSlidingWindowMax(new int[]{1}, 1), "P3: single");
        assertArrayEquals(new int[]{3}, refSlidingWindowMax(new int[]{1,3,2}, 3), "P3: k=n");
        assertArrayEquals(new int[]{5,5,5}, refSlidingWindowMax(new int[]{5,5,5,5}, 2), "P3: all same");
        assertArrayEquals(new int[]{9,7,5}, refSlidingWindowMax(new int[]{9,7,5,3,1}, 3), "P3: decreasing");
    }

    static void testP4() {
        assertListEquals(Arrays.asList(1, 1, 0), refQueueUsingStacks(new String[][]{
            {"enqueue","1"},{"enqueue","2"},{"peek","0"},{"dequeue","0"},{"empty","0"}}), "P4: basic");
        assertListEquals(Arrays.asList(10, 20, 30), refQueueUsingStacks(new String[][]{
            {"enqueue","10"},{"enqueue","20"},{"enqueue","30"},
            {"dequeue","0"},{"dequeue","0"},{"dequeue","0"}}), "P4: FIFO");
        assertListEquals(Arrays.asList(1, 0, 1, 1), refQueueUsingStacks(new String[][]{
            {"empty","0"},{"enqueue","1"},{"empty","0"},{"dequeue","0"},{"empty","0"}}), "P4: empty checks");
    }

    static void testP5() {
        assertStringEquals("ca", refRemoveAdjacentDups("abbaca"), "P5: abbaca");
        assertStringEquals("ay", refRemoveAdjacentDups("azxxzy"), "P5: azxxzy");
        assertStringEquals("abc", refRemoveAdjacentDups("abc"), "P5: abc");
        assertStringEquals("", refRemoveAdjacentDups("aabbcc"), "P5: aabbcc");
        assertStringEquals("a", refRemoveAdjacentDups("a"), "P5: single");
        assertStringEquals("", refRemoveAdjacentDups("abba"), "P5: abba");
    }

    static void testC1() {
        assertEquals(10, refLargestRectangle(new int[]{2,1,5,6,2,3}), "C1: basic");
        assertEquals(4, refLargestRectangle(new int[]{2,4}), "C1: two bars");
        assertEquals(5, refLargestRectangle(new int[]{5}), "C1: single");
        assertEquals(9, refLargestRectangle(new int[]{1,2,3,4,5}), "C1: increasing");
        assertEquals(9, refLargestRectangle(new int[]{5,4,3,2,1}), "C1: decreasing");
        assertEquals(12, refLargestRectangle(new int[]{3,3,3,3}), "C1: all same");
        assertEquals(12, refLargestRectangle(new int[]{6,2,5,4,5,1,6}), "C1: valley");
    }

    static void testC2() {
        assertEquals(6, refTrappingRain(new int[]{0,1,0,2,1,0,1,3,2,1,2,1}), "C2: basic");
        assertEquals(9, refTrappingRain(new int[]{4,2,0,3,2,5}), "C2: v-shape");
        assertEquals(0, refTrappingRain(new int[]{1,2,3}), "C2: increasing");
        assertEquals(0, refTrappingRain(new int[]{3,2,1}), "C2: decreasing");
        assertEquals(0, refTrappingRain(new int[]{}), "C2: empty");
        assertEquals(3, refTrappingRain(new int[]{3,0,3}), "C2: simple pool");
    }

    static void testC3() {
        assertArrayEquals(new int[]{1,1,1,2,1,4,6}, refStockSpan(new int[]{100,80,60,70,60,75,85}), "C3: basic");
        assertArrayEquals(new int[]{1,2,3,4,5}, refStockSpan(new int[]{1,2,3,4,5}), "C3: increasing");
        assertArrayEquals(new int[]{1,1,1,1,1}, refStockSpan(new int[]{5,4,3,2,1}), "C3: decreasing");
        assertArrayEquals(new int[]{1,2,3,4}, refStockSpan(new int[]{5,5,5,5}), "C3: all same");
        assertArrayEquals(new int[]{1}, refStockSpan(new int[]{10}), "C3: single");
    }

    static void testC4() {
        assertListEquals(Arrays.asList(1, -1, -1, 3, 4), refLRUCache(2, new String[][]{
            {"put","1","1"},{"put","2","2"},{"get","1"},
            {"put","3","3"},{"get","2"},
            {"put","4","4"},{"get","1"},{"get","3"},{"get","4"}}), "C4: basic");
        assertListEquals(Arrays.asList(10), refLRUCache(2, new String[][]{
            {"put","1","1"},{"put","1","10"},{"get","1"}}), "C4: update");
        assertListEquals(Arrays.asList(-1), refLRUCache(1, new String[][]{
            {"get","1"}}), "C4: get missing");
        assertListEquals(Arrays.asList(-1, 2, 3), refLRUCache(2, new String[][]{
            {"put","1","1"},{"put","2","2"},{"put","3","3"},
            {"get","1"},{"get","2"},{"get","3"}}), "C4: eviction");
        assertListEquals(Arrays.asList(10, -1, 20), refLRUCache(1, new String[][]{
            {"put","1","10"},{"get","1"},{"put","2","20"},{"get","1"},{"get","2"}}), "C4: cap=1");
    }

    // ── Main ────────────────────────────────────────────────────────

    public static void main(String[] args) {
        System.out.println("Chapter 22: Stacks & Queues — Order Matters");
        System.out.println("=============================================\n");

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
