function solution(n, computers) {
    var answer = 0;
    var q = [];
    var visited = new Array(n).fill(0);

    for (var i=0; i<n; i++) {
        if (visited[i] == 0) {
            q.push(i);
            visited[i] = 1;
            answer++;

            while (q.length > 0) {
                var now = q.shift();

                for (var next=0; next<n; next++) {
                    if (visited[next] == 0 && computers[now][next] == 1) {
                        q.push(next);
                        visited[next] = 1;
                    }
                }
            }
        }
    }
    
    return answer;
}