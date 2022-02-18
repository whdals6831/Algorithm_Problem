package baekjoon.단계별로_풀어보기.문자열;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 다이얼 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        char[] input = br.readLine().toCharArray();
        String[] dial = {"ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"};
        int result = 0;

        for (char c : input) {
            for (int i = 0; i < dial.length; i++) {
                if (dial[i].indexOf(c) != -1) {
                    result += i + 3;
                }
            }
        }

        System.out.println(result);
    }
}
