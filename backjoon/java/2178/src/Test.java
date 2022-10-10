import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Queue;
import java.util.LinkedList;

public class Test {
    static final int[] DIRECTION_ROW = {1, 0, -1, 0};
    static final int[] DIRECTION_COL = {0, -1, 0, 1};
    static final int DIRECTION_NUM = 4;

    public static void main(String args[]) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        String[] line = bf.readLine().split(" ");
        int mapRow = Integer.valueOf(line[0]);
        int mapCol = Integer.valueOf(line[1]);
        int[][] map = new int[mapRow][mapCol];
        boolean[][] visited = new boolean[mapRow][mapCol];

        String tempLine;
        int curRow = 0;
        int curCol;
        while ((tempLine = bf.readLine()) != null){
            if (tempLine.equals("")){
                break;
            }
            char cell;
            for (curCol = 0; curCol < mapCol; curCol++) {
                cell = tempLine.charAt(curCol);
                map[curRow][curCol] = Character.getNumericValue(cell);
                visited[curRow][curCol] = false;
            }
            curRow++;
        }

        Queue<Integer[]> candidateCells = new LinkedList<>();
        Integer[] curCell;
        int move = 0;
        Integer[] firstCell = {0, 0, 1};
        candidateCells.add(firstCell);

        while (!candidateCells.isEmpty()) {
            curCell = candidateCells.poll();
            curRow = curCell[0];
            curCol = curCell[1];
            move = curCell[2];
            visited[curRow][curCol] = true;

            if ((curRow == mapRow - 1) && (curCol == mapCol - 1)) {
                System.out.println(move);
                return;
            }
            for (int i = 0; i < DIRECTION_NUM; i++) {
                int nextRow = curRow + DIRECTION_ROW[i];
                int nextCol = curCol + DIRECTION_COL[i];
                if (isNormalLocation(nextRow, nextCol, mapRow, mapCol, map) &&
                        !visited[nextRow][nextCol]) {
                    Integer[] candidate_cell = {nextRow, nextCol, move + 1};
                    candidateCells.add(candidate_cell);
                }
            }
        }
    }
    private static boolean isNormalLocation(int curRow, int curCol, int mapRow, int mapCol, int[][] map){
        if ((curRow >= 0 && curRow < mapRow) && (curCol >= 0 && curCol < mapCol)){
            return (map[curRow][curCol] == 1);
        }
        return false;
    }
//
//    private static boolean isDestination(int curRow, int curCol, int mapRow, int mapCol){
//        return (curRow == mapRow - 1) && (curCol == mapCol - 1);
//    }
}
