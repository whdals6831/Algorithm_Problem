function solution(record) {
    var answer = [];
    let db = {};

    // db에 유저 id에 대한 정보 저장
    for (var i of record) {
        var log = i.split(" ");

        if (log[0] === "Enter") {
            db[log[1]] = log[2];
        }

        if (log[0] === "Change") {
            db[log[1]] = log[2];
        }
    }

    // log 변환
    for (var i of record) {
        var log = i.split(" ");

        if (log[0] === "Enter") {
            answer.push(`${db[log[1]]}님이 들어왔습니다.`);
        }

        if (log[0] === "Leave") {
            answer.push(`${db[log[1]]}님이 나갔습니다.`);
        }
    }

    return answer;
}