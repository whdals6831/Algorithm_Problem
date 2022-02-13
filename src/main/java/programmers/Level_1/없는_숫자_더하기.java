package programmers.Level_1;

import java.util.Arrays;

public class 없는_숫자_더하기 {
    public int solution(int[] numbers) {
        int answer = 0;
        boolean[] visit = new boolean[10];
        Arrays.fill(visit, true);

        for (int n : numbers) {
            visit[n] = false;
        }

        for (int i=0; i<10; i++) {
            if (visit[i]) {
                answer += i;
            }
        }

        return answer;
    }
}

//public class 없는_숫자_더하기 {
//    public static void main(String[] args) {
//        programmers.Level_1.Solution s = new programmers.Level_1.Solution();
//        int[] input = {1,2,3,4,6,7,8,0};
//        System.out.println(s.solution(input));
//    }
//}
