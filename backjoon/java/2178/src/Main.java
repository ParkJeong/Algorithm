import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Queue;
import java.util.LinkedList;

public class Main {
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

            if (isDestination(curRow, curCol, mapRow, mapCol)) {
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
    private static boolean isNormalLocation(int row, int col, int mapRow, int mapCol, int[][] map){
        if ((row >= 0 && row < mapRow) && (col >= 0 && col < mapCol)){
            return (map[row][col] == 1);
        }
        return false;
    }

    private static boolean isDestination(int row, int col, int mapRow, int mapCol){
        return (row == mapRow - 1) && (col == mapCol - 1);
    }
}
