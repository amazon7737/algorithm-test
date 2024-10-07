package examples;

/**
 * 팩토리얼 함수
 */
public class FactorialRecursive {

    public static int factorialRecursive(int n){
        if(n<=1){
            return 1;
        }

        return n * factorialRecursive(n-1);
    }

}
