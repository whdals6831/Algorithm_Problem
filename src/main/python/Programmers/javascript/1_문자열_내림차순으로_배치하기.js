function solution(s) {
    s = Array.from(s);
    
    s.sort((a,b) => {
        if (a > b) return -1;
        else return 1;
    });

    return s.join('');
}

console.log(solution("Zbcdefg"));