// https://www.geeksforgeeks.org/problems/kth-smallest-element5635/1?page=1&sortBy=submissions
//{ Driver Code Starts
// Initial Template for javascript

"use strict";

process.stdin.resume();
process.stdin.setEncoding("utf-8");

let inputString = "";
let currentLine = 0;

process.stdin.on("data", (inputStdin) => { inputString += inputStdin; });

process.stdin.on("end", (_) => {
    inputString =
        inputString.trim().split("\n").map((string) => { return string.trim(); });

    main();
});

function readLine() { return inputString[currentLine++]; }

function main() {
    let t = parseInt(readLine());
    let i = 0;

    for (; i < t; i++) {
        // let N = parseInt(readLine());
        let arr = readLine().trim().split(" ").map((x) => parseInt(x));
        let k = parseInt(readLine());
        let obj = new Solution();
        let res = obj.kthSmallest(arr, k);
        console.log(res);

        console.log("~");
    }
}

// } Driver Code Ends


// User function Template for javascript

/**
 * @param {number[]} arr
 * @param {number} k
 * @return {number}
 */

class Solution {
    kthSmallest(arr, k) {
        // code here
        // console.log("arr",arr)
        var arr2 = arr.sort((a,b) =>{
            return a-b
        })
        
        // console.log("arr2",arr2)
        
        return arr2[k-1]
    }
}

// Follow up: Don't solve it using the inbuilt sort function.