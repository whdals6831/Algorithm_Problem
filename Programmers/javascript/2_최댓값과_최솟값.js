function solution(s) {
    var answer = '';
    s = s.split(' ').map((n) => Number(n));
    answer += `${Math.min(...s)} ${Math.max(...s)}`;
    return answer;
}