function solution(cacheSize, cities) {
    let answer = 0;
    let cache = new Array(cacheSize);

    for (let citie of cities) {
        citie = citie.toLowerCase();

        if (cacheSize === 0) {
            answer += 5;
            continue;
        }

        if (cache.includes(citie)) {
            let idx = cache.indexOf(citie);
            cache.splice(idx, 1);
            answer += 1;
        }
        else {
            cache.shift();
            answer += 5;
        }

        cache.push(citie);
    }

    return answer;
}

console.log(solution(5,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]));