function solution(nums) {
    var answer = 0;
    var nums_len = nums.length/2;
    var set = new Set(nums);
    var uniqueArr = [...set];

    if (uniqueArr.length < nums_len) {
        answer = uniqueArr.length
    }
    else {
        answer = nums_len;
    }
    return answer;
}