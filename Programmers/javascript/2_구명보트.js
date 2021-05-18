function solution(people, limit) {
    let answer = 0;

    people.sort((a, b) => { return b-a; });

    let left = 0;
    let right = people.length - 1;

    while (left <= right) {
        if (people[left] <= limit/2) {
            answer += Math.ceil((right - left + 1) / 2);
            break;
        }

        if (people[left] + people[right] <= limit) {
            left++;
            right--;
        }
        else {
            left++;
        }
        answer++
    }
    
    return answer;
}

// solution([70, 50, 80, 50], 100);