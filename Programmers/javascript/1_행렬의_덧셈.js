function solution(arr1, arr2) {
    arr1 = arr1.map((row, i) => {
        return row.map((value, j) => {
            value += arr2[i][j];
            return value;
        })
    })

    return arr1;
}