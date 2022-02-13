package programmers.Level_1;

import java.util.Arrays;

public class 최소직사각형 {
    public int solution(int[][] sizes) {
        int maxNumber = -1;
        int minNumber = -1;

        for (int i=0; i<sizes.length; i++) {
            int maxSize = Arrays.stream(sizes[i]).max().getAsInt();
            int minSize = Arrays.stream(sizes[i]).min().getAsInt();

            if (maxSize > maxNumber) {
                maxNumber = maxSize;
            }

            if (minSize > minNumber) {
                minNumber = minSize;
            }
        }

        return maxNumber*minNumber;
    }
}