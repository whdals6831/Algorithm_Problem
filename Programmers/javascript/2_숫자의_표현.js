function solution(n) {
    var answer = 0;

    for (var i=1; i<=n; i++) {
        var sum = i;
        var next = i+1;

        while(sum < n) {
            sum += next;
            next++;
        }

        if (sum === n) {
            answer++;
        }
    }

    return answer;
}