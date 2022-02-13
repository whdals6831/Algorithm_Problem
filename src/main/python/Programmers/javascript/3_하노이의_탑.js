let answer = [];

function hanoi(n, start, to, via) { // via는 경유지

    if (n === 1) {
        answer.push([start, to]);
        return;
    }

    hanoi(n-1, start, via, to); // 첫 번째 재귀에서는 맨 밑의 N번째 원반을 목적지로 옮기기 위해 위의 N-1 개의 원반을 경유지로 옮긴다.
    answer.push([start, to]); // 그 다음 N 번째 원반을 목적지로 옮긴다.
    hanoi(n-1, via, to, start); // 경유지에 있는 N-1 개의 원반을 to로 옮긴다.
}

function solution(n) {
    hanoi(n, 1, 3, 2);

    return answer;
}

console.log(solution(3));