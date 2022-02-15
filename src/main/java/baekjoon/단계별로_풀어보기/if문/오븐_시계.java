package baekjoon.단계별로_풀어보기.if문;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class 오븐_시계 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] startTime = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int cookTime = Integer.parseInt(br.readLine());
        int endHour = 0;
        int endMinute = 0;

        int cookHour = cookTime / 60;
        int cookMinute = cookTime % 60;

        if (cookMinute + startTime[1] >= 60) {
            cookHour += 1;
            endMinute = cookMinute + startTime[1] - 60;
        }
        else {
            endMinute = cookMinute + startTime[1];
        }

        if (cookHour + startTime[0] > 23) {
            endHour = cookHour + startTime[0] - 24;
        }
        else {
            endHour = cookHour + startTime[0];
        }

        System.out.println(endHour + " " + endMinute);
    }
}
