import java.util.*;
import java.io.BufferedReader;
import java.io.InputStreamReader;

class Main {
    ArrayList<Integer>[] computer;
    ArrayList<Integer> visited;
    public int bfs(){
        int q, count = 0;
        Queue<Integer> queue = new LinkedList<>();
        queue.add(1);

        while (!queue.isEmpty()){
            q = queue.poll();

            if (visited.get(q) == 1){
                continue;
            }
            
            visited.set(q, 1);
            count++;
            for (Integer i : computer[q]){
                if (visited.get(i) == 0){
                    queue.add(i);
                }
            }
        }
        return count-1;
    }
    public void test() throws Exception{
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int v_num;
        int e_num;

        v_num = Integer.parseInt(reader.readLine());
        e_num = Integer.parseInt(reader.readLine());
        computer = new ArrayList[v_num+1];
        visited = new ArrayList(
                Collections.nCopies(v_num+1, 0)
        );
        for (int i = 0; i <= v_num; i++){
            computer[i] = new ArrayList<Integer>();
        }
        for (int i = 0; i < e_num; i++){
            StringTokenizer token = new StringTokenizer(reader.readLine());

            int a = Integer.parseInt(token.nextToken());
            int b = Integer.parseInt(token.nextToken());
            computer[a].add(b);
            computer[b].add(a);
        }
        int count = bfs();
        sb.append(count);
        System.out.println(sb);
    }
    public static void main(String[] args) throws Exception{
        new Main().test();
    }
}