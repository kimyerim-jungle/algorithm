import java.math.BigInteger;
import java.util.*;
import java.io.BufferedReader;
import java.io.InputStreamReader;

class Main {
    public void test() throws Exception{
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int t = Integer.parseInt(reader.readLine());
        String string = reader.readLine();
        boolean seq = false;
        String num = "";
        BigInteger result = new BigInteger("0");

        for (int i=0; i<t; i++){
            char a = string.charAt(i);
            if (Character.isDigit(a)){ // 숫자면 연속인지 확인
                if (!seq)
                    seq = true;
                num += a;
            }
            else{
                if (seq){
                    seq = false;
                    result = result.add(BigInteger.valueOf(Integer.parseInt(num)));
                    num = "";
                }
            }
        }
        if (num.length() > 0)
            result = result.add(BigInteger.valueOf(Integer.parseInt(num)));

        sb.append(result.toString());
        System.out.println(sb);
    }
    public static void main(String[] args) throws Exception{
        new Main().test();
    }
}