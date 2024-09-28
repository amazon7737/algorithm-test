import java.util.*;

class Solution {
    public int solution(int[] picks, String[] minerals) {
        
        /**
        
        곡괭이당 광물 5개를 캔다 근데 피로도는 전부 다르다
        
        캐는 광물이 뭔지 -> 곡괭이를 사용했다 올려주고-> 광물에 따라서 피로도 올려주고 -> 5번 사용했으면 곡괭이 한개 제거 한다
        
        **/
        
        int fatigue = 0;
        int use = 5;
        int count = 0;
		String hand = "";
        
        //String[] target =  new String[5];
        
        while (true){
            
            // 철 곡괭이나 돌곡괭이를 먼저 들어버릴 경우
            
            // 다이아가 아예없다 -> 철 곡괭이 -> 없다 -> 돌 곡괭이
            // 철이 아예 없다 -> 돌곡괭이
            
            // 다이아가 연속으로 5개 -> 다이아 곡괭이
            // 철이 연속으로 5개 -> 철 곡괭이
            // 돌이 연속으로 5개 -> 돌 곡괭이
            
            
            if((picks[0] == 0) && (picks[1] == 0) && (picks[2] == 0) && (use == 5)){
                break;
            }
            
        	if (count == minerals.length){
                break;
            }
            
            //if(minerals.length >= 5){
                //if(minerals[count].equals("diamond") && ){
                //}
            //}
            
            if(count ==0){
                if(picks[count] == 0 && picks[count+1] == 0 && picks[count+2] == 0){
                    break;
                }
            }
            
            
            if(use == 5){
                    //System.out.println("!!!");
                    if(picks[0] >= 1){
                        use = 0;
                        hand = "diamond";
                        picks[0] -= 1;
                    }else if(picks[1] >= 1){
                        use = 0;
                        hand = "iron";
                        picks[1] -= 1;
                    }else if(picks[2] >= 1){
                        use = 0;
                        hand = "stone";
                        picks[2] -= 1;
                    }
            }
            
            //System.out.println("hand: " + hand);
            //System.out.println("minerals: " + minerals[count]);
            
            if(hand.equals("diamond")){
                fatigue += 1;
                use++;
            }else if(hand.equals("iron")){
                if(minerals[count].equals("diamond")){
                    fatigue += 5;
                    use++;
                }else{
                    fatigue += 1;
                    use++;
                }
            }else if(hand.equals("stone")){
                if(minerals[count].equals("diamond")){
                    fatigue += 25;
                    use++;
                }else if(minerals[count].equals("iron")){
                    fatigue += 5;
                    use++;
                }else{
                    fatigue += 1;
                    use++;
                }
            }
            
        	count ++;
            
        }
        
        return fatigue;
    }
    
}
