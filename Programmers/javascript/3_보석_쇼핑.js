function solution(gems) {
    let answer = [0, 100001];
    let uniqueGems = Array.from(new Set(gems));
    let gemMap = new Map();
    let left = 0;

    for (let i=0; i<gems.length; i++) {
        if (gemMap.has(gems[i])) {
            gemMap.set(gems[i], gemMap.get(gems[i])+1);
        }
        else {
            gemMap.set(gems[i], 1);
        }

        if (answer[1] !== 100001) { // 슬라이딩 윈도우
            if (gemMap.get(gems[left])-1 === 0) {
                gemMap.delete(gems[left]);
            }
            else {
                gemMap.set(gems[left], gemMap.get(gems[left])-1);
            }
            left++;
        }

        while (gemMap.size === uniqueGems.length) {
            if (i-left < answer[1]-answer[0]) {
                answer = [left+1, i+1];
            }

            if (gemMap.get(gems[left])-1 === 0) {
                gemMap.delete(gems[left]);
            }
            else {
                gemMap.set(gems[left], gemMap.get(gems[left])-1);
            }
            left++;
        }
    }

    return answer;
}

console.log(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]));