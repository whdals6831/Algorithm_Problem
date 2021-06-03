function solution(s) {
    let isUp = true;
    
    s = s.split("");

    for (var i=0; i<s.length; i++) {
        if (s[i] === ' ') {
            isUp = true;
            continue;
        }
        
        if (isUp) {
            s[i] = s[i].toUpperCase();
            isUp = false;
        }
        else {
            s[i] = s[i].toLowerCase();
        }

    }

    return s.join("");
}

console.log(solution("  3people   unFollowed me hEllo 1woRld"));