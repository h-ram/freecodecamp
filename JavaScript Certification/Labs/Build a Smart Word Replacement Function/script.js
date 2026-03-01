function myReplace(str,oldWord,newWord){
  if(/^[A-Z]/.test(oldWord)){
    console.log("yes");
    newWord = newWord[0].toUpperCase()+newWord.slice(1);
  }else{
    newWord = newWord[0].toLowerCase() + newWord.slice(1);
  }
  return str.replace(oldWord, newWord);
}
console.log(myReplace("Let us go to the store", "store", "mall"));
console.log(myReplace("He is Sleeping on the couch", "Sleeping", "sitting"));
console.log(myReplace("I think we should look up there", "up", "Down"));