function getContent(page) {
    let regex = '<meta property="og:url" content="\\S*';
    let metaTag = page.match(regex)[0];
    metaTag = metaTag.split(/content="|"\/>/);
    return metaTag[1];
}

function getLink(page) {
    let link = [];
    let temp = page.match(/<a href="\S*">/g);
    if (temp) {
        for (let aTag of temp) {
            link.push(aTag.slice(9, aTag.length-2));
        }
    }

    return link;
}

function solution(word, pages) {
    let website = new Map();
    let index = 0;

    for (let page of pages) {
        let content = getContent(page);
        let link = getLink(page);
        let baseScore = 0;
        page = page.split(/[^a-zA-Z]/g);

        for (let searchText of page) {
            if (searchText.toLowerCase() === word.toLowerCase()) {
                baseScore++;
            }
        }

        let outLinks = link.length;
        let linkScore = outLinks != 0 ? baseScore/outLinks : 0;

        website.set(content ,[index, baseScore, link, linkScore]);
        index++;
    }

    for (const [index, baseScore, link, linkScore] of website.values()) {
        for (let site of link) {
            if (website.has(site)) {
                let value = website.get(site);
                website.set(site, [value[0], value[1]+linkScore, value[2], value[3]]);
            }
        }
    }

    website = new Map([...website.entries()].sort((a,b) => {
        if (a[1][1] > b[1][1]) return -1;
        if (a[1][1] < b[1][1]) return 1;
        if (a[1][0] > b[1][0]) return 1;
        if (a[1][0] < b[1][0]) return -1;
    }));
    
    return website.entries().next()['value'][1][0];
}

solution('Muzi',["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]);