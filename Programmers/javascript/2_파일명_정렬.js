function solution(files) {
    files.sort((a,b) => {
        var a_head = a.replace(/[^a-zA-Z]/g, " ").split(/\s+/g);
        var a_number = a.match(/\d+/g);
        var b_head = b.replace(/[^a-zA-Z]/g, " ").split(/\s+/g);
        var b_number = b.match(/\d+/g);

        if (a_head[0].toLowerCase() < b_head[0].toLowerCase()) return -1;
        if (a_head[0].toLowerCase() > b_head[0].toLowerCase()) return 1;
        if (Number(a_number[0]) < Number(b_number[0])) return -1;
        if (Number(a_number[0]) > Number(b_number[0])) return 1;
    })

    return files;
}

// console.log(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]));
// console.log(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]));
// console.log(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]));
console.log(solution(["fe"]));
