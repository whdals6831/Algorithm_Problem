function solution(arr1, arr2) {
    let answer = [];

    for (let arr of arr1) {
        let temp = [];

        for (let i=0; i<arr2[0].length; i++) {
            let total = 0;
    
            for (let j=0; j<arr.length; j++) {
                total += arr[j]*arr2[j][i];
            }
            
            temp.push(total);
        }
        answer.push(temp);
    }
    
    return answer;
}