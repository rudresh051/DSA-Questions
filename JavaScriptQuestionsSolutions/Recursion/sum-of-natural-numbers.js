// Recursive function to find the sum of 
// numbers from 0 to n
function findSum(n) {

    // Base case 
    if (n === 0) 
        return 0; 
    
    // Recursive case 
    return n + findSum(n - 1);
}

let n = 5;
console.log(findSum(n));