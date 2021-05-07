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
    let bidList = banned_id.map((bid) => {
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
        console.log(level, curSet);
        if (level === banned_id.length) {
            let str = curSet.sort().join("");
            s.add(str);
            return;
        }

        for(var bid of bidList[level]) {
            if (curSet.includes(bid)) {
                continue;
            }
            curSet.push(bid);
            dfs(level+1);
            curSet.splice(curSet.indexOf(bid),1);
        }
        return;
    }
    dfs(0);

    return s.size;
}

solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "*rodo", "******", "******"]);