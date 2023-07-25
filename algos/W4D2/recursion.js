// http://pages.di.unipi.it/marino/python/Recursion/TheThreeLawsofRecursion.html

// RECURSION
// repeating
// calls itself / loop
// a function that calls itself

/*
a multi line 
comment
here
*/

/**
 * this is a cool var
 */
// var x = "cool"

/**
 * this function is cool 😎
 */
function hi() {
    console.log("hello")
    hi();
}

// hi();

// ===============


// 5!
// 5*4*3*2*1
// 3!
// 3*2*1
// 2!
// 2*1
// 1!
// 1
// 0!
// 1





/* 
  Recursive Factorial

  Input: integer
  Output: integer, product of ints from 1 up to given integer
  
  If less than zero, treat as zero.
  Bonus: If not integer, truncate (remove decimals).
  
  Experts tell us 0! is 1.
  
  rFact(3) = 6 (1*2*3)
  rFact(6.8) = 720 (1*2*3*4*5*6)
*/

const num1 = 3;
const expected1 = 6;
// Explanation: 1*2*3 = 6

const num2 = 6.8;
const expected2 = 720;
// Explanation: 1*2*3*4*5*6 = 720

const num3 = 0;
const expected3 = 1;

/**
 * Recursively multiples 1 to the given int.
 * - Time: O(?).
 * - Space: O(?).
 * @param {number} n The int to factorial. Treat negatives as zero and
 *    floor decimals.
 * @returns {number} The result of !n.
 */
//                 4
function factorial(n) {
  // 1. base case
  if (n == 1) {
    return 1
  }
  // 2. logic towards the base case
  // 3. call the function again
  return n * factorial(n - 1)
}
console.log(
  factorial(4)
)