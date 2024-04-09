import java.math.BigInteger;
import java.nio.Buffer;
import java.util.*;
import java.io.BufferedReader;
import java.io.InputStreamReader;

class Main {
    int[] dx = {0, -1, 0, 1};
    int[] dy = {-1, 0, 1, 0};
    public int bfs(String start, int a, int b, String[][] color, int[][] visited, int maxW, int maxH){
        int count = 0;
        int[] pos = {a, b};
        Queue<int[]> queue = new LinkedList<>();
        queue.add(pos);

        while (!queue.isEmpty()){
            pos = queue.poll();
            int x = pos[0];
            int y = pos[1];

            if (visited[x][y] == 1)
                continue;

            visited[x][y] = 1;
            count++;
            for (int i=0; i<4; i++){
                int nx = x + dx[i];
                int ny = y + dy[i];
                if(0 <= nx && nx < maxW && 0 <= ny && ny < maxH && color[nx][ny].equals(start) && visited[nx][ny] == 0){
                    int[] next = {nx, ny};
                    queue.add(next);
                }
            }
        }

        return count;
    }

    public void test() throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        String nums = br.readLine();
        String[] numss = nums.split(" ");
        int h = Integer.parseInt(numss[0]);
        int w = Integer.parseInt(numss[1]);
        String[][] color = new String[w][h];
        int[][] visited = new int[w][h]; // 0으로 초기화
        int white = 0;
        int blue = 0;
        int mul;

        for (int i=0; i<w; i++){
            color[i] = br.readLine().split("");
        }

        for (int i=0; i<w; i++){
            for (int j=0; j<h; j++){
                if (color[i][j].equals("W")){
                    mul = bfs("W", i, j, color, visited, w, h);
                    white += mul*mul;
                }
                if (color[i][j].equals("B")){
                    mul = bfs("B", i, j, color, visited, w, h);
                    blue += mul*mul;
                }
            }
        }
        sb.append(white).append(' ');
        sb.append(blue);
        System.out.println(sb);
    }
    public static void main(String[] args) throws Exception{
        new Main().test();
    }
}