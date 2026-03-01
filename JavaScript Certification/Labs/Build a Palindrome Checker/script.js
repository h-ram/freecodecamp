const textInput = document.querySelector("#text-input")
const checkBtn = document.querySelector("#check-btn")
const result = document.querySelector("#result")

checkBtn.addEventListener("click", ()=>{
  const val = textInput.value;
  if(val == ""){
    alert("Please input a value");
    return;
  }
  if(isPalindrome(val)){
    result.textContent = `${val} is a palindrome`
  }else{
    result.textContent = `${val} is not a palindrome`
  }
  setTimeout(()=>{
    result.textContent = ""
  }, 10000)
});

textInput.addEventListener("focus",()=>{
  result.textContent = "";
  textInput.value = "";
})
function isPalindrome(str) {
  const cleaned = str.toLowerCase().replace(/[^a-z0-9]/g, "");
  const reversed = cleaned.split("").reverse().join("");
  return cleaned === reversed;
}