function solution(n, t, m, p) {
    var answer = '';
    let words = '';
    let order = 1;

    for (var i=0; i <= t*m; i++) {
        words += i.toString(n).toUpperCase();
    }
    
    for (var i=0; i <= words.length; i++) {
        if (order === p) {
            answer += words[i];

            if (answer.length === t) {
                break;
            }
        }

        order++;

        if (order > m) {
            order = 1;
        }
    }
    
    return answer;
}

console.log(solution(16,16,2,1));