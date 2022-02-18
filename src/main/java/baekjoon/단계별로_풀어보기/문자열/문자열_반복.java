package baekjoon.단계별로_풀어보기.문자열;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 문자열_반복 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int testCase = Integer.parseInt(br.readLine());

        for (int i = 0; i < testCase; i++) {
            String[] input = br.readLine().split(" ");
            int n = Integer.parseInt(input[0]);
            String s = input[1];
            String result = "";


            for (int j = 0; j < s.length(); j++) {
                char c = s.charAt(j);

                for (int k = 0; k < n; k++) {
                    result += c;
                }
            }

            System.out.println(result);
        }
    }
}
