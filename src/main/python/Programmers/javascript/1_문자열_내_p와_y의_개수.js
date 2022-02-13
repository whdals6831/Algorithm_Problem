function solution(s){
    let answer = true;
    let p = 0;
    let y = 0;

    for (var i of s) {
        if (i === 'p' || i === 'P') {
            p++;
        }
        else if (i === 'y' || i === 'Y') {
            y++;
        }
    }

    if (p !== y) {
        answer = false;
    }

    return answer;
}