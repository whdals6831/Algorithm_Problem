function delSideDot(new_id) {
    if (new_id[0] === '.') {
        new_id = new_id.substring(1,new_id.length);
    }

    if (new_id[new_id.length-1] === '.') {
        new_id = new_id.substring(0,new_id.length-1);
    }

    return new_id;
}

function solution(new_id) {
    new_id = new_id.toLowerCase();
    new_id = new_id.match(/[a-z0-9._-]/g).join('');
    new_id = new_id.replace(/[\.]+/g, ".");
    
    new_id = delSideDot(new_id);
    
    if (new_id.length === 0) {
        new_id = 'a';
    }
    
    if (new_id.length > 15) {
        new_id = new_id.substr(0, 15);
    }
    
    new_id = delSideDot(new_id);
    

    while (new_id.length < 3) {
        new_id = new_id + new_id[new_id.length-1];
    }

    return new_id;
}

console.log(solution("...!@BaT#*..y.abc-_defgh2ijklm"));