// https://www.geeksforgeeks.org/problems/smallest-number-repeating-k-times3239/1?page=1&sortBy=difficulty
//{ Driver Code Starts
'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => { inputString += inputStdin; });

process.stdin.on('end', () => {
    inputString = inputString.trim().split('\n').map(string => string.trim());
    main();
});

function readLine() { return inputString[currentLine++]; }

function printList(arr) { console.log(arr.join(' ')); }

function main() {
    let t = parseInt(readLine(), 10);
    for (let i = 0; i < t; i++) {
        let arr = readLine().split(' ').map(x => parseInt(x, 10));
        let k = parseInt(readLine(), 10);
        let obj = new Solution();
        let res = obj.findDuplicate(arr, k);
        console.log(res);
    }
}

// } Driver Code Ends


// User function Template for javascript

/**
 * @param {number[]} arr
 * @param {number} k
 * @returns {number}
 */

class Solution {
    // Function to count the number of subarrays with a sum divisible by k
    findDuplicate(arr, k) {
        // code here
        
    var countMap = {}
    for(var value of arr){
        // console.log("arr[values]",arr[values])
        if(countMap[value]){
            countMap[value] = countMap[value] + 1;
        }
        else{
            countMap[value] = 1;
        }
    }   
    
    
    const result = []
    
    for(var num in countMap){
        if(countMap[num] === k){
            result.push(num);
        }
    }
    // console.log("result",result)
    if(result.length===0){
        return -1
    }
        
    return Math.min(...result.map(Number))

        
        
    }
}
