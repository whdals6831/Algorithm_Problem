package baekjoon.단계별로_풀어보기.if문;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class 주사위_세개 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] dice = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int one = dice[0];
        int two = dice[1];
        int three = dice[2];

        if (one == two && one == three) {
            System.out.println(10000 + one * 1000);
        } else if (one != two && two != three && one != three) {
            int maxNum = 0;

            for (int n : dice) {
                if (maxNum < n) {
                    maxNum = n;
                }
            }

            System.out.println(maxNum * 100);
        } else {
            int pair = 0;

            if (one == two) {
                pair = one;
            } else if (one == three) {
                pair = one;
            } else {
                pair = two;
            }

            System.out.println(1000 + pair * 100);
        }
    }
}
