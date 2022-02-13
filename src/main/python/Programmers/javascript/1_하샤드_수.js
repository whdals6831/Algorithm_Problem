function solution(x) {
    let total = 0;

    for (let n of String(x)) {
        total += Number(n);
    }

    if (x%total === 0) {
        return true;
    }
    else {
        return false;
    }
}