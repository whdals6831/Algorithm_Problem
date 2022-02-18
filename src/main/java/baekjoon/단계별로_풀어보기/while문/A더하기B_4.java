package baekjoon.단계별로_풀어보기.while문;

import java.io.*;
import java.util.*;

public class A더하기B_4 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String nums = "";

        while ((nums = br.readLine()) != null && !nums.isEmpty()) {
            int[] temp = Arrays.stream(nums.split(" ")).mapToInt(Integer::parseInt).toArray();
            System.out.println(temp[0] + temp[1]);
        }
    }
}
