package baekjoon.단계별로_풀어보기.기본수학1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class 손익분기점 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] input = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        long a = input[0];
        long b = input[1];
        long c = input[2];

        if (b >= c) {
            System.out.println(-1);
        } else {
            System.out.println(a / (c - b) + 1);
        }
    }
}
