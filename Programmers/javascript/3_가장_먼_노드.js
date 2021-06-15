function bfs(n, graph) {
    let q = [];
    let moveLog = [];
    let visited = new Array(n+1).fill(false);
    let maxVertex = 0;
    let result = 0;

    q.push([1, 0]);
    visited[1] = true;
    moveLog.push([1,0]);

    while(q.length > 0) {
        var now = q.shift();
        
        for (var i of graph[now[0]]) {
            if (!visited[i]) {
                q.push([i, now[1]+1]);
                visited[i] = true;
                
                if (maxVertex < now[1]+1) {
                    maxVertex = now[1]+1;
                }
                moveLog.push([i, now[1]+1]);
            }
        }
    }

    for (var v of moveLog) {
        if (v[1] === maxVertex) {
            result++;
        }
    }

    return result;
}

function solution(n, edge) {
    const graph = Array(n+1).fill(0).map(() => []);
    // let graph = Array.from(Array(n+1), () => Array(n+1).fill(0)); 이와같은 자료구조는 메모리 용량의 부족인건지 signal: aborted (core dumped)에러가 난다.

    for (var e of edge) {
        graph[e[0]].push(e[1]);
        graph[e[1]].push(e[0]);
    }

    return bfs(n, graph);
}

console.log(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]));