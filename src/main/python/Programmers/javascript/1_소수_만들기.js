let answer = 0;

function primeNumber() {
    let n = 10000000;
    let arr = new Array(n).fill(1);

    arr[0] = 0;
    arr[1] = 0;

    for (var i=2; i<parseInt(Math.sqrt(n)); i++) { // 에라토스테네스의 체
        if (arr[i] == 1) {
            for (var j=i+i; j<n; j=j+i) {
                arr[j] = 0
            }
        }
    }

    return arr;
}

function findPrime(nums, primeArr, nowIdx, cnt, result) {
    if (cnt === 3) {
        if (primeArr[result] === 1) {
            answer++;
        }
        return;
    }

    for (let i=nowIdx; i<nums.length; i++) {
        findPrime(nums, primeArr, i+1, cnt+1, result+nums[i]);
    }
}

function solution(nums) {
    let primeArr = primeNumber();
    findPrime(nums, primeArr, 0, 0, 0);

    return answer;
}