// Given a sorted array arr[] of distinct integers. Sort the array into a wave-like array(In Place). In other words, arrange the elements into a sequence such that arr[1] >= arr[2] <= arr[3] >= arr[4] <= arr[5].....
// If there are multiple solutions, find the lexicographically smallest one.

// Note: The given array is sorted in ascending order, and you don't need to return anything to change the original array.

//{ Driver Code Starts
//Initial Template for javascript

//Initial Template for javascript


'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

function main() {
    let t = parseInt(readLine());
    let i = 0;
    for(;i<t;i++)
    {
        let n = parseInt(readLine());
        let arr = new Array(n);
        let input_ar0 = readLine().split(' ').map(x=>parseInt(x));
        for(let i=0;i<n;i++)
            arr[i] = input_ar0[i];
    
        let obj = new Solution();
        arr = obj.convertToWave(n, arr);
        let ans = "";
        for(let element of arr) ans += element + " ";
        
        console.log(ans);
    }
}
// } Driver Code Ends


//User function Template for javascript

class Solution {
    // arr: input array
    // n: size of array
    //Function to sort the array into a wave-like array.
    convertToWave(n, arr)
    {
        // Steps 
        // 1. Initialize two empty array arr1, arr2
        // 2. Loop over the given array ones only for odd values of i and ones only even values of i
        // 3. push to arr1 when i is only odd values
        // 4. push to arr2 when i is only even values
        // 5. Now initialize an empty array arr3
        // 6. Loop over the arr1 or arr2
        // 7. Push to arr3 for each value of i when i is even and when i is odd
    }
}