function solution(N, number) {
    var answer = -1;
    let dp = Array.from(Array(9), () => Array());
    dp = dp.map(array => new Set(array));

    dp[1].add(N);

    for (var i=2; i<9; i++) {
        for (var v of dp[i-1]) {
            dp[i].add(v+N);
            dp[i].add(v-N);
            dp[i].add(N-v);
            dp[i].add(v*N);
            dp[i].add(Math.floor(v/N));
            dp[i].add(Math.floor(N/v));
        }

        dp[i].add(Number(Array(i+1).join(N)));
    }

    for (var i=4; i<9; i++) { // 2개+2개, 3개-2개 같은 경우의 수
        let a=2;
        let b=i-a;

        while (a <= b) {
            let arr1 = [...dp[a]];
            let arr2 = [...dp[b]];
            for (var v1 of arr1) {
                for (var v2 of arr2) {
                    dp[i].add(v1+v2);
                    dp[i].add(Math.abs(v1-v2));
                    dp[i].add(Math.abs(v2-v1));
                    dp[i].add(v1*v2);
                    dp[i].add(Math.floor(v1/v2));
                    dp[i].add(Math.floor(v2/v1));
                }
            }
            a++;
            b--;
        }
    }

    for (var i=1; i<dp.length; i++) {
        if (dp[i].has(number)) {
            answer = i;
            break;
        }
    }

    return answer;
}

console.log(solution(5,12));
console.log(solution(4,17));
console.log(solution(2,11));
console.log(solution(8,53)); // 8*8-88/8

// 1   5
// 2   10,0,25,1,55 전 단계의 각 원소에 (사칙연산, 연속된 숫자 붙히기)