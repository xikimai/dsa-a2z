package ch13.solutions;
public class Warmup05Sol {
    public static String solve(char[][] board) {
        for(int i=0;i<3;i++){
            if(board[i][0]==board[i][1]&&board[i][1]==board[i][2]&&board[i][0]!='.')return""+board[i][0];
            if(board[0][i]==board[1][i]&&board[1][i]==board[2][i]&&board[0][i]!='.')return""+board[0][i];
        }
        if(board[0][0]==board[1][1]&&board[1][1]==board[2][2]&&board[0][0]!='.')return""+board[0][0];
        if(board[0][2]==board[1][1]&&board[1][1]==board[2][0]&&board[0][2]!='.')return""+board[0][2];
        for(char[]r:board)for(char c:r)if(c=='.')return"Ongoing";
        return"Draw";
    }
    public static void main(String[] args) { System.out.println(solve(new char[][]{{'X','X','X'},{'O','O','.'},{'.','.','.'}})); }
}
