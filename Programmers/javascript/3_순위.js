function getHowManyPlayerWinOrLose(n, table, player) {
    let q = [];
    let visited = new Array(n+1).fill(false);
    let cnt = 0;
    
    q, visited = pushPlayer(q, table[player], visited);
    
    while (q.length > 0) {
        let nextPlayer = q.shift();
        cnt++;
        q, visited = pushPlayer(q, table[nextPlayer], visited);
    }
    
    return cnt;
}

function pushPlayer(q, table, visited) {
    for (let player of table) {
        if (visited[player]) {
            continue;
        }
        else {
            q.push(player);
            visited[player] = true;
        }
    }
    return q, visited;
}

function isPlayerRank(n, winTable, loseTable, player) {
    let winNum = getHowManyPlayerWinOrLose(n, winTable, player);
    let loseNum = getHowManyPlayerWinOrLose(n, loseTable, player);
    
    if (winNum+loseNum === n-1) {
        return true;
    }
    else {
        return false;
    }
}

function solution(n, results) {
    let answer = 0;
    let winTable = new Array(n+1).fill(0).map(() => []);
    let loseTable = new Array(n+1).fill(0).map(() => []);
    
    for (let result of results) {
        winTable[result[0]].push(result[1]);
        loseTable[result[1]].push(result[0]);
    }
    
    for (let i=1; i<n+1; i++) {
        if (isPlayerRank(n, winTable, loseTable, i)) {
            answer++;
        }   
    }
    
    return answer;
}