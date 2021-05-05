function solution(s)
{
    var answer = 0;

    while (s.length > 0) {
        var before = '';
        var temp = [];
        var before_len = s.length;

        for (var i=0; i<s.length; i++) {
            if (before === s[i]) {
                temp.pop();
                before = temp[temp.length-1];
            }
            else {
                temp.push(s[i]);
                before = s[i];
            }
        }

        s = temp.join('');

        if (before_len === s.length) {
            break
        }
    }

    if (s.length == 0) {
        answer = 1;
    }

    return answer;
}