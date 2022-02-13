function solution(n) {
    let arr = new Array(100001);

    arr[0] = 0;
    arr[1] = 1;

    for (var i=2; i<=n; i++) {
        arr[i] = (arr[i-1] + arr[i-2])%1234567;
    }

    return arr[n];
}