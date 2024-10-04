/**
a, b, c, d 네 개의 원소 중에서 두 개의 원소를 고르는 모든 경우의 수를 만드는 과정
**/
import java.util.*;

class Solution {
    
    ArrayList<ArrayList<String>> arr = new ArrayList<ArrayList<String>>();
    
    String[] array = {"a", "b", "c", "d"};
    
    int temp = 0;
    
    public int solution(int age) {
        
        try{
            dfs(array, 0, array[0]);
        }catch(ArrayIndexOutOfBoundsException e){
            return 0;
        }
        
        return 0;
    }
    
    void dfs(String[] array , int n, String step){
        
        //if(temp >= array.length){
            //return;
        //}
        
        for(int i=n+1; i<array.length; i++){
            
            ArrayList<String> list = new ArrayList<>();
            
            list.add(step);
            list.add(array[i]);
            arr.add(list);   
            
        }
        
        if(temp < array.length){
            temp++;
        }
        
        System.out.println("n: " + n + " " + "array:" + arr);
        System.out.println("temp: " + temp);
        
     	if(n == array.length){
        	return;
     	}else{
        	dfs(array, n+1, array[temp]);
        }
        
    }
    
}
