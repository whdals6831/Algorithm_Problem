function findTwobyTwoBlock(m, n, board) {
    let removeBlockIdx = Array.from(Array(m+2), () => Array(n+2).fill(false));
    
    // 동일한 형태의 2x2 찾기
    for (var i=1; i<=m; i++) {
        for (var j=1; j<=n; j++) {
            var shape = board[i][j];

            if (shape === 0) {
                continue;
            }

            if (
                board[i][j+1] != 0 &&
                board[i][j+1] === shape &&
                board[i+1][j] != 0 &&
                board[i+1][j] === shape &&
                board[i+1][j+1] != 0 &&
                board[i+1][j+1] === shape
            ) {
                removeBlockIdx[i][j] = true;
                removeBlockIdx[i][j+1] = true;
                removeBlockIdx[i+1][j] = true;
                removeBlockIdx[i+1][j+1] = true;
            }
        }
    }

    return removeBlockIdx;
}

function newTwoByTwoBlock(m, n, board, removeBlockIdx) {
    let newBoard = Array.from(Array(m+2), () => Array(n+2).fill(0));

    // 2x2블록 제거하기
    for (var j=1; j<=n; j++) {
        var temp = [];

        for (var i=m; i>0; i--) {
            if (!removeBlockIdx[i][j]) {
                temp.push(board[i][j]);
            }
        }

        // 남은 블록 내리기
        var tempLen = temp.length;

        for (var i=m; i>m-tempLen; i--) {
            newBoard[i][j] = temp.shift();
        }
    }

    return newBoard;
}

function solution(m, n, board) {
    var answer = 0;

    // 벽 만들어 놓기
    const wall = new Array(n+2).fill(0);
    for (var i=0; i<m; i++) {
        board[i] = [0, ...board[i], 0];
    }
    board = [[...wall], ...board, [...wall]];

    let removeBlockIdx = findTwobyTwoBlock(m, n, board);
    board = newTwoByTwoBlock(m, n, board, removeBlockIdx);

    const checkTwoByTwo = (row) => row.every((block) => block === false) === true;

    while (!removeBlockIdx.every(checkTwoByTwo)) {
        removeBlockIdx = findTwobyTwoBlock(m, n, board);
        board = newTwoByTwoBlock(m, n, board, removeBlockIdx);
    }

    for (var i=1; i<=m; i++) {
        for (var j=1; j<=n; j++) {
            if (board[i][j] === 0) {
                answer++;
            }
        }
    }

    return answer;
}

console.log(solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]));