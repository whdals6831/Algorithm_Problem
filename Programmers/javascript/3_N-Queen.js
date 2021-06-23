let board = new Array(13);
let answer = 0;

function dfs(y, n) { // y는 현재 몇개의 퀸이 배치되었는지
    var flag;

    if (y === n) {
        answer++;
        return;
    } 

    for (var i=0; i<n; i++) { // row에 column의 위치
        flag = true;
        for (var j=0; j<y; j++) { // 현재 배치된 퀸의 위치 확인 후 판별 board[j] = k는 j행에 k번째 열에 퀸이 있다는 소리
            if (board[j] === i || Math.abs(y-j) === Math.abs(i-board[j])) { // 직선, 대각선(각 퀸의 높이 거리하고 너비 거리가 같으면 대각선에 위치한것임) 체크
                flag = false;
                break;
            }
        }
        if (flag) {
            board[y] = i;
            dfs(y+1, n);
        }
    }
}

function solution(n) {
    dfs(0, n); 

    return answer;
}

console.log(solution(12));