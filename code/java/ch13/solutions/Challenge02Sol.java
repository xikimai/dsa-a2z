package ch13.solutions;
public class Challenge02Sol {
    public static boolean solve(char[][] board, String word) {
        for(int r=0;r<board.length;r++)for(int c=0;c<board[0].length;c++)
            if(bt(board,word,r,c,0))return true;
        return false;
    }
    static boolean bt(char[][] b,String w,int r,int c,int idx){
        if(idx==w.length())return true;
        if(r<0||r>=b.length||c<0||c>=b[0].length||b[r][c]!=w.charAt(idx))return false;
        char tmp=b[r][c];b[r][c]='#';
        int[][] dirs={{-1,0},{1,0},{0,-1},{0,1}};
        for(int[] d:dirs)if(bt(b,w,r+d[0],c+d[1],idx+1)){b[r][c]=tmp;return true;}
        b[r][c]=tmp;return false;
    }
}
