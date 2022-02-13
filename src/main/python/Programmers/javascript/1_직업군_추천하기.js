function solution(table, languages, preference) {
    let scoreTable = [];

    for (let job of table) {
        let occupationLanguagesList = job.split(' ').reverse();
        let occupation = occupationLanguagesList[5];
        let score = 0;
        
        for (let i=0; i<languages.length; i++) {
            let languagesScore = occupationLanguagesList.indexOf(languages[i])+1;

            score += languagesScore * preference[i];
        }
        scoreTable.push([occupation, score]);
    }

    scoreTable.sort((a,b) => {
        if (a[1] > b[1]) return -1;
        if (a[1] < b[1]) return 1;
        if (a[0] > b[0]) return 1;
        if (a[0] < b[0]) return -1;
    });

    return scoreTable[0][0];
}

solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"], ["PYTHON", "C++", "SQL"], [7, 5, 5]);