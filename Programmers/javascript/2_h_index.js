function solution(citations) {
    var answer = 0;
    var maxCitation = Math.max(...citations)

    for (var i=0; i<=maxCitation; i++) {
        var quotationCnt = 0;
        var remainCnt = 0;

        for (var j=0; j<citations.length; j++) {
            if (i <= citations[j]) {
                quotationCnt++;
            }
            else {
                remainCnt++;
            }
        }

        if (quotationCnt >= i && remainCnt < i) {
            answer = Math.max(answer, i);
        }
    }

    return answer;
}

console.log(solution([3, 0, 6, 1, 5]))