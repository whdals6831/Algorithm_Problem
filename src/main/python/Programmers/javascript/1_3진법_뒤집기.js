function solution(n) {
    var answer = 0;
    
    var ts = n.toString(3);
    ts = [...ts].reverse().join("");
    
    for (var i=ts.length-1; i>=0; i--) {
        console.log(ts[i])
        answer += Number(ts[i])*Math.pow(3, ts.length-1-i)
    }
    
    return answer;
}