package baekjoon.단계별로_풀어보기.문자열;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 그룹_단어_체커 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int ans = 0;

        for (int i = 0; i < n; i++) {
            String temp = "";
            char before = 0;
            char[] word = br.readLine().toCharArray();
            boolean isGroupWord = true;

            for (int j = 0; j < word.length; j++) {
                if (before == 0) {
                    before = word[j];
                    temp += word[j];
                    continue;
                }

                if (word[j] == before) continue;

                if (temp.indexOf(word[j]) == -1) {
                    before = word[j];
                    temp += word[j];
                } else {
                    isGroupWord = false;
                }
            }

            if (isGroupWord) {
                ans++;
            }

        }

        System.out.println(ans);

    }
}
