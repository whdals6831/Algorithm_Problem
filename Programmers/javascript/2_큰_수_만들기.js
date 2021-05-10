function solution(number, k) {
    var answer = [];

    numList = number.split("").map(x => Number(x));
    
    var start = 0;

    for (var i=1; i<=k; i++) {
        if (number[i] > number[start]) {
            start = i;
        }
    }

    answer.push(number[start]);
    start++;

    while (answer.length < number.length-k) {
        if (answer[answer.length-1] < number[start]) {
            
        } 
    }

    console.log(start);


    return answer;
}

solution("1924",2);
solution("1231234",3);
solution("4177252841",4);