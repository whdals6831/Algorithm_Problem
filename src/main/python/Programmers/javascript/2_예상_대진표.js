function solution(n,a,b)
{
    var answer = 0;

    while (true) {
        var next_a = parseInt((a-1)/2)+1;
        var next_b = parseInt((b-1)/2)+1;

        answer++;
        
        if (next_a === next_b) {
            break;
        }

        a = next_a;
        b = next_b;
    }

    return answer;
}

// console.log(solution(8,4,7));