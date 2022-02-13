function solution(genres, plays) {
    let bestAlbum = [];
    let genresMap = {};
    let genresPlayCnt = {};
    
    // genre별로 정리
    for (var i=0; i<genres.length; i++) {
        if (genres[i] in genresMap) {
            genresMap[genres[i]].push([plays[i], i]);
            genresPlayCnt[genres[i]] += plays[i];
        }
        else {
            genresMap[genres[i]] = [[plays[i], i]];
            genresPlayCnt[genres[i]] = plays[i];
        }
    }

    // play횟수와 고유 번호에 따른 정렬
    for (var key in genresMap) {
        genresMap[key] = genresMap[key].sort((a,b) => {
        if (b[0] === a[0]) {
            return a[1]-b[1]; // 고유번호 내림차순
        }
        else {
            return b[0]-a[0]; // play횟수 오름차순
        }
        });
    }

    // 가장 많이 재생된 장르 순으로 정렬
    const visitOrder = Object.keys(genresPlayCnt).sort((a,b) => genresPlayCnt[b] - genresPlayCnt[a]);

    // 베스트 앨범 생성
    for (var key of visitOrder) {
        if (genresMap[key].length > 1) {
            bestAlbum.push(genresMap[key][0][1]);
            bestAlbum.push(genresMap[key][1][1]);
        }
        else {
            bestAlbum.push(genresMap[key][0][1]);
        }
    }

    return bestAlbum;
}

console.log(solution(["classic", "pop", "classic", "classic", "pop", "pop"], [500, 600, 150, 800, 2500, 600]));