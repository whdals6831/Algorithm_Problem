function makeGrade(average) {
    if (average >= 90) {
        return 'A';
    }
    else if (average >= 80 && average < 90) {
        return 'B';
    }
    else if (average >= 70 && average < 80) {
        return 'C';
    }
    else if (average >= 50 && average < 70) {
        return 'D';
    }
    else {
        return 'F';
    }
}

function solution(scores) {
    var answer = '';

    for (let j=0; j<scores[0].length; j++) {
        let total = 0;
        let scoreCount = scores.length;
        let selfScore = scores[j][j];
        let minCount = 0;
        let maxCount = 0;

        for (let i=0; i<scoreCount; i++) {
            total += scores[i][j];

            if (i === j) continue;

            if (scores[i][j] < selfScore) {
                minCount++;
            }

            if (scores[i][j] > selfScore) {
                maxCount++;
            }
        }

        if (minCount === scoreCount-1 || maxCount === scoreCount-1) {
            total -= selfScore;
            scoreCount--;
        }

        answer += makeGrade(total/scoreCount);
    }

    return answer;
}