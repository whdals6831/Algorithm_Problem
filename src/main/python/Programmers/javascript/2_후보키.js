function getSubsets(arr) { // 멱집합 구하기
    let flag = new Array(arr.length).fill(false);
    const subSets = [];
  
    const subSet = function DFS (depth) { // 부분 집합 구하는 재귀 함수, DFS 알고리즘
      if (depth === arr.length) { // 트리의 끝에 다다른 것 ==> 재귀 종료 조건
        const subSet = arr.filter((value, index) => flag[index]); // 해당 flag true => 부분집합 포함
        subSets.push(subSet); // 부분집합들을 담는 배열에 push
  
        return;
      }
  
      flag[depth] = true; // 해당 depth의 flag true = 트리의 왼쪽
      subSet(depth + 1); // 트리의 왼쪽에 대해 재귀호출
  
      flag[depth] = false; // 해당 depth의 flag false = 트리의 오른쪽
      subSet(depth + 1); // 트리의 오른쪽에 대해 재귀 호출
    }
    
    subSet(0); // depth 0 부터 시작
    return subSets;
  }

function solution(relation) {
    var answer = 0;
    var nonUnique = [];

    for (var i=0; i<relation[0].length; i++) {
        var temp = new Set();

        for (var key of relation) {
            temp.add(key[i]);
        }

        if (temp.size === relation.length) {
            answer++;
        }
        else {
            nonUnique.push(i);
        }
    }

    const multiKeyList = getSubsets(nonUnique).sort((a,b) => a.length - b.length); // 후보키를 만들 수 있는 경우의 수
    let clearKey = []; // 생성된 후보키

    for (var multiKey of multiKeyList) {
        if (multiKey.length < 2) continue;
        var flag = false;
        
        if (clearKey.length > 0) {
            for (var k of clearKey) { // 후보키가 포함되면 pass
                if (k.every(v => multiKey.indexOf(v) != -1)) {
                    flag = true;
                    break;
                };
            }
        }

        if (flag) continue;

        let temp = new Set();

        for (var i=0; i<relation.length; i++) {
            let word = "";
            for (var j of multiKey) {
                word += relation[i][j];
            }
            temp.add(word);
        }

        if (temp.size === relation.length) {
            answer++;
            clearKey.push(multiKey);
        }
    }

    return answer;
}

console.log(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]));
console.log(solution([["a","b","c"],["1","b","c"],["a","b","4"],["a","5","c"]]));
console.log(solution([["a","1","4"],["2","1","5"],["a","2","4"]])); // 후보키 (0,1), (1,2)
