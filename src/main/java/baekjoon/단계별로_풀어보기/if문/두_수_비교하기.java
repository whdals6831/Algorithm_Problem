package baekjoon.단계별로_풀어보기.if문;

import java.io.*;
import java.util.*;

public class 두_수_비교하기 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] line = br.readLine().split(" ");
        int[] nums = Arrays.stream(line).mapToInt(Integer::parseInt).toArray();

        if (nums[0] > nums[1]) {
            System.out.println(">");
        } else if (nums[0] < nums[1]) {
            System.out.println("<");
        } else {
            System.out.println("==");
        }
    }
}
