import java.io.*;
import java.util.LinkedList;
import java.util.Queue;

class Point {
        int width;
        int length;
        int height;
        int step;
}

public class Main {

    int[] DIRECTION_X = {1, -1, 0, 0, 0, 0};
    int[] DIRECTION_Y = {0, 0, 1, -1, 0, 0};
    int[] DIRECTION_Z = {0, 0, 0, 0, 1, -1};
    int DIRECTION_NUM = 6;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] line = br.readLine().split(" ");
        int width = Integer.parseInt(line[0]);
        int length = Integer.parseInt(line[1]);
        int height = Integer.parseInt(line[2]);

        int[][][] tomatoes = new int[height][length][width];
        for (int i = 0; i < height; i++){
            for (int j = 0; j < length; j++){
                line = br.readLine().split(" ");
                for (int k = 0; k < width; k++){
                    tomatoes[i][j][k] = Integer.parseInt(line[k]);
                }
            }
        }

        Queue<Point> queue = new LinkedList<>();

        for (int i = 0; i < height; i++){
            for (int j = 0; j < length; j++){
                for (int k = 0; k < length; k++){
                    if (tomatoes[i][j][k] == 1) {
                        Point p = new Point();
                        p.height = i;
                        p.length = j;
                        p.width = k;
                        p.step = 0;
                        queue.add(p);
                    }
                }
            }
        }

        while (queue.size() > 0) {
            for(Point now_p : queue) {

            }
        }


        System.out.println("hello");
    }

    public static void bfs(){

    }
}
