class Solution {
    public int solution(int[] number) {
        int cnt =0;
        
        for(int i=0; i<number.length;i++){
            for(int j=i+1; j<number.length; j++){
                for(int w=j+1; w<number.length; w++){
                    if(number[i]+number[j]+number[w] ==0){
                        cnt ++;
                    }
                }
            }
        }
        
        return cnt;
        
    }
}
