function find(N, bridge) {
    let visited = new Array(N).fill(false);
    let q = [];
    let result = 0;
    let cnt = N;

    q.push([0,0]);

    while (cnt > 0) {
        var now = q.shift();

        if (visited[now[0]]) {
            continue;
        }
        
        visited[now[0]] = true;
        result += now[1];
        cnt--;

        for (var i=0; i<N; i++) {
            if (!visited[i] && bridge[now[0]][i] != -1) {
                q.push([i,bridge[now[0]][i]]);
            }
        }
        q.sort((a,b) => a[1]-b[1]);
    }

    return result;
}

function solution(n, costs) {
    let bridge = Array.from(Array(n), () => Array(n).fill(-1))

    for (var cost of costs) {
        bridge[cost[0]][cost[1]] = cost[2];
        bridge[cost[1]][cost[0]] = cost[2];
    }

    return find(n, bridge);
}

console.log(solution(4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]));