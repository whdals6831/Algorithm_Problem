function solution(msg) {
    let answer = [];
    let dictionary = ['~'];

    for (let i=0; i<26; i++) {
        dictionary.push(String.fromCharCode(65+i));
    }

    let w = '';
    let c = '';

    for (let i=0; i<msg.length; i++) {
        w += msg[i];
        c = w+msg[i+1];

        if (dictionary.indexOf(c) === -1) {
            answer.push(dictionary.indexOf(w));
            dictionary.push(c);
            w = '';
        }
    }
    
    return answer;
}

console.log(solution("TOBEORNOTTOBEORTOBEORNOT"));