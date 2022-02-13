function solution(s) {
    let answer = '';
    let cnt = 0;

    for (let i in s) {
        if (s[i] === ' ') {
            cnt = 0;
            answer += ' ';
            continue;
        }

        if (cnt%2 === 0) {
            answer += s[i].toUpperCase();
        }
        else {
            answer += s[i].toLowerCase();
        }

        cnt++;
    }

    return answer;
}