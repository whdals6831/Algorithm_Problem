function worksScore(n, works) {
    let answer = 0;
    let cur = 1;

    while (n > 0) {
        if (cur < works.length) {
            if (works[cur-1] > works[cur]) {
                for (var i=0; i<cur; i++) {
                    works[i] -= 1;
                    n--;

                    if (n === 0) break;
                }
            }
            else if(works[cur-1] === works[cur]) {
                for (var i=0; i<=cur; i++) {
                    if (works[i] === 0) continue;
                    
                    works[i] -= 1;
                    n--;

                    if (n === 0) break;
                }
                cur++;
            }
            else {
                works[cur] -= 1;
                cur++;
                n--;
            }
        }
        else {
            if (works[cur-1] === 0) {
                return 0;
            }
            else {
                works[cur-1] -= 1;
                n--;
            }
        }
    }

    for (var work of works) {
        answer += work*work;
    }

    return answer;
}

function solution(n, works) {
    works = works.sort((a,b) => b-a);
  
    return worksScore(n, works);
}

console.log(solution(4, [4, 3, 3]));
console.log(solution(1, [5,1,1]));
console.log(solution(99, [2, 15, 22, 55, 55])); //580
console.log(solution(10, [1,2,3,2,3,2,3]));
