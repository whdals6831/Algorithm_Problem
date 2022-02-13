function solution(numbers) {
    var answer = '';

    numbers.sort((a,b) => {
        var x = Number(String(a)+String(b));
        var y = Number(String(b)+String(a));

        if (x < y) return 1; // return 값이 1 이면 x와 y를 바꾼다! 여기서는 내림차순
        if (x > y) return -1;

        return 0;
    })

    if (numbers.every(v => v === 0)) {
        answer = "0";
    }
    else {
        answer = numbers.join("");
    }
    
    // console.log(answer);

    return answer;
}

// solution([10, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
// solution([412, 41]);
// solution([403,40]);
// solution([21,212]);
// solution([90,908,89,898,10,101,1,8,9]);