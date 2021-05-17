function numOfCase(order) { // string
    let len = order.length;
    let result = [];
    order = order.split('').sort().join('');
    result.push(order[len-1]);
    
    for (var i=len-2; i>=0; i--) { // 끝에서 시작하여 앞에 채워나가는 형식
        var temp = [];
        for (var j of result) {
            temp.push(order[i]+j);
        }
        result = [...temp, ...result];
        result.push(order[i]);
    }

    return result; // array
}

function solution(orders, course) {
    var answer = [];
    var orderCnt = {};

    for (var i of orders) {
        var result = numOfCase(i);

        for (var j of result) { // 메뉴별 주문 횟수 파악
            if (j in orderCnt) {
                orderCnt[j] += 1;
            }
            else {
                orderCnt[j] = 1;
            }
        }
    }

    for (var courseLen of course) {
        var max = 0;
        var temp = [];

        for (var order in orderCnt) {
            if (order.length === courseLen && orderCnt[order] > 1) {
                if (orderCnt[order] === max) {
                    temp.push(order);
                }
                else if (orderCnt[order] > max) {
                    max = orderCnt[order];
                    temp = [];
                    temp.push(order);
                }
            }
        }
        answer = [...answer, ...temp]
    }

    return answer.sort();
}

// solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]);
// console.log(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]));
// console.log(solution(["XYZ", "XWY", "WXA"], [2,3,4]));