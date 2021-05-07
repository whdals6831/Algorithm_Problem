function check(uid, bid) {
    if (uid.length !== bid.length) {
        return false;
    }

    for (var i=0; i<uid.length; i++) {
        if (bid[i] === "*") {
            continue;
        }
        if (uid[i] !== bid[i]) {
            return false;
        }
    }
    return true;
}

function solution(user_id, banned_id) {
    let bidList = banned_id.map((bid) => { // 각 bid마다 검사
        let temp = [];
        for (var uid of user_id) {
            if(check(uid, bid)) {
                temp.push(uid);
            }
        }
        return temp;
    });

    console.log(bidList);

    let s = new Set();
    let curSet = [];

    function dfs(level) {
        if (level === banned_id.length) {
            let str = curSet.sort().join("");
            s.add(str);
            return;
        }
        
        // 모든 경우의 수를 다 탐색
        for(var bid of bidList[level]) {
            if (curSet.includes(bid)) {
                continue;
            }
            curSet.push(bid);
            // console.log(level, curSet, bid);
            dfs(level+1);
            curSet.splice(curSet.indexOf(bid),1); // 정렬이 되기 때문에 index를 찾아 삭제 -> 백트래킹
            // console.log("Back",level, curSet, bid);
        }
        return;
    }
    dfs(0);

    return s.size;
}

// solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "*rodo", "******", "******"]);