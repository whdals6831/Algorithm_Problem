package baekjoon.단계별로_풀어보기.일차원_배열;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 최댓값 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int idx = 1;
        int max = 0;
        int maxIdx = 1;

        while (true) {
            int n = Integer.parseInt(br.readLine());

            if (max < n) {
                max = n;
                maxIdx = idx;
            }

            idx++;

            if (idx == 10) {
                break;
            }
        }

        System.out.println(max);
        System.out.println(maxIdx);
    }
}
