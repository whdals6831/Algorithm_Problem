function solution(n, money) {
    let dp = new Array(n+1).fill(0);
    dp[0] = 1;

    for (let i=0; i<money.length; i++) {
        for (let j=0; j<n+1; j++) {
            if (j >= money[i]) {
                dp[j] += dp[j-money[i]]; // 현재의 거스름돈을 제외한 이전의 거스름돈 dp에서의 경우의 수를 더해줌
            }
            // console.log(i, j, dp);
        }
    }

    return dp[n];
}

console.log(solution(5, [1,2,5]));