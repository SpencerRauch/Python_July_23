/* 
  Given an array of strings
  return the number of times each string occurs (a frequency / hash table)
*/

const arr1 = ["a", "a", "a"];
const expected1 = {
    a: 3,
};

const arr2 = ["a", "b", "a", "c", "Bob", "c", "c", "d"];
const expected2 = {
    a: 2,
    b: 1,
    c: 3,
    Bob: 1,
    d: 1,
};

const arr3 = [];
const expected3 = {};

/**
 * Builds a frequency table based on the given array.
 * @param {Array<string>} arr
 * @returns {Object<string, number>} A frequency table where the keys are items
 *    from the given arr and the values are the amnt of times that item occurs.
 *  Possible hint: .hasOwnProperty() <- Don't know it? Google it as a group!
 */
function makeFrequencyTable(arr) {
    let table = {};
    for (let elem of arr) {
        table.hasOwnProperty(elem) ? table[elem]++ : table[elem] = 1;
        //   statement                 code if true  : code if false 
    }
    return table;
}

console.log(makeFrequencyTable(arr1));
console.log("Expected: ", expected1);
console.log(makeFrequencyTable(arr2));
console.log("Expected: ", expected2);
console.log(makeFrequencyTable(arr3));
console.log("Expected: ", expected3);




// *************************** Algo #2 ***************************

/* 
Given a non-empty array of odd length containing ints where every int but one
has a matching pair (another int that is the same)
return the only int that has no matching pair.
*/

const numsA = [1];
const expectedA = 1;

const numsB = [5, 4, 5];
const expectedB = 4;

const numsC = [5, 4, 3, 4, 3, 4, 5];
const expectedC = 4; // there is a pair of 4s but one 4 has no pair.

const numsD = [5, 2, 6, 2, 3, 1, 6, 3, 2, 5, 2];
const expectedD = 1;

function oddOccurrencesInArray(nums) {
    let table = makeFrequencyTable(nums);
    //   for (let key in table){
    //     if (table[key] % 2 !== 0){
    //         return parseInt(key);
    //     }
    //   }
    let keys = Object.keys(table) //returns an array of the keys of an object
    for (let i = 0; i < keys.length ; i++){
        if (table[keys[i]] % 2 == 1){
            return parseInt(keys[i])
        }
    }
    return false;
}


console.log(oddOccurrencesInArray(numsA), "should equal", expectedA);
console.log(oddOccurrencesInArray(numsB), "should equal", expectedB);
console.log(oddOccurrencesInArray(numsC), "should equal", expectedC);
console.log(oddOccurrencesInArray(numsD), "should equal", expectedD);