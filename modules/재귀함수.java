/**
재귀함수
**/

class Solution {
    public String solution(String s) {
        String answer = "";
        
        int n = 10;
        System.out.println(recursiveSum(n));
        
        
        
        return answer;
    }
    
    int recursiveSum(int n){
        if(n == 1){
            return 1; // 더이상 쪼개지지 않을때
        }
        
        System.out.println(String.valueOf(n) + " + " + String.valueOf(n-1));
        
        return n + recursiveSum(n-1);
    }
}
