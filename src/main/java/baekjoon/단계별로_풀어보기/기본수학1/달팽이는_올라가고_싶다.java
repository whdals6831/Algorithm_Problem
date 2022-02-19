package baekjoon.단계별로_풀어보기.기본수학1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class 달팽이는_올라가고_싶다 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] input = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        double a = input[0];
        double b = input[1];
        double v = input[2];

        System.out.println((long)(Math.ceil((v-a)/(a-b)) + 1));
    }
}
