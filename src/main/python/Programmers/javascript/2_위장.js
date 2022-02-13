function solution(clothes) {
    var answer = 0;
    let clothesList = {};

    for (var cloth of clothes) {
        if (cloth[1] in clothesList) {
            clothesList[cloth[1]].push(cloth[0]);
        }
        else {
            clothesList[cloth[1]] = [cloth[0]];
        }
    }

    if (Object.keys(clothesList).length === 1) {
        for (var i in clothesList) {
            answer = clothesList[i].length;
        }
    }
    else {
        let result = 1;

        // 안입는 경우까지 포함해서 각 옷 리스트 길이만큼 곱하기
        for (var i in clothesList) {
            result = result * (clothesList[i].length + 1);
        }

        result -= 1 // 모두 안입는 경우 제외
        answer = result;
    }

    return answer;
}

// console.log(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]));