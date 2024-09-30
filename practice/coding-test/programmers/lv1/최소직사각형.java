import java.util.*;

class Solution {
    public int solution(int[][] sizes) {
        int answer = 0;
        
        for(int i=0; i< sizes.length; i++){
            if(sizes[i][0] < sizes[i][1]){
                int temp = sizes[i][1];
                sizes[i][1] = sizes[i][0];
                sizes[i][0] = temp;
            }
        }
        
        
        int[] left_array = new int[sizes.length];
        int[] right_array = new int[sizes.length];
        
        for(int i=0; i< sizes.length;i++){
            left_array[i] = sizes[i][0];
            right_array[i] = sizes[i][1];
        }
        
        int max_left = left_array[0];
        int max_right = right_array[0];
        
        
        for(int i=1; i< sizes.length;i++){
            if(max_left< left_array[i]){
                max_left = left_array[i];
            }
            
            if(max_right < right_array[i]){
                max_right = right_array[i];
            }
        }
        
        
        return max_left*max_right;
    }
}


/**
2024-09-30
**/

import java.util.*;


class Solution {

    public int solution(int[][] sizes) {

        int leftNumber = 0;
        int rightNumber = 0;

        for(int i=0; i< sizes.length;i++){

            if(sizes[i][0] < sizes[i][1]){
                int temp = sizes[i][0];
                sizes[i][0] = sizes[i][1];
                sizes[i][1] = temp;
            }

        }

        for(int j=0; j< sizes.length;j++){
            if(leftNumber < sizes[j][0]){
                leftNumber = sizes[j][0];
            }
            if(rightNumber < sizes[j][1]){
                rightNumber = sizes[j][1];
            }
        }

        //System.out.println(Arrays.toString(sizes));

        return leftNumber*rightNumber;
    }

}
