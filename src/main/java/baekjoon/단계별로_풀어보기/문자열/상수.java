package baekjoon.단계별로_풀어보기.문자열;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 상수 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");

        StringBuffer sb1 = new StringBuffer(input[0]);
        StringBuffer sb2 = new StringBuffer(input[1]);
        int reNum1 = Integer.parseInt(sb1.reverse().toString());
        int reNum2 = Integer.parseInt(sb2.reverse().toString());

        if (reNum1 > reNum2) {
            System.out.println(reNum1);
        } else {
            System.out.println(reNum2);
        }
    }
}
