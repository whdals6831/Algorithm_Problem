function solution(n, words) {
    var answer = [];
    let arr = [];
    let nowPerson = 0;
    let cnt = 1;
    let beforeAlphabet = words[0][words[0].length-1];
    let flag = true;

    arr.push(words[0]);

    for (var i=1; i<words.length; i++) {
        nowPerson++;
        nowPerson = nowPerson % n;
        cnt++;

        if (!arr.includes(words[i]) && (words[i][0] === beforeAlphabet)) {
            arr.push(words[i]);
            beforeAlphabet = words[i][words[i].length-1];
        }
        else {
            flag = false;
            break;
        }
    }

    if (flag) {
        answer.push(0);
        answer.push(0);
    } else {
        answer.push(nowPerson+1);
        answer.push(Math.ceil(cnt/n));
    }

    return answer;
}

console.log(solution(3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]));

// 다른 사람 풀이

// function solution(n, words) {
//     var fail_i = -1;
//     for(var i = 1; i < words.length; i++){
//         var val = words[i];
//         if(
//             // 전단계의 끝말과 현단계 첫말이 다를 경우
//             words[i-1].substring(words[i-1].length-1) != val.substring(0, 1)
//             ||
//             // indexOf 함수는 첫번째로 값이 맞는 인덱스만 반환하므로
//             // 현재 인덱스와 맞지 않을 경우 중복된 값
//            words.indexOf(val) != i
//           ) {
//             fail_i = i;
//             break;
//         } 
//     }

//     if(fail_i == -1) return [0,0];

//     var no = fail_i%n + 1;
//     var turn = Math.floor(fail_i/n) + 1; 
//     return [no, turn];
// }