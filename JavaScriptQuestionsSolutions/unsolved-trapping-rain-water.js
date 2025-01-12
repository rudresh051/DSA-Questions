//{ Driver Code Starts
// https://www.geeksforgeeks.org/problems/trapping-rain-water-1587115621/1
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
    let i = 0;
    for (; i < t; i++) {
        let arr = readLine().split(' ').map(
            x => parseInt(x)); // Read and split input into an array
        let obj = new Solution();
        console.log(obj.maxWater(arr)); // Use the array directly

        console.log("~");
    }
}
// } Driver Code Ends


// User function Template for javascript

/**
 * @param {number[]} arr
 * @returns {number}
 */

class Solution {
    // Function to find the trapped water between the blocks.
    maxWater(arr) {
        var res = []
        var sum = 0

        // code here
        for(var i=0;i<=arr.length-1;i++){
            if(arr[i] > arr[0]){
                res.push(0)
            }else{
                res.push(arr[0]-arr[i])
            }
        }
        
        console.log("res",res)
        for(var i=0;i<=res.length-1;i++){
            sum = sum + res[i]
        }
        console.log("sum",sum)
    }
}