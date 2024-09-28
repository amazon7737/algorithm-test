import java.util.*;

class Solution {
    public int[] solution(long n) {
        String str = String.valueOf(n);
        
        int[] arr = new int[str.length()];
        
        int cnt = str.length();
        
        
        for(int i=str.length(); i>0; i--){
            try{
                arr[cnt-i] = Integer.parseInt(str.substring(i-1, i));
            }catch(StringIndexOutOfBoundsException e){
                continue;
            }catch(ArrayIndexOutOfBoundsException e){
                continue;
            }
        }
        
        
        return arr;
    }
}
