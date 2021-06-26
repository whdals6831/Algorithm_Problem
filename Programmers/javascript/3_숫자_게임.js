function solution(A, B) {
    let answer = 0;
    let curA = 0;
    let curB = 0;

    A.sort((a,b) => a-b);
    B.sort((a,b) => a-b);

    while (curB < B.length) {
        if (A[curA] < B[curB]) {
            curA++;
            curB++;
            answer++;
        }
        else {
            curB++;
        }
    }

    return answer;
}

console.log(solution([5,1,3,7],[2,2,6,8]));
console.log(solution([2,2,2,2],[1,1,1,1]));