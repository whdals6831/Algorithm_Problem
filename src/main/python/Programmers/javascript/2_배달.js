function dijkstra(N, village) {
    let visited = new Array(N+1).fill(false);
    let find = new Array(N+1).fill(500001);
    let q = [];
    
    find[1] = 0;
    visited[0] = true;
    visited[1] = true;
    q.push(1);

    while (q.length > 0) {
        var now = q.shift();

        for (var i=1; i<N+1; i++) {
            if (village[now][i] != 500001) {
                find[i] = Math.min(find[i], find[now] + village[now][i]);
            }
        }

        // 이미 방문한 곳은 q에 집어넣을 수 없게 변형
        var temp = find.map( (value, idx) => {
            if (visited[idx]) {
                value = 500001;
            }
            return value
        })

        // find에서 방문하지 않고 가장 작은 값을 가진 곳을 다음 방문할 장소로 지정
        var next = temp.indexOf(Math.min(...temp));

        // 다음 방문할 곳의 index가 0이면 모든곳을 다 방문한것임
        if (next != 0) {
            q.push(next);
            visited[next] = true;
        }
    }

    return find;
}

function solution(N, road, K) {
    var answer = 0;
    let village = Array.from(Array(N+1), () => Array(N+1).fill(500001));

    for (var [a,b,c] of road) {
        c = Math.min(village[a][b], c);
        village[a][b] = c;
        village[b][a] = c;
    }

    let arr = dijkstra(N, village);

    for (var distance of arr) {
        if (distance <= K) {
            answer ++;
        }
    }

    return answer;
}

console.log(solution(6,[[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]],4));