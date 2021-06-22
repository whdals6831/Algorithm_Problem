function solution(jobs) {
    let answer = 0;
    let curEndPoint = 0;
    let visited = new Array(jobs.length).fill(false);

    jobs.sort((a,b) => {
        if (a[0]<b[0]) return -1;
        if (a[0]>b[0]) return 1;
        if (a[1]<b[1]) return -1;
        if (a[1]>b[1]) return 1; 
    });

    answer += jobs[0][1];
    curEndPoint = jobs[0][0] + jobs[0][1];
    visited[0] = true;

    for (let i=1; i<jobs.length; i++) {
        let temp = [];
        let isCrash = false;

        for (let j=1; j<jobs.length; j++) {
            if (visited[j]) continue;

            if (jobs[j][0] <= curEndPoint) {
                temp.push([...jobs[j], j]);
                isCrash = true;
            }
            else {
                break
            };
        }

        if (isCrash) { // 작업시간에 대해서 오름차순
            temp.sort((a,b) => {
                if (a[1] < b[1]) return -1;
                if (a[1] > b[1]) return 1;
            });

            answer += curEndPoint - temp[0][0] + temp[0][1];
            curEndPoint += temp[0][1];
            visited[temp[0][2]] = true;
        }
        else {
            for (let j=1; j<jobs.length; j++) {
                if (visited[j]) continue;
    
                answer += jobs[j][1];
                curEndPoint = jobs[j][0] + jobs[j][1];
                visited[j] = true;
                break;
            }
        }
    }

    return Math.floor(answer/jobs.length);
}

console.log(solution([[24, 10], [18, 39], [34, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]])); // 74
console.log(solution([[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]])); // 72
console.log(solution([[0, 5], [1, 2], [5, 5]])); // 6