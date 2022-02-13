package programmers.Level_2;

public class 카카오프렌즈_컬러링북 {
    public int getArea(int color, int x, int y, int[][] picture) {
        if (x < 0 || y < 0 || x >= picture.length || y >= picture[0].length || picture[x][y] != color) {
            return 0;
        }
        picture[x][y] = 0;
        return 1 + getArea(color, x + 1, y, picture)
                + getArea(color, x, y + 1, picture)
                + getArea(color, x - 1, y, picture)
                + getArea(color, x, y - 1, picture);
    }

    public int[] solution(int m, int n, int[][] picture) {
        int numberOfArea = 0;
        int maxSizeOfOneArea = 0;
        int[][] picClone = new int[m][n];

        for (int i = 0; i < m; i++) { // 채점이 이상해서 복사한 후 사용
            for (int j = 0; j < n; j++) {
                picClone[i][j] = picture[i][j];
            }
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (picClone[i][j] > 0) {
                    numberOfArea++;
                    maxSizeOfOneArea = Math.max(maxSizeOfOneArea, getArea(picClone[i][j], i, j, picClone));
                }
            }
        }

        int[] answer = new int[2];
        answer[0] = numberOfArea;
        answer[1] = maxSizeOfOneArea;
        return answer;
    }
}

// [[1,1,1,0],
//  [1,2,2,0],
//  [1,0,0,1],
//  [0,0,0,1],
//  [0,0,0,3],
//  [0,0,0,3]]