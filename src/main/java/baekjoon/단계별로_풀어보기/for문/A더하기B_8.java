package baekjoon.단계별로_풀어보기.for문;

import java.io.*;
import java.util.*;

public class A더하기B_8 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int testCase = Integer.parseInt(br.readLine());

        for (int i = 1; i <= testCase; i++) {
            int[] nums = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            System.out.println("Case #" + i + ": " + nums[0] + " + " + nums[1] + " = " + (nums[0] + nums[1]));
        }
    }
}