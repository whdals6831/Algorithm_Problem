function solution(brown, yellow) {
    var answer = [];

    for (var i=1; i<brown/2; i++) {
        if ((brown+yellow)%i === 0) {
            for (var j=1; j<brown/2; j++) {
                if ((brown+yellow)%j === 0) {
                    var bCheck = 2*i + 2*j - 4;
                    var yCheck = i*j - brown;

                    if (bCheck === brown && yCheck === yellow) {
                        answer.push(Math.max(i,j));
                        answer.push(Math.min(i,j));
                        return answer;
                    }
                }
            }
        }
    }
}

console.log(solution(10,2));
console.log(solution(8,1));
console.log(solution(24,24));