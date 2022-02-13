package baekjoon.단계별로_풀어보기.입출력과_사칙연산;

import java.io.*;

public class 곱셈 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String v1 = br.readLine();
        String v2 = br.readLine();
        int total = 0;
        int totalDigit = 1;

        if (v1.length() < v2.length()) {
            String temp = v1;
            v1 = v2;
            v2 = temp;
        }

        int len1 = v1.length();
        int len2 = v2.length();

        for (int i = 1; i <= len2; i++) {

            int mulNum = Character.getNumericValue(v2.charAt(len2 - i));
            int mulResult = 0;
            int digit = 1;

            for (int j = 1; j <= len1; j++) {
                int n = Character.getNumericValue(v1.charAt(len1 - j));
                mulResult += n * mulNum * digit;
                digit *= 10;
            }

            System.out.println(mulResult);
            total += mulResult * totalDigit;
            totalDigit *= 10;
        }

        System.out.println(total);
    }
}
