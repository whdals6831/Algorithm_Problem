package baekjoon.단계별로_풀어보기.함수;

public class 정수_N개의_합 {
    public static void main(String[] args) {
        Test t = new Test();
        int[] list = {1, 2, 3, 4, 5};
        System.out.println(t.sum(list));
    }
}

class Test {
    public long sum(int[] a) {
        long total = 0;

        for (long n : a) {
            total += n;
        }

        return total;
    }
}