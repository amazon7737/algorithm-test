
// 접두사 합을 활용한 구간 합 계산 소스코드
public class 접두사합 {
    public static int n = 5;
    public static int arr[] = {10, 20, 30, 40, 50};
    public static int[] prefixSum = new int[6];

    public static void main(String[] args){
        // 접두사 합(Prefix Sum) 배열 계산
        int sumValue = 0;

        for(int i =0; i<n; i++){
            sumValue += arr[i];
            prefixSum[i+1] = sumValue;
        }

        // 구간 합 계산(세 번째 수부터 네번째 수까지)
        int left = 3;
        int right = 4;
        System.out.println(prefixSum[right] - prefixSum[left-1]);

    }
}
