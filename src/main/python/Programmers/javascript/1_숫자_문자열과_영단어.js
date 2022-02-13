function isNumeric(data) {
    return !isNaN(Number(data))
}

function solution(s) {
    let answer = "";
    let numDic = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
    }

    let key = "";

    for (let w of s) {
        if (isNumeric(w)) {
            answer += w;
        }
        else {
            key += w;

            if (numDic.hasOwnProperty(key)) {
                answer += numDic[key];
                key = "";
            }
        }
    }
    return Number(answer);
}