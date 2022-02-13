function solution(land) {
    let result = land[0];
    
    for (var i=1; i<land.length; i++) {
        var temp = [...result];
        for (var j=0; j<4; j++) {
            for (var k=0; k<4; k++) {
                if (j === k) {
                    continue;
                }
                result[j] = Math.max(result[j], temp[k]+land[i][j]);
            }
        }
    }

    return Math.max(...result);
}

console.log(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]));