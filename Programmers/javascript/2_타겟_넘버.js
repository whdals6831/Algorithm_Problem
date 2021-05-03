function dfs(numbers, target, idx, result) {
    if (numbers.length == idx) {
        if (target === result) {
            return 1;
        }
        else {
            return 0;
        }
    }

    return dfs(numbers, target, idx+1, result+numbers[idx]) + dfs(numbers, target, idx+1, result-numbers[idx])
}

function solution(numbers, target) {
    var answer = 0;
    answer = dfs(numbers, target, 0, 0);

    return answer;
}