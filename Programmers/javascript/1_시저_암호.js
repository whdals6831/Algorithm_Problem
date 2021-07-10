function solution(s, n) {
    let answer = '';

    for (let i=0; i<s.length; i++) {
        if (s.charCodeAt(i) === 32) { // 공백
            answer += ' ';
        }
        else {
            let ascii = s.charCodeAt(i);
            let nAscii = ascii+n;

            if (ascii >= 65 && ascii <= 90) { // 대문자
                if (nAscii > 90) {
                    nAscii = nAscii%91 + 65;
                }
            }
            else {
                if (nAscii > 122) {
                    nAscii = nAscii%123 + 97;
                }
            }

            answer += String.fromCharCode(nAscii);
        }
    }

    return answer;
}

solution('s h', 2);