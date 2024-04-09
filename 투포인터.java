

public class 투포인터 {
    public static int n = 5; // 데이터의 개수 N
    public static int m = 5; // 찾고자 하는 부분합 M
    public static int[] arr = {1,2,3,2,5}; // 전체 수열

    public static void main(String[] args){
        int cnt = 0;
        int intervalSum = 0;
        int end = 0;

        for(int start = 0; start < n; start++){
            while(intervalSum < m &&end < n){
                intervalSum += arr[end];
                end += 1;
            }
            if(intervalSum == m){
                cnt += 1;
            }
            intervalSum -= arr[start];
        }

        System.out.println(cnt);
    }
}
