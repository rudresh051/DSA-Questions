// https://www.geeksforgeeks.org/problems/search-an-element-in-an-array-1587115621/1?page=1&difficulty=Basic&status=unsolved&sortBy=submissions


//{ Driver Code Starts
// Initial Template for javascript

// Given an array, arr of n integers, and an integer element x, find whether element x is present in the array. Return the index of the first occurrence of x in the array, or -1 if it doesn't exist.


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

function main() {
    let t = parseInt(readLine());
    for (let i = 0; i < t; i++) {
        let arr = readLine().split(' ').map(x => parseInt(x, 10));
        let X = parseInt(readLine(), 10);
        let obj = new Solution();
        console.log(obj.search(arr, X));
    }
}

// } Driver Code Ends


// User function Template for javascript

/**
 * @param {number[]} arr
 * @param {number} x
 * @return {number}
 */
class Solution {
    search(arr, x) {
        // write your code here
        for (var i=0;i<=arr.length-1;i++){
            if(arr[i]==x){
                return i
            }
            else{
                continue
            }
        }
        return -1
    }
}
