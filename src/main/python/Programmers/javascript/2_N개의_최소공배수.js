function gcd(a, b) {
    return( b === 0 ? a : gcd(b, a%b) );
}

function solution(arr) {
    var a = arr[0];

    for (var i=1; i<arr.length; i++) {
        a = a * arr[i] / gcd(a, arr[i]);
    }
    
    return a;
}

console.log(solution([2,6,8,14]));