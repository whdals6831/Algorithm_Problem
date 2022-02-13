function move(cmd, now) {
    let [x, y] = now;

    if (cmd === "U") {
        y += 1;
    }

    if (cmd === "D") {
        y -= 1;
    }

    if (cmd === "L") {
        x -= 1;
    }

    if (cmd === "R") {
        x += 1;
    }

    return [x, y]
}

function solution(dirs) {
    var answer = 0;
    let now = [0, 0];
    let visited = Array.from(Array(30), () => Array(30).fill(false));

    for (var cmd of dirs) {
        var vX = now[0];
        var vY = now[1];
        var [x, y] = move(cmd, now);

        // 경계를 넘어가면 무시
        if (x < -5 || x > 5 || y < -5 || y > 5) {
            continue;
        }

        // 지나간 길인지 판별
        if (!visited[x+vX+10][y+vY+10]) {
            visited[x+vX+10][y+vY+10] = true;
            answer++;
        }
        
        now = [x, y];
    }

    return answer;
}

console.log(solution("ULURRDLLU"));
console.log(solution("LULLLLLLU"));