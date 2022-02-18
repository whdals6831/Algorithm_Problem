package baekjoon.단계별로_풀어보기.브루트포스;

import java.io.*;
import java.util.*;

public class 블랙잭 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int maxValue = 0;

        st = new StringTokenizer(br.readLine());
        List<Integer> cardList = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            cardList.add(Integer.parseInt(st.nextToken()));
        }

        for (int i = 0; i < cardList.size() - 2; i++) {
            for (int j = i + 1; j < cardList.size() - 1; j++) {
                for (int k = j + 1; k < cardList.size(); k++) {
                    int sum = cardList.get(i)+cardList.get(j)+cardList.get(k);

                    if (sum <= m && sum > maxValue) {
                        maxValue = sum;
                    }
                }
            }
        }

        System.out.println(maxValue);
    }
}
