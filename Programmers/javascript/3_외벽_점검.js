let answer = 9999999;

function dfs(n, weak, dist, now, cnt) {
    if (weak.length === 0) {
        answer = Math.min(answer, cnt);
        return;
    }
    else if (dist.length === now) {
        if (weak.length > 0) {
            return;
        }
    }
    else if (cnt > answer) {
        return;
    }

    for (var i=0; i<weak.length; i++) {
        var clock = (weak[i] + dist[now]) % n;

        if (clock > weak[i]) { 
            var temp = [];
            for (var j of weak) {
                if (j > clock || j < weak[i]) {
                    temp.push(j);
                }
            }
            dfs(n, [...temp], dist, now+1, cnt+1);
        }
        else if (clock < weak[i]) { // n을 넘어갈때
            var temp = [];
            for (var j of weak) {
                if (j > clock && j < weak[i]) {
                    temp.push(j);
                }
            }
            dfs(n, [...temp], dist, now+1, cnt+1);
        }
    }
}

function solution(n, weak, dist) {
    dist.sort((a,b) => b-a);
    dfs(n, weak, dist, 0, 0);

    if (answer === 9999999) {
        answer = -1;
    }

    return answer;
}

console.log(solution(12,[1, 5, 6, 10],[1, 2, 3, 4]));