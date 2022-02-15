package baekjoon.단계별로_풀어보기.if문;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class 알람시계 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] time = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int hour = time[0];
        int minute = time[1];

        if (minute < 45) {
            minute += 15;

            if (hour == 0) {
                hour = 23;
            }
            else {
                hour -= 1;
            }

            System.out.println(hour + " " + minute);

        } else {
            System.out.println(hour + " " + (minute - 45));
        }
    }
}
