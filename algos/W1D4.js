/* 
  String: Is Palindrome
  Create a function that returns a boolean whether the string is a strict palindrome. 
    - palindrome = string that is same forwards and backwards
  
  Do not ignore spaces, punctuation or capitalization
*/
// RIOT Read Input Output Talk
const str1 = "a x a";
const expected1 = true;

const str2 = "racecar";
const expected2 = true;

const str3 = "Dud";
const expected3 = false;

const str4 = "oho!";
const expected4 = false;

const str5 = "abba";
const expected5 = true;


function isPalindrome(str) {
  //Your code here
}

console.log(isPalindrome(str1)); //expected: true
console.log(isPalindrome(str2)); //expected: true
console.log(isPalindrome(str3)); //expected: false
console.log(isPalindrome(str4)); //expected: false
console.log(isPalindrome(str5)); //expected: true


function isPalindrome(str) {
  if (str.length < 2) return true;
  let start = 0;
  let end = str.length - 1;
  while (start < end) {
    if (str[start] !== str[end]) return false;
    start++;
    end--;
  }
  return true;
}


function isPalindrome2(str) {
  let str2 = str;
  str2 = str2.split('').reverse().join('')
  return str2 === str;
}