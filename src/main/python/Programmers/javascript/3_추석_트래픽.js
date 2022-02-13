function sort_process(processTime) {
    processTime.sort((a,b) => {
        if (a[0] > b[0]) {
            return 1; // b를 a보다 낮은 색으로 정렬
        }
        if (a[0] < b[0]) {
            return -1; // a를 b보다 낮은 색인으로 정렬
        }
        if (a[1] > b[1]) {
            return 1;
        }
        if (a[1] < b[1]) {
            return -1;
        }
        return 0; // 변경하지 않음
    });

    return processTime;
}

function solution(lines) {
    var answer = 1;
    let processTime_f = [];
    let processTime_b = [];

    for (var i of lines) {
        var h = Number(i.substr(11,2));
        var m = Number(i.substr(14,2));
        var s = Number(i.substr(17,6));
        var t = Number(i.substring(24,i.length-1));
        
        // 다 정수로 바꾸기
        var timeToInt = (h*60*60 + m*60 + s)*1000
        var start = timeToInt - t*1000 + 1;
        var end = timeToInt;

        processTime_f.push([start, end]);
        processTime_b.push([end, start]);
    }

    processTime_f = sort_process(processTime_f);
    processTime_b = sort_process(processTime_b);

    // 정렬된 시작시간에 대해서 처리시간 구하기
    for (var i=0; i<processTime_f.length-1; i++) {
        var start = processTime_f[i][0];
        var end = processTime_f[i][1];
        var s_inTime = 1;

        for (var j=i+1; j<processTime_f.length; j++) {
            if (end+1000 < processTime_f[j][0]) {
                break;
            }
            
            if (!(processTime_f[j][0] > start+999)) {
                s_inTime++;
            }
        }

        answer = Math.max(answer, s_inTime);
    }

    // 정렬된 끝시간에 대해서 처리시간 구하기
    for (var i=0; i<processTime_b.length-1; i++) {
        var start = processTime_b[i][1];
        var end = processTime_b[i][0];
        var e_inTime = 1;

        for (var j=i+1; j<processTime_b.length; j++) {
            if (!(processTime_b[j][1] > end+999)) {
                e_inTime++;
            }
        }

        answer = Math.max(answer, e_inTime);
    }

    return answer;
}

// console.log(solution(["2016-09-15 20:59:57.421 0.351s",
// "2016-09-15 20:59:58.233 1.181s",
// "2016-09-15 20:59:58.299 0.8s",
// "2016-09-15 20:59:58.688 1.041s",
// "2016-09-15 20:59:59.591 1.412s",
// "2016-09-15 21:00:00.464 1.466s",
// "2016-09-15 21:00:00.741 1.581s",
// "2016-09-15 21:00:00.748 2.31s",
// "2016-09-15 21:00:00.966 0.381s",
// "2016-09-15 21:00:02.066 2.62s"
// ]));