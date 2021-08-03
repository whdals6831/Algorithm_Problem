function solution(n)
{
    var answer = 0;

    for (let i of String(n)) {
        answer += Number(i);
    }

    return answer;
}