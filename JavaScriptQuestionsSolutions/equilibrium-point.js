//{ Driver Code Starts
// Initial Template for javascript
'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => { inputString += inputStdin; });

process.stdin.on('end', _ => {
    inputString =
        inputString.trim().split('\n').map(string => { return string.trim(); });

    main();
});

function readLine() { return inputString[currentLine++]; }

function main() {
    let t = parseInt(readLine());
    for (let i = 0; i < t; i++) {
        const arr = readLine().split(' ').map(x => parseInt(x));
        let obj = new Solution();
        let ans = obj.findEquilibrium(arr);
        if (ans == -0) ans = 0;
        console.log(ans);
        console.log('~');
    }
}
// } Driver Code Ends


// User function Template for javascript

/**
 * @param {number[]} arr
 * @returns {number}
 */

class Solution {
    // Function to find equilibrium point in the array.
    findEquilibrium(arr) {
        // code here
        let totalSum = arr.reduce((acc, val) => acc + val, 0);
        let leftSum = 0;

        for (let i = 0; i < arr.length; i++) {
            totalSum -= arr[i]; 
            // console.log("totalSum",totalSum)
            
            if (leftSum === totalSum) {
                return i; 
            }
            
            leftSum += arr[i]; // Update left sum for next iteration
        }

        return -1; // No equilibrium index found
    }
}