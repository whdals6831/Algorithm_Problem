let a = [];
const ops = ['*', '-', '+'];

function calc(a, b, op) {
    a = parseInt(a);
    b = parseInt(b);

    switch (op) {
        case '+':
            return a + b;
        case '-':
            return a - b;
        case '*':
            return a * b;
    }
}

function dfs(arr,i) {
    if (arr.length === 1) {
        a.push(Math.abs(arr[0]));
        return ;
    }

    for (var op of ops) {
        var temp = [];

        for (var i=0; i<arr.length; i++) {
            if (arr[i] === op) {
                temp[temp.length-1] = calc(temp[temp.length-1], arr[i+1], op);
                i++;
            }
            else {
                temp.push(arr[i]);
            }
        }
        
        if (temp.length !== arr.length) {
            dfs([...temp],i+1);
        }
    }
}

function solution(expression) {
    var answer = 0;

    // ()를 포함하는 정규표현식일 경우, 포획된 결과도 배열에 포함됩니다.
    let arr = expression.split(/([*+-])/); 

    dfs(arr,0);
    answer = Math.max(...a);

    return answer;
}

// solution("100-200*300-500+20");