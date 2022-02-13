function isNumeric(data) {
    return !isNaN(Number(data))
}

function solution(dartResult) {
    var threeChance = [0];
    var idx = 1;
    var s = '';
    
    for (var i of dartResult) {
        if (isNumeric(i)) {
            s += i;
        }    
        else if ( i==='S' || i==='D' || i==='T' ) {
            threeChance.push(Number(s));
            s = '';
            
            if (i==='D') {
                threeChance[idx] = Math.pow(threeChance[idx], 2);
            }

            if (i==='T') {
                threeChance[idx] = Math.pow(threeChance[idx], 3);
            }
            idx += 1
        }
        else if (i==='#') {
            threeChance[idx-1] = threeChance[idx-1]*(-1);
        }
        else if (i==='*') {
            threeChance[idx-2] = threeChance[idx-2]*2;
            threeChance[idx-1] = threeChance[idx-1]*2;
        }
    }

    return threeChance[1] + threeChance[2] + threeChance[3];
}