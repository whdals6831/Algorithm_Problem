package programmers.Level_2;

import java.util.Arrays;

public class 피로도 {
    static int maxValue = Integer.MIN_VALUE;

    public int solution(int k, int[][] dungeons) {
        boolean[] visit = new boolean[dungeons.length];
        Arrays.fill(visit, true);
        findMaxEnterTheDungeon(k, 0, visit, dungeons);
        return maxValue;
    }

    public void findMaxEnterTheDungeon(int k, int count, boolean[] visit, int[][] dungeons) {

        if (count == visit.length) {
            maxValue = visit.length;
        }

        for (int i = 0; i < visit.length; i++) {
            if (visit[i] && dungeons[i][0] <= k) {
                visit[i] = false;
                findMaxEnterTheDungeon(k - dungeons[i][1], count + 1, visit, dungeons);
                visit[i] = true;
            }
            else {
                maxValue = Math.max(maxValue, count);
            }
        }
    }

    public static void main(String[] args) {
        피로도 s = new 피로도();
        int[][] dungeons = {{80,20},{50,40},{30,10}};
        System.out.println(s.solution(80, dungeons));
    }
}
