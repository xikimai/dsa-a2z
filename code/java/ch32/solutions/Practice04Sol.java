package ch32.solutions;

public class Practice04Sol {
    public static int solve(String a, String b) {
        if (a.isEmpty() || b.isEmpty()) return b.isEmpty() ? 1 : -1;
        int repeats = (b.length() + a.length() - 1) / a.length(); // ceil division
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < repeats; i++) sb.append(a);
        if (sb.toString().contains(b)) return repeats;
        sb.append(a);
        if (sb.toString().contains(b)) return repeats + 1;
        return -1;
    }
}
