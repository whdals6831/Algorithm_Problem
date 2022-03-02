package baekjoon.단계별로_풀어보기.기본수학1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;

public class 큰_수_A더하기B {
    static void reverseArray(int[] array, int[] result) {
        for (int i = 0; i < array.length; i++) {
            result[i] = array[array.length - i - 1];
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] nums = br.readLine().split(" ");

        int[] n1 = nums[0].chars().map(x->x-'0').toArray();
        int[] n2 = nums[1].chars().map(x->x-'0').toArray();

        if (n1.length < n2.length) {
            int[] temp = n1;
            n1 = n2;
            n2 = temp;
        }

        int[] reNum1 = new int[n1.length + 1];
        int[] reNum2 = new int[n1.length + 1];
        int[] result = new int[n1.length + 1];

        Arrays.fill(reNum1, 0);
        Arrays.fill(reNum2, 0);

        reverseArray(n1, reNum1);
        reverseArray(n2, reNum2);

        for (int i = 0; i < n1.length; i++) {
            int temp = result[i];
            result[i] = (reNum1[i] + reNum2[i] + temp) % 10;
            result[i + 1] = (reNum1[i] + reNum2[i] + temp) / 10;
        }

        List<Integer> nList = (ArrayList<Integer>) Arrays.stream(result).boxed().collect(Collectors.toList());

        if (nList.get(nList.size() - 1) == 0) {
            nList.remove(nList.size() - 1);
        }

        Collections.reverse(nList);

        String answer = "";

        for (int n : nList) {
            answer += n;
        }

        System.out.println(answer);
    }
}
