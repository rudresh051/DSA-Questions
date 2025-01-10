// https://www.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/1?page=1&sortBy=submissions
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
        let ans = obj.maxSubarraySum(arr);
        if (ans == -0) ans = 0;
        console.log(ans);
    }
}
// } Driver Code Ends


// User function Template for javascript

/**
 * @param {number[]} arr
 * @returns {number}
 */
class Solution {
    // Function to find the sum of contiguous subarray with maximum sum.
    maxSubarraySum(arr) {
        // code here
        var result = arr[0]
        for(var i=0;i<=arr.length-1;i++){
            var currSum = 0
            for(var j = i;j<=arr.length-1;j++){
                currSum = currSum + arr[j]
                // console.log("currSum",currSum)
                result = Math.max(result,currSum)
            }
        }
        
        // console.log("maxSum",maxSum)
        return result
        
    }
}

// Hint : Please optimize your code and submit again.