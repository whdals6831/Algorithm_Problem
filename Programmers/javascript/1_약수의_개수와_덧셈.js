function getMeasureLength(n) {
    let result = 0;

    for (let i=1; i<=n; i++) {
        if (n%i === 0) {
            result ++;
        }
    }

    return result;
}

function solution(left, right) {
    let answer = 0;

    for (let i=left; i<=right; i++) {
        if (getMeasureLength(i)%2 === 0) {
            answer += i;
        }
        else {
            answer -= i;
        }
    }

    return answer;
}