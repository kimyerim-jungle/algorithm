import java.io.BufferedReader;
import java.io.InputStreamReader;

class Main {
    public void test() throws Exception{
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        String num = reader.readLine();
        int real_num;

        if (num.charAt(0) == '0'){
            if (num.charAt(1) == 'x')
                real_num = Integer.parseInt(num, 2, num.length(), 16);
            else
                real_num = Integer.parseInt(num, 8);
        }
        else
            real_num = Integer.parseInt(num);

        sb.append(real_num);
        System.out.println(sb);
    }
    public static void main(String[] args) throws Exception{
        new Main().test();
    }
}