import java.util.*;

public class test {

  static boolean[] visited = new boolean[10];

  static int[] graph = {1,2,3,4,5,6,7,8,9};


  public static void main(String[] args) {

     dfs(0);

  }

  static void dfs(int index){
    //  방문처리
    visited[index] = true;

    System.out.println(index + " -> ");

    System.out.println("visited: " + Arrays.toString(visited));

    //System.out.println("graph: " + Arrays.toString(graph));

    for(int node : graph) {
      if(!visited[node]) {
        dfs(node);
      }
    }

  }

}
