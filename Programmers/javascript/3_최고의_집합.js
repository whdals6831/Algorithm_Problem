function solution(n, s) {
    var answer = [];

    if (s < n) {
        return [-1];
    }

    let divideNumber = Math.floor(s/n);

    while (n > 0) {
        answer.push(divideNumber);
        s -= divideNumber;
        n--;
    }

    let lastIdx = answer.length-1;

    for (let i=s; i>0; i--) {
        answer[lastIdx] += 1;
        lastIdx--;
    }

    return answer;
}

console.log(solution(2,9));
console.log(solution(4,6));