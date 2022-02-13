function solution(s){
    var answer = true;
    var q = [];

    for (var bracket of s) {
        if (bracket === "(") {
            q.push(bracket);
        }
        
        if (bracket === ")") {
            if (q.pop() === "(") {
                continue;
            }
            else {
                answer = false;
                break;
            }
        }
    }

    if (q.length > 0) {
        answer = false;
    }

    return answer;
}