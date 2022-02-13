function solution(bridge_length, weight, truck_weights) {
    let answer = 0;
    let now_weight = 0;
    let q = [];

    while (truck_weights.length > 0 || q.length != 0) {

        if (q.length > 0 && q[0][1] > bridge_length) {
            var tb = q.shift();
            now_weight -= tb[0];
        }

        if (truck_weights[0] + now_weight <= weight) {
            var tw = truck_weights.shift();
            q.push([tw, 1]);
            now_weight += tw;
        }

        for (var i=0; i<q.length; i++) {
            q[i][1] += 1;
        }

        answer++;
    } 

    return answer;
}

console.log(solution(2, 10, [7,4,5,6]));