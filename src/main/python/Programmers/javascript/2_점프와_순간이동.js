function solution(n)
{
    var ans = 0;

    while (n != 0) {
        if (n % 2 == 0) {
            n = n/2;
        }
        else {
            n -= 1;
            ans++;
        }
    }

    return ans;
}

console.log(solution(5000));