function solution(maps) {
    var answer = 0;
    let n = maps.length;
    let m = maps[0].length;
    let wall = [new Array(m).fill(0)];
    let extendMap = [...wall, ...maps, ...wall];
    let visit = [];
    const dx = [1,0,-1,0];
    const dy = [0,1,0,-1];

    extendMap = extendMap.map(arr => [0,...arr,0]);

    for (var i=0; i<extendMap.length; i++) {
        visit.push(new Array(extendMap[0].length).fill(0));
    }


    let q = [];
    q.push([1,1]);

    while (q.length > 0) {
        var [x, y] = q.shift();

        for (var i=0; i<4; i++) {
            var nextX = x+dx[i];
            var nextY = y+dy[i];
            if (extendMap[nextX][nextY] !== 0 && visit[nextX][nextY] === 0) {
                extendMap[nextX][nextY] = extendMap[x][y] + 1;
                visit[nextX][nextY] = 1;
                q.push([nextX, nextY]);
            }
        }
    }

    if (visit[n][m] === 0) {
        answer = -1;
    }
    else {
        answer = extendMap[n][m];
    }

    return answer;
}

// console.log(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]));