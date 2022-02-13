function toBinary(n, arr) {
    let result = [];

    for (let number of arr) {
        let binary = number.toString(2);

        if (binary.length < n) {
            binary = "0".repeat(n-binary.length) + binary;
        }
        result.push(binary);
    }

    return result;
}

function solution(n, arr1, arr2) {
    var answer = [];

    arr1 = toBinary(n, arr1);
    arr2 = toBinary(n, arr2);

    let password = "";

    for (let i=0; i<n; i++) {
        for (let j=0; j<n; j++) {
            if (arr1[i][j] === "0" && arr2[i][j] === "0") {
                password += " ";
            }
            else {
                password += "#"
            }
        }
        answer.push(password);
        password = "";
    }

    return answer;
}

solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28]);