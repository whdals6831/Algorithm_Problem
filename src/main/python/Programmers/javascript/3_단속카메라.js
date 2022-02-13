function solution(routes) {
    let answer = 0;

    routes.sort((a,b) => {
        if (a[0] < b[0]) return -1;
        if (a[0] > b[0]) return 1;
        if (a[1] < b[1]) return -1;
        if (a[1] > b[1]) return 1;
    })


    let left = routes[0][0];
    let right = routes[0][1];
    answer++;
    
    for (let i=1; i<routes.length; i++) {
        if (right < routes[i][0]) {
            left = routes[i][0];
            right = routes[i][1];
            answer++;
        }
        else {
            left = routes[i][0];
            right = Math.min(right, routes[i][1]);
        }
    }

    return answer;
}

console.log(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]));