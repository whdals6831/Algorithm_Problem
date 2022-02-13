function solution(n) {
    let dp = new Array(2001);
    dp[1] = 1;
    dp[2] = 2;

    for (var i=3; i<=n; i++) {
        dp[i] = (dp[i-1] + dp[i-2]) % 1234567;
    }

    return dp[n];
}

console.log(solution(6));