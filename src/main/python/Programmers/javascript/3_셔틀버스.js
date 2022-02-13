function makeTimeForm(n) {
    var hour = parseInt(n / 60);
    var minute = n % 60;

    if (hour < 10) {
        hour = "0" + hour;
    }

    if (minute < 10) {
        minute = "0" + minute;
    }

    return `${hour}:${minute}`;
}

function solution(n, t, m, timetable) {
    let busSchedule = new Map();
    let beforeBusTime = 540;

    // 버스운행표 만들기
    for (var i=0; i<n; i++) {
        busSchedule.set(beforeBusTime, []);
        beforeBusTime += t;
    }  

    // timetable 시 -> 분으로 바꾸기
    timetable = timetable.map(time => {
        var hour = Number(time.substring(0,2))*60;
        var minute = Number(time.substring(3,5));
        
        return hour+minute;
    });

    timetable.sort((a,b) => a-b);

    // 각 크루들이 어떤 버스에 타게되는지 기입
    for (var time of timetable) {
        for (var busStop of busSchedule.keys()) {
            if (busSchedule.get(busStop).length < m && busStop >= time) {
                busSchedule.get(busStop).push(time);
                break;
            }
        }  
    }

    let order = Array.from(busSchedule.keys()).sort((a,b) => b-a)

    // 제일 늦은 버스를 기준으로 얼마까지 늦게 탈 수 있는지 체크
    let crewList = busSchedule.get(order[0])

    if (crewList.length < m) { // 자리가 있으면 승차
        return makeTimeForm(order[0]);
    }
    else { // 없으면 제일 늦게온 크루를 기준으로 -1분
        var max = 9999999;

        for (var j=crewList.length-1; j>=0; j--) {
            if (j === crewList.length-1) {
                max = crewList[j];
            }
            else {
                if (max > crewList[j]) {
                    return makeTimeForm(max-1);
                }
            }
        }
        return makeTimeForm(max-1);
    }
}

console.log(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))
console.log(solution(10, 60, 45, ["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]))