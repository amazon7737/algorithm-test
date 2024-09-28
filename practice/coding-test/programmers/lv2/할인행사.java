import java.util.*;

class Solution {
    public int solution(String[] want, int[] number, String[] discount) {
        int answer = 0;
        
        Map<String, Integer> map = new HashMap();
        
        for(int i=0; i< want.length; i++){
            map.put(want[i], number[i]);
        }
        
        //System.out.println(map.get("banana"));
        
        int result = 0;
        int round = 0;
        int startNumber = 0;
        
        while (true){
            if(startNumber == discount.length-9){
                break;
            }
            
            Map<String, Integer> check = new HashMap();
            
            for(int i=0; i< want.length;i++){
                check.put(want[i], 0);
            }
            
            int count = 0;
            
            String[] items = new String[10];
            
            for(int i=0; i< 10; i++){
                //System.out.println(discount[startNumber+i]);
                
                items[i] = discount[startNumber+i];
            }
            
            for(int i=0; i< 10;i++){
                
                if(check.get(items[i]) == null){
                    continue;
                }else{
                    check.put(items[i], check.get(items[i])+1);
                }
                
                //System.out.println(items[i] + " " + check.get(items[i]));
                
            }
            
            for(int i=0; i< want.length;i++){
                
                
                if(map.get(want[i]) == check.get(want[i])){
                    //System.out.println(map.get(items[i]));
                    //System.out.println(check.get(items[i]));
                    count++;
                }
            }
            
            if(count == want.length){
                result++;
            }
            
            //System.out.println(check);
            
            startNumber++;
            //round++;
            
        }
        
            
        
        return result;
    }
}
