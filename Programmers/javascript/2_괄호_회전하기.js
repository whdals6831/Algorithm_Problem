function check(s) {
    var stack = [];

    for (var i=0; i<s.length; i++) {
        if (s[i] === '(' || s[i] === '[' || s[i] === '{') {
            stack.push(s[i]);
        }

        if (s[i] === ')') {
            if (stack.pop() !== '(') {
                return false;
            }
        }

        if (s[i] === ']') {
            if (stack.pop() !== '[') {
                return false;
            }
        }

        if (s[i] === '}') {
            if (stack.pop() !== '{') {
                return false;
            }
        }
    }

    if (stack.length === 0) {
        return true;
    }
    else {
        return false;
    }
}

function solution(s) {
    var answer = 0;

    for (var i=0; i<s.length; i++) {
        if (check(s)) {
            answer++;
        }
        
        s = s.slice(1,s.length) + s[0];
    }

    return answer;
}