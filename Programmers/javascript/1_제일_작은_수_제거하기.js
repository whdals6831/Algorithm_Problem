function solution(arr) {
    let minIndex = 0;
    let minValue = 999999999;

    for (let i=0; i<arr.length; i++) {
        if (minValue > arr[i]) {
            minValue = arr[i];
            minIndex = i;
        }
    }

    arr.splice(minIndex, 1);

    if (arr.length < 1) {
        return [-1];
    }

    return arr;
}