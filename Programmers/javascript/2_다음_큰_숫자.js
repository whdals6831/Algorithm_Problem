function solution(n) {
    var answer = 0;
    var bin = n.toString(2).split("");

    var firstCnt = bin.reduce((acc, cur) => Number(acc) + Number(cur));

    for (var i=n+1; i<=1000000; i++) {
        var binNext = i.toString(2).split("");
        var secondCnt = binNext.reduce((acc, cur) => Number(acc) + Number(cur));

        if (firstCnt === secondCnt) {
            answer = i;
            break;
        }
    }

    return answer;
}

console.log(solution(78));

// 정규식을 사용한 다른 사람 풀이
// function nextBigNumber(n) {
//     var size = n.toString(2).match(/1/g).length
//     while(n++) {
//         if(size === n.toString(2).match(/1/g).length) return n
//     }
// }

// console.log(nextBigNumber(78));