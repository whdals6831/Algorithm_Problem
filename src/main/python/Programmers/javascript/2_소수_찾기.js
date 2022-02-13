let set = new Set();

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

function bruteForce(num, visit, cnt, str) { // 만들 수 있는 숫자의 모든 경우의 수
    if (cnt == num.length) {
        return;
    }

    for (var i=0; i<num.length; i++) {
        if (visit[i] == 0) {
            var next = str + num[i];
            var nextVisit = [...visit]; // deep copy
            nextVisit[i] = 1;
            set.add(parseInt(next));
            bruteForce(num, nextVisit, cnt+1, next);
        }
    }
}

function solution(numbers) {
    var answer = 0;
    let primeNum = primeNumber();
    let visit = new Array(numbers.length).fill(0);

    bruteForce(numbers, visit, 0, '');

    for (var i of set) {
        if (primeNum[i] == 1) {
            answer++;
        }
    }

    return answer;
}