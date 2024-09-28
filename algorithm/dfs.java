public class dfs {

    static boolean[] visited = new boolean[10];

    static int[] graph = {1,2,3,4,5,6,7,8,9};

    public static void main(String[] args) {
        dfs(0);

    }

    static void dfs(int nodeIndex){
        // 방문처리
        visited[nodeIndex] = true;

        System.out.println(nodeIndex + " -> ");

        for(int node : graph){
            if(!visited[node]){
                dfs(node);
            }
        }
    }

}
