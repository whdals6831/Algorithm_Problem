function solution(n, times) {
    times.sort((a,b) => a-b);
    let left = 1;
    // right는 현재 입국심사를 받는데 가장 오래 걸리는 시간이다.
    let right = times[times.length-1] * n;

    while(left <= right) {
        let mid = Math.floor((left+right)/2); // 제한시간
        let cnt = 0;
        
        for (var time of times) { 
            // 현재 주어진 제한시간안에 최대 몇명이 받을 수 있는지 계산
            cnt += Math.floor(mid/time);
        }

        if (cnt >=n) {
            right = mid-1;
        }
        else if (cnt < n) {
            left = mid+1;
        }
    }

    return left;
}

console.log(solution(6,[7,10]));