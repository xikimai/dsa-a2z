package ch13.solutions;
import java.util.*;
public class Practice03Sol {
    public static List<String> solve(int[][] maze) {
        int n=maze.length; if(n==0||maze[0][0]==0)return new ArrayList<>();
        List<String> res=new ArrayList<>(); boolean[][] vis=new boolean[n][n]; vis[0][0]=true;
        bt(maze,0,0,n,"",vis,res); return res;
    }
    static void bt(int[][] m,int r,int c,int n,String path,boolean[][] vis,List<String> res){
        if(r==n-1&&c==n-1){res.add(path);return;}
        int[][] dirs={{1,0},{0,-1},{0,1},{-1,0}}; char[] dn={'D','L','R','U'};
        for(int d=0;d<4;d++){int nr=r+dirs[d][0],nc=c+dirs[d][1];
            if(nr>=0&&nr<n&&nc>=0&&nc<n&&m[nr][nc]==1&&!vis[nr][nc]){
                vis[nr][nc]=true;bt(m,nr,nc,n,path+dn[d],vis,res);vis[nr][nc]=false;}}
    }
}
