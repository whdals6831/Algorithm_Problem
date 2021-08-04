function solution(d, budget) {
    let answer = 0;

    d.sort((a,b) => a-b);

    for (let money of d) {
        if (money <= budget) {
            answer++;
            budget -= money;
        }
    }

    return answer;
}