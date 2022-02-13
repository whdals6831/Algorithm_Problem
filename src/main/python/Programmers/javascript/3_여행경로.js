let answer = []

function cloneObject(obj) {
    var clone = {};
    for(var i in obj) {
        clone[i] = obj[i];
    }
    return clone;
}

function dfs(n, tourList, airport, root) {
    // 탈출 조건
    if (n == 0) {
        if (answer.length == 0) {
            answer = root.split(" ");
        }
        return;
    }

    // dfs를 위한 deepcopy
    var cloneList = cloneObject(tourList);

    if (!tourList[airport]) { // 방문할 공항이 리스트에 없는경우
        return;
    }
    
    for (var next of tourList[airport]) {
        // console.log(n,cloneList);
        var idx = cloneList[airport].indexOf(next);
        cloneList[airport].splice(idx, 1); // 방문할 곳 제거
        dfs(n-1, cloneList, next, root + ` ${next}`);
        cloneList[airport].splice(idx, 0, next); // 다시 넣어주기 -> 백트래킹
    }
    return;
}

function solution(tickets) {
    var tourList = {};

    // 각 공항에서 갈수있는 경로 설정
    for (var [a, b] of tickets) {
        if (tourList[a]) {
            tourList[a].push(b);
        } else {
            tourList[a] = [b];
        }
    }

    // 알파벳 순서가 앞서는 경로를 return하기 위해 정렬
    for (var key in tourList) {
        tourList[key].sort();
    }
    
    dfs(tickets.length, tourList, "ICN", "ICN");

    return answer;
}

// solution([["ICN", "SFO"], ["SFO", "ICN"], ["ICN", "SFO"], ["SFO", "QRE"]]);