function solution(phone_number) {
    let answer = '*';
    let len = phone_number.length;

    answer = answer.repeat(len-4);

    for (let i=len-4; i<len; i++) {
        answer += phone_number[i];
    }

    return answer;
}