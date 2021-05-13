function make2Token(str) {
    var result = {};
    var reg = /[^A-Z]/; // 영문자 아닌 것들을 체크
    var len = 0;
    
    for (var i=0; i<str.length-1; i++) {
        var temp = (str[i]+str[i+1]).toUpperCase();
        if (reg.test(temp)) {
            continue;
        }
        else {
            if (temp in result) {
                result[temp] += 1;
            }
            else {
                result[temp] = 1;
            }
        }
    }

    for (var i in result) {
        len += result[i];
    }

    return [result, len];
}

function intersectionSize(tokenSet1, tokenSet2) { // 교집합
    var result = 0;

    for (var i in tokenSet1) {
        if (i in tokenSet2) {
            result += Math.min(tokenSet1[i], tokenSet2[i]);
        }
    }

    return result;
}

function solution(str1, str2) {
    var answer = 0;
      
    var token1 = make2Token(str1);
    var token2 = make2Token(str2);

    // console.log(token1[0]);
    // console.log(token2[0]);

    var result = intersectionSize(token1[0], token2[0]);
    var unionSize = token1[1] + token2[1] - result;

    answer = parseInt(65536 * result / unionSize);
    // console.log(result, unionSize);

    if (unionSize == 0) {
        answer = 65536;
    }

    return answer;
}

// console.log(solution("handshake", "shake hands"));
// console.log(solution("aa1+aa2", "AAAA12"));
// console.log(solution("AAbbaa_AA"," BBB"));
// console.log(solution('aaa','aaaa'));