function solution(arr1, arr2) {
    arr1.map((row, i) => {
        for (let j=0; j<row.length; j++) {
            row[j] += arr2[i][j];
        }
        return row;
    })
    return arr1;
}