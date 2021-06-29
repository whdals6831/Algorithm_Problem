function solution(n, money) {
    let dp = new Array(n+1).fill(0);
    dp[0] = 1;

    for (let i=0; i<money.length; i++) {
        for (let j=0; j<n+1; j++) {
            if (j >= money[i]) {
                dp[j] += dp[j-money[i]];
            }
            // console.log(i, j, dp);
        }
    }

    return dp[n];
}

console.log(solution(5, [1,2,5]));