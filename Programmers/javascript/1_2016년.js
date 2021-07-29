function solution(a, b) {
    let day = {
        0: "SUN",
        1: "MON",
        2: "TUE",
        3: "WED",
        4: "THU",
        5: "FRI",
        6: "SAT"
    }
    let dayNumber = new Date(`2016/${a}/${b}`).getDay();

    return day[dayNumber];
}

console.log(solution(5,24));