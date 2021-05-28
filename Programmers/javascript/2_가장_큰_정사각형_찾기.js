function solution(board)
{
    var answer = 0;
    const y = board[0].length;
    let arr = new Array(y).fill(0);

    for (var row of board) {
        for (var i=0; i<y; i++) {
            if (row[i] === 0) {
                arr[i] = 0;
            }
            else {
                arr[i] += 1;
            }
        }

        for (var j=0; j<y; j++) {
            if (arr[j] >= answer+1) {
                var flag = false;
                
                // 현재 answer보다 크기가 1 큰 정사각형이 만들어 질 수 있는지 체크
                for (var k=j+1; k<j+answer+1; k++) {
                    if (j+answer+1 > y || arr[k] < answer+1) {
                        flag = true;
                        break;
                    }
                }

                if (!flag) {
                    answer++;
                }
            }
        }
    }

    return answer*answer;
}

console.log(solution([[1, 0, 0, 1, 0], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]));