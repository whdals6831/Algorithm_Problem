function solution(N, stages) {
    let failureRate = new Array(N).fill(0);
    stages.sort((a,b) => a-b);
    let curIdx = 0;
    let startIdx = 0;
    let floor = 1;
    let challenger = 0;

    while (curIdx < stages.length) {
        if (floor >= stages[curIdx]) {
            challenger++;
            curIdx++;
        }
        else {
            failureRate[floor-1] = challenger/(stages.length-startIdx);
            floor++;
            startIdx = curIdx;
            challenger = 0;
        }
    }

    if (floor <= N) {
        failureRate[floor-1] = challenger/(stages.length-startIdx);
    }

    failureRate = failureRate.map((rate, idx) => [rate, idx+1]);

    failureRate.sort((a,b) => {
        if (a[0] > b[0]) return -1;
        if (a[0] < b[0]) return 1;
        if (a[1] < b[1]) return -1;
        if (a[1] > b[1]) return 1;
    });

    return failureRate.map(arr => arr[1]);
}

console.log(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]));
console.log(solution(4,[4,4,4,4,4]));