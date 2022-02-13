package programmers.Level_2;

import java.util.PriorityQueue;

public class 더_맵게 {
    public int solution(int[] scoville, int K) {

        int answer = 0;
        // heap
        PriorityQueue<Integer> sortedScoville = new PriorityQueue<>();

        for (int s : scoville) {
            sortedScoville.add(s);
        }

        while (true) {
            if (sortedScoville.peek() >= K) {
                break;
            }

            if (sortedScoville.size() == 1) {
                answer = -1;
                break;
            }

            int mixScoville = sortedScoville.poll() + sortedScoville.poll()*2;
            sortedScoville.add(mixScoville);
            answer++;
        }

        return answer;
    }
}
