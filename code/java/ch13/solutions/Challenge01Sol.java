package ch13.solutions;
public class Challenge01Sol {
    public static int[][] solve(int[][] board) { bt(board); return board; }
    static boolean bt(int[][] b){
        for(int r=0;r<9;r++)for(int c=0;c<9;c++)if(b[r][c]==0){
            for(int n=1;n<=9;n++)if(valid(b,r,c,n)){b[r][c]=n;if(bt(b))return true;b[r][c]=0;}
            return false;}
        return true;
    }
    static boolean valid(int[][] b,int r,int c,int n){
        for(int i=0;i<9;i++){if(b[r][i]==n||b[i][c]==n)return false;}
        int br=3*(r/3),bc=3*(c/3);
        for(int i=br;i<br+3;i++)for(int j=bc;j<bc+3;j++)if(b[i][j]==n)return false;
        return true;
    }
}
