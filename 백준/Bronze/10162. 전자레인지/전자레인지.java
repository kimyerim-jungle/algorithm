import java.math.BigInteger;
import java.nio.Buffer;
import java.util.*;
import java.io.BufferedReader;
import java.io.InputStreamReader;

class Main {

    public void test() throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int A = 300, B = 60, C = 10;
        int countA = 0, countB = 0, countC = 0;
        int T = Integer.parseInt(br.readLine());
        boolean succ = true;
        
        while (T != 0){
            if (T >= A){
                countA++;
                T -= A;
            }
            else if (T >= B){
                countB++;
                T -= B;
            }
            else if (T >= C){
                countC++;
                T -= C;
            }
            else {
                succ = false;
                break;
            }
            //System.out.println("T: " + T + " count A B C: " + countA + countB + countC);
        }

        if (succ)
            sb.append(countA).append(" ").append(countB).append(" ").append(countC);
        else
            sb.append(-1);
        System.out.println(sb);
    }
    public static void main(String[] args) throws Exception{
        new Main().test();
    }
}