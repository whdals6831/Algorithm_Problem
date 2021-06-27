function isPass(n, pillar, paper) {
    for (let i=1; i<n+1; i++) {
        for (let j=0; j<n+1; j++) {
            if (pillar[i][j] === 1) {
                if (!(pillar[i][j-1] === 1 || paper[i][j] === 1 || paper[i-1][j] === 1)) {
                    return false;
                }
            }

            if (paper[i][j] === 1) {
                if (!(pillar[i][j-1] === 1 || pillar[i+1][j-1] === 1 || (paper[i-1][j] === 1 && paper[i+1][j] === 1))) {
                    return false;
                }
            }
        }
    }

    return true;
}

function solution(n, build_frame) {
    var answer = [[]];
    let pillar = Array.from(Array(n+1), () => Array(n+1).fill(0));
    let paper = Array.from(Array(n+1), () => Array(n+1).fill(0));

    let q = [];

    for (var [x,y,a,b] of build_frame) {
        if (a === 0) { // 기둥
            if (b === 1) { // 설치
                if (y === 0 || pillar[x][y-1] === 1 || paper[x-1][y] === 1) {
                    pillar[x][y] = 1;
                }
                continue;
            }
            else { // 삭제
                let copyPillar = [...pillar];
                copyPillar[x][y] = 0;

                if (isPass(n, copyPillar, paper)) {
                    pillar = copyPillar;
                }

                continue;
            }
        }
        else { // 보 
            if (b === 1) { // 설치
                if (pillar[x][y-1] === 1 || pillar[x+1][y-1] === 1 || (paper[x-1][y] === 1 && paper[x+1][y] === 1)) {
                    paper[x][y] = 1;
                }
                continue;
            }
            else { // 삭제
                let copyPaper = [...paper];
                copyPaper[x][y] = 0;

                if (isPass(n, pillar, copyPaper)) {
                    paper = copyPaper;
                }

                continue;
            }
        }
    }

    console.log(pillar);
    console.log(paper);
    
    return answer;
}

// console.log(solution(5,[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]));
console.log(solution(5,[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))