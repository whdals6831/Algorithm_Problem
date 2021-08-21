function solution(scores) {
    var answer = '';

    for (let i=0; i<scores.length; i++) {
        let max = Math.max([...scores[i]]);
        let min = Math.min([...scores[i]]);
        let total = 0;
        let selfScoreMin = scores[i][i];
        let selfScoreMax = scores[i][i];

        for (let j=0; j<scores[i].length; j++) {
            if (i === j) continue;

            if (selfScoreMin >= scores[i][j]) {
                selfScoreMin = 0;
            }
        }
    }

    return answer;
}