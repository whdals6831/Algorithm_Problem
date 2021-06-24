function solution(enroll, referral, seller, amount) {
    var answer = [];
    let chart = {};

    for (var i=0; i<enroll.length; i++) {
        chart[enroll[i]] = {
            benefit: 0, 
            parent: referral[i]
        }
    }

    for (var i=0; i<seller.length; i++) {
        var benefit = amount[i]*100;
        var parent = seller[i];

        while (benefit > 0 && parent != '-') {
            let fees = Math.floor(benefit*0.1);
            let take = benefit-fees;

            if (fees === 0) {
                take = benefit;
            }

            chart[parent]["benefit"] += take;
            benefit = fees;
            parent = chart[parent]["parent"];
        }
    }

    for (var name of enroll) {
        answer.push(chart[name]["benefit"]);
    }

    return answer;
}

console.log(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],["young", "john", "tod", "emily", "mary"],[12, 4, 2, 5, 10]));