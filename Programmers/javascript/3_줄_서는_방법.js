function factorial(n) {
    let result = 1;

    while (n > 0) {
        result *= n;
        n--;
    }

    return result;
}

function solution(n, k) {
    let answer = [];
    let nList = [];
    
    // 뽑아낼 번호 리스트 생성
    for (let i=1; i<n+1; i++) {
        nList.push(i);
    }

    let nFactorial = factorial(n);
    let pushNumIdx = 0;
    k -= 1;

    while (answer.length !== n) {
        nFactorial = nFactorial/nList.length;
        pushNumIdx = Math.floor(k/nFactorial);
        answer.push(nList[pushNumIdx]);
        k = k % nFactorial;
        nList.splice(pushNumIdx, 1);
    }
    return answer;
}

console.log(solution(3, 1));