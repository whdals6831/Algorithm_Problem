function solution(n) {
    var answer = '';

    while (n>0) {
        let reminder = n%3;
        n = parseInt(n/3);

        if (reminder == 0) {
            n -= 1; // 정확히 나누어 떨어지며 몫이 1이 생기기때문에 -1을 해줘야함
            reminder = 4;
        }

        answer = reminder + answer;
    }
    return answer;
}