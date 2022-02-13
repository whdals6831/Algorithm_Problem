function solution(n) {
    let root = Math.sqrt(n);

    if (Number.isInteger(root)) {
        return (root+1)*(root+1);
    }
    else {
        return -1;
    }
}