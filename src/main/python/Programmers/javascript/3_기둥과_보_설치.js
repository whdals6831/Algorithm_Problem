function checkPillar(n, pillar, paper, x, y) {
    if (y === 0 || pillar[x][y-1] === 1) return true;
    if ((x > 0 && paper[x-1][y] === 1) || paper[x][y] === 1) return true;
    return false;
}

function checkPaper(n, pillar, paper, x, y) {
    if (pillar[x][y-1] === 1 || pillar[x+1][y-1] === 1) return true; 
    if ((x > 0 && paper[x-1][y] === 1) && paper[x+1][y] === 1) return true;
    return false;
}

function checkDelete(n, pillar, paper) {
    for (let y=0; y<n+1; y++) {
        for (let x=0; x<n+1; x++) {
            if (pillar[x][y] === 1) {
                if (!checkPillar(n, pillar, paper, x, y)) return false;
            }

            if (paper[x][y] === 1) {
                if (!checkPaper(n, pillar, paper, x, y)) return false;
            }
        }
    }

    return true;
}

function solution(n, build_frame) {
    let answer = [];
    let pillar = Array.from(Array(n+1), () => Array(n+1).fill(0));
    let paper = Array.from(Array(n+1), () => Array(n+1).fill(0));

    for (var [x,y,a,b] of build_frame) {
        if (a === 0) { // 기둥
            if (b === 1) { // 설치
                if (checkPillar(n, pillar, paper, x, y)) {
                    pillar[x][y] = 1;
                }
            }
            else { // 삭제
                pillar[x][y] = 0;

                if (!checkDelete(n, pillar, paper, x, y)) {
                    pillar[x][y] = 1;
                }
            }
        }
        else { // 보 
            if (b === 1) { // 설치
                if (checkPaper(n, pillar, paper, x, y)) {
                    paper[x][y] = 1;
                }
            }
            else { // 삭제
                paper[x][y] = 0;

                if (!checkDelete(n, pillar, paper, x, y)) {
                    paper[x][y] = 1;
                }
            }
        }
    }

    for (let x=0; x<n+1; x++) {
        for (let y=0; y<n+1; y++) {
            if (pillar[x][y] === 1) {
                answer.push([x,y,0]);
            }

            if (paper[x][y] === 1) {
                answer.push([x,y,1]);
            }
        }
    }
    
    return answer;
}

console.log(solution(5,[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]));
console.log(solution(5,[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))