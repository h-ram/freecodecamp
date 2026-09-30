
function isPrime(num){
    if(num<2){return false}
    for(let d = 2;d<num/2+1;d++){
        if(num%d === 0) return false;
    }
    return true
}

module.exports = {
    isPrime,
}