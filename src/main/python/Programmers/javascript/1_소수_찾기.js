function primeNumber() {
    let n = 1000000;
    let arr = new Array(n).fill(1);

    arr[0] = 0;
    arr[1] = 0;

    for (var i=2; i<parseInt(Math.sqrt(n)); i++) { // 에라토스테네스의 체
        if (arr[i] == 1) {
            for (var j=i+i; j<n; j=j+i) {
                arr[j] = 0
            }
        }
    }

    return arr;
}

function solution(n) {
    let answer = 0;
    let primeArr = primeNumber();

    for (let i=1; i<=n; i++) {
        if (primeArr[i] === 1) {
            answer++;
        }
    }

    return answer;
}