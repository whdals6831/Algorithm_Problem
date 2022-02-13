function search(s) {
    let _min = s.length;
    
    for (var cut=1; cut<=parseInt(s.length/2); cut++) { // 자르는 단위
        var result = '';
        var before = s.substr(0,cut); // 이전 단어
        var n = 1; // 단어 중복 횟수
        var last_idx = 0;

        for (var i=cut; i<=s.length; i+=cut) {
            var word = s.substr(i,cut);
            last_idx = i;

            if (word === before) {
                n++;
            }
            else { // 이전 단어와 다를 때
                if (n>1) {
                    result = result + String(n) + before;
                }
                else {
                    result = result + before;
                }
                before = word;
                n = 1;
            }
        }

        // 뒤에 남은 부분 더해주기
        result = result + s.substring(last_idx, s.length);
        _min = Math.min(_min, result.length);
    }
    
    return _min
}

function solution(s) {
    var answer = 0;
    
    answer = search(s);
    // console.log(answer)
    
    return answer;
}

// solution("aabbaccc");