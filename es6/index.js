function getlength(number) {
    return number.toString().length;
}
function check(a,b){
    //let ascii = a.charCodeAt(0);
    // console.log(a,b);
    if(parseInt(b)===parseInt(a)+1 || parseInt(b)===parseInt(a)-1){
        //console.log("hi");
        return true;
    }
    else if((a==='0' && b==='9')||(a==='0' && b==='9')){
        //console.log("hi");
        return true;
    }
    return false;
}
function processData(input) {
    if(getlength(input)<3){
        // console.log("No");
        return 0;
    }
    let n = input.toString();
    console.log(n.length);
    const map1 = new Map();
    map1.set(0, {val: 0});
    map1.set(1, {val: 0});
    map1.set(2, {val: 0});
    map1.set(3, {val: 0});
    map1.set(4, {val: 0});
    map1.set(5, {val: 0});
    map1.set(6, {val: 0});
    map1.set(7, {val: 0});
    map1.set(8, {val: 0});
    map1.set(9, {val: 0});
    while (input>0) {
        // console.log(input%10);
        map1.get(input%10).val++;
        input=Math.floor(input/10);
        // console.log(input);
    }
    i=0;
    
    // console.log("hi0");
    let count=0;
    while (i<=9){
        if(map1.get(i).val===n.length-1){
            
            console.log("Yes");
            return 0;
        }
        else if(map1.get(i).val===2){
            count++;
        }
        i=i+1;
    }
    if(count*2+1===n.length){
        console.log("Yes");
        return 0;
    }
    // console.log("hi1");
    if(map1.get(0).val===n.length-2){
        console.log("Yes");
        return 0;
    }
    // console.log("hi2");
    i=0;
    f=0;
    while (i<n.length-1){
        let p=true,q=true;
        if(i-1>=0){
           p=check(n.charAt(i),n.charAt(i-1)); 
        }
        if(i+1<n.length-1){
            q=check(n.charAt(i),n.charAt(i+1)); 
        }
        if(p===false || q===false){
            f=1;
            break;
        }
        // console.log(p,q);
        i++;

    }
    // console.log("hi3");
    
    if(f===0){
        // console.log("hi");
        console.log("Yes");
        return 0;
    }
    var reverseWord = n.split("").reverse().join("");
    if(n===reverseWord){
        console.log("Yes");
        return 0;
    }
    console.log("No");
}
processData(1000000000000);