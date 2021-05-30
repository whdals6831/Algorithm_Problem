function solution(info, query) {
    const answer = [];
    const infoMap = {};

    // '-backend-pizza', 'java-seniorpizza' 같은 key로 만들 수 있는 모든 조합 구하기
    function combination(arr, score, start) {
        var key = arr.join("");
        var value = infoMap[key];

        if (value) {
            infoMap[key].push(score);
        }
        else {
            infoMap[key] = [score];
        }

        for (var i = start; i<arr.length; i++) {
            var temp = [...arr];
            temp[i] = "-"
            combination(temp, score, i+1);
        }
    }

    // 이진 탐색
    function binarySearch(arr, score) {
        if (arr) {
            var start = 0;
            var end = arr.length;

            while (start < end) {
                var mid = Math.floor((start+end)/2);
                
                if (arr[mid] < score) {
                    start = mid+1;
                }
                else {
                    end = mid
                }
            }

            return arr.length - start;
        }
        else {
            return 0;
        }
    }

    for (var i of info) {
        var infoArr = i.split(" ");
        var score = Number(infoArr.pop());
        combination(infoArr, score, 0);
    }

    for (var key in infoMap) {
        infoMap[key] = infoMap[key].sort((a, b) => a - b);
    }

    for (var q of query) {
        var queryArr = q.replace(/ and/g, "").split(" ");
        var score = Number(queryArr.pop());
        var key = queryArr.join("");
        var findArr = infoMap[key];

        answer.push(binarySearch(findArr, score));

    }
    
    return answer;
}

console.log(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]));