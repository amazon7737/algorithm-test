class Solution {
    int answer = 0;
    
    public int solution(int n, int[][] computers) {
        
        boolean[] visited = new boolean[n];
        for(int i=0; i< n; i++){
            if(visited[i] == false){
                dfs(n, computers, visited, i);
                answer++;
            }
        }
        
        return answer;
    }
    
    public void dfs(int n, int[][] computers, boolean[] visited , int index){
        visited[index] = true;
        
        for(int i=0; i<n; i++){
            if(computers[index][i] == 1 && visited[i] == false && i!=index){
                dfs(n, computers, visited, i);
            }
        }
        
    }
    
}
