class Solution {
    public int solution(String s) {
        int answer = 0;
        String[] stringArray = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
        int[] numberArray = {0,1,2,3,4,5,6,7,8,9};

        
        for(int i=0; i<stringArray.length;i++){
            
         s = s.replace(stringArray[i], Integer.toString(numberArray[i]));
            
        }
        
        
        return Integer.parseInt(s);
    }
}
