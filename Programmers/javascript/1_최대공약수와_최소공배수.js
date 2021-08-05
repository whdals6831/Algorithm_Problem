// GCD는 최대공약수 -> 유클리드 호제법 사용
// GCM은 최소공배수

function GCD(a, b){ // a >= b
    return b ? GCD(b, a % b) : a ;
}

function GCM(a, b) {
    return (a * b) / GCD(a, b);
}

function solution(n, m) {
    let answer = [];

    answer.push(GCD(n, m));
    answer.push(GCM(n, m));

    return answer;
}