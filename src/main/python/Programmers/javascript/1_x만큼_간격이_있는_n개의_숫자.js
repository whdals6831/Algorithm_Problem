function solution(x, n) {
    var answer = [];
    let pushNumber = x;

    while (n > 0) {
        answer.push(pushNumber);
        pushNumber += x;
        n--;
    }

    return answer;
}