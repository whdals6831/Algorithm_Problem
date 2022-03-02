package baekjoon.단계별로_풀어보기.기본수학1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class 부녀회장이_될테야 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int testCase = Integer.parseInt(br.readLine());

        for (int i = 0; i < testCase; i++) {
            int k = Integer.parseInt(br.readLine());
            int n = Integer.parseInt(br.readLine());
            int[][] apart = new int[k+1][n+1];

            for (int[] a : apart) {
                Arrays.fill(a, 0);
            }

            for (int j = 1; j < n + 1; j++) {
                apart[0][j] = j;
            }

            for (int floor = 1; floor <= k; floor++) {
                for (int room = 1; room <= n; room++) {
                    apart[floor][room] = apart[floor-1][room] + apart[floor][room-1];
                }
            }

            System.out.println(apart[k][n]);
        }

    }
}
