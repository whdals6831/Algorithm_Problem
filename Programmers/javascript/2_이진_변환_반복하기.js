function solution(s) {
    let answer = [0, 0];
    let temp = '';
    while (s !== '1') {
        answer[0] += 1;

        for (let i of s) {
            if (i === '0') {
                answer[1] += 1;
            }
            else {
                temp += '1';
            }
        }

        s = temp.length.toString(2);
        temp = '';
    } 
    
    return answer;
}