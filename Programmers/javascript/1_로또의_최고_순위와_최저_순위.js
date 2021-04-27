function solution(lottos, win_nums) {
    let answer = [];
    let max_lotto = 0;
    let min_lotto = 0;
    let winning_grade = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6};
    let dict = {};

    for (var num of win_nums) {
        dict[num] = 1;
    }

    for (var num of lottos) {
        if (num === 0) {
            max_lotto += 1;
            continue;
        }

        if (dict[num] === 1) {
            max_lotto += 1;
            min_lotto += 1;
        }
    }

    answer.push(winning_grade[max_lotto]);    
    answer.push(winning_grade[min_lotto]);
    console.log(answer);
    return answer;
}

solution([44, 1, 0, 0, 31, 25],[31, 10, 45, 1, 6, 19]);