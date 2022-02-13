function solution(numbers, hand) {
    let answer = '';
    let nowL = [3,0];
    let nowR = [3,2];
    let nPoint = {
        1: [0,0],
        2: [0,1],
        3: [0,2],
        4: [1,0],
        5: [1,1],
        6: [1,2],
        7: [2,0],
        8: [2,1],
        9: [2,2],
        0: [3,1]
    }

    for (let n of numbers) {
        switch (n) {
            case 1:
            case 4:
            case 7:
                answer += 'L';
                nowL = nPoint[n];
                break;
            case 3:
            case 6:
            case 9:
                answer += 'R';
                nowR = nPoint[n];
                break;
            case 2:
            case 5:
            case 8:
            case 0:
                let touchPoint = nPoint[n];
                let xL = Math.abs(touchPoint[0]-nowL[0]);
                let yL = Math.abs(touchPoint[1]-nowL[1]);
                let xR = Math.abs(touchPoint[0]-nowR[0]);
                let yR = Math.abs(touchPoint[1]-nowR[1]);

                if (xL+yL < xR+yR) {
                    nowL = touchPoint;
                    answer += 'L';
                    break;
                }
                else if (xL+yL > xR+yR) {
                    nowR = touchPoint;
                    answer += 'R';
                    break;
                }
                else {
                    if (hand === 'right') {
                        nowR = touchPoint;
                        answer += 'R';
                        break;
                    }
                    else {
                        nowL = touchPoint;
                        answer += 'L';
                        break;
                    }
                }
        }
    }
    
    return answer;
}

console.log(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right'));
console.log(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], 'left'));
console.log(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 'right'));