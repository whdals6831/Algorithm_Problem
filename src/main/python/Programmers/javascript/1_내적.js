function solution(a, b) {
    return a.reduce(((acc, curVal, curIdx) => acc + curVal * b[curIdx]), 0);
}