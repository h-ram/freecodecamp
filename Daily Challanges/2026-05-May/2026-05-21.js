function iBeforeE(sentence) {
  sentence = sentence.replaceAll("ei", "ie");
  sentence = sentence.replaceAll("cie", "cei");
  return sentence;
}
console.log(iBeforeE("beleive"));
console.log(iBeforeE("recieve"));
console.log(iBeforeE("we recieved a breif"));
