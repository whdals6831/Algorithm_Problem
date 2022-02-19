package baekjoon.단계별로_풀어보기.기본수학1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class ACM_호텔 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int testCase = Integer.parseInt(br.readLine());

        for (int i = 0; i < testCase; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int h = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            int n = Integer.parseInt(st.nextToken());

            int floor = n % h;
            int room = (int)Math.ceil((double)n/h);

            if (floor == 0) {
                floor = h;
            }

            if (room < 10) {
                System.out.println(floor + "0" + room);
            } else {
                System.out.println(floor + "" + room);
            }
        }

    }
}
