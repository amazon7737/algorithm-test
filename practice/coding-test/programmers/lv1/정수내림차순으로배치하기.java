import java.util.*;
import java.util.Collections;

/**
* 2024-08-02 (금) 오후 09:01
**/

class Solution {
    public long solution(long n) {
        long answer = 0;
        
        String translateStr = String.valueOf(n);
        
        String[] list = translateStr.split("");
        
        Integer[] result = new Integer[list.length];
        
        for(int i=0; i<list.length; i++){
            
            result[i] = Integer.valueOf(list[i]);
            
        }
        
        Arrays.sort(result, Collections.reverseOrder());
        
        
        String str = "";
        
        for(int i=0; i< result.length;i++){
            str += String.valueOf(result[i]);
        }
        
        
        return Long.valueOf(str);
    }
}
