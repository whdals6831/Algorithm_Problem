package baekjoon.단계별로_풀어보기.if문;

import java.io.*;

public class 사분면_고르기 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n1 = Integer.parseInt(br.readLine());
        int n2 = Integer.parseInt(br.readLine());

        if (n1 > 0 && n2 > 0) {
            System.out.println(1);
        } else if (n1 < 0 && n2 > 0) {
            System.out.println(2);
        } else if (n1 < 0 && n2 < 0) {
            System.out.println(3);
        } else{
            System.out.println(4);
        }
    }
}
