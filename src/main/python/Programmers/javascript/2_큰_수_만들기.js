function solution(number, k) {
    let answer = '';
    let arr = [];
    let n = 0;

    for (var i=0; i<number.length; i++) {
        while (arr.length != 0) {
            if (n == k) break; // 제거할 수가 채워지면 종료

            if(arr[arr.length-1] < number[i]) {
                n++;
                arr.pop();
            }
            else break;
        }

        arr.push(number[i]);
    }

    answer = arr.join("").substr(0, number.length-k);
    return answer;
}