function isKeepDistance(place, i, j) {
    let dx = [0,1,0,-1];
    let dy = [1,0,-1,0];
    let diagonal_X = [1,1,-1,-1];
    let diagonal_Y = [1,-1,-1,1];

    for (let v=0; v<4; v++) { // 동서남북 검사
        if (place[i+dx[v]][j+dy[v]] === "P" || (place[i+dx[v]][j+dy[v]] === "O" && place[i+dx[v]*2][j+dy[v]*2] === "P")) {
            return 0;
        }
    }

    for (let v=0; v<4; v++) { // 대각선 검사
        if (place[i+diagonal_X[v]][j+diagonal_Y[v]] === "P") {
            if (place[i+dx[v]][j+dy[v]] !== "X" && place[i+(dx[v]%4)][j+(dy[v]%4)] !== "X") {
                return 0;
            }
        }
    }

    return 1;
}

function solution(places) {
    let answer = [];
    places = places.map(place => ["XXXXXXX", ...place.map(row => `X${row}X`), "XXXXXXX"]); // 계산을 편하게 하기 위한 빈 벽생성

    for (let place of places) {
        let flag = true;

        for (let i=1; i<=5; i++) {
            if (flag) {
                for (let j=1; j<=5; j++) {
                    if (place[i][j] === "P") {
                        if (!isKeepDistance(place, i, j)) {
                            flag = false;
                            answer.push(0);
                            break;
                        };
                    }
                }
            }
            else {
                break;
            }
        }

        if (flag) {
            answer.push(1);
        }
    }

    return answer;
}

console.log(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]));