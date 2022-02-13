let count = 100;

function dfs(begin, target, words, visited, cnt) {
    if (cnt > count) {
        return;
    }

    if (begin === target) {
        count = Math.min(count, cnt);
        return;
    }

    for (var i=0; i<words.length; i++) {
        var notCollectCnt = 0;
        var v = [...visited];

        if (!v[i]) {
            for (var j=0; j<begin.length; j++) {
                if (notCollectCnt > 1) {
                    break;
                }
    
                if (begin[j] != words[i][j]) {
                    notCollectCnt++;
                }
            }
        }

        if (notCollectCnt === 1) {
            v[i] = true;
            dfs(words[i], target, words, v, cnt+1);
        }
    }
}

function solution(begin, target, words) {
    var visited = new Array(words.length).fill(false);

    if (!words.includes(target)) {
        return 0;
    }

    dfs(begin, target, words, visited, 0);

    return count;
}

console.log(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]));