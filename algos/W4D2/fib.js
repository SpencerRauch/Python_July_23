/* 
  Return the fibonacci number at the nth position, recursively.

  Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
  The next number is found by adding up the two numbers before it,
  starting with 0 and 1 as the first two numbers of the sequence.
*/

const num1 = 0;
const expected1 = 0;

const numX = 55;

const num2 = 1;
const expected2 = 1;

const num3 = 2;
const expected3 = 1;

const num4 = 3;
const expected4 = 2;

const num5 = 4;
const expected5 = 3;

const num6 = 8;
const expected6 = 21;


// 1. Driver 🚗
// 2. Presenter 👩‍💻
// 3. Navigator 🧭

// create the function and decide what params it needs and what it will return
// R.I.O.T.

function fib(n, memo = {0:0, 1:1}){

    if(memo.hasOwnProperty(n)) {
        return memo[n];
    }

    if(n <= 1) {
        return n
    }

    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]
}

for(var i = 1; i <= 500; i++) {
    console.log(`fib(${i}) ==> ${fib(i)}`)
}

// memoization
