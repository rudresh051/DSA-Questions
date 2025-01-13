// https://www.geeksforgeeks.org/problems/print-pattern3549/1
//{ Driver Code Starts
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

function printList(res,n){
    let s="";
    for(let i=0;i<n;i++){
        s+=res[i];
        s+=" ";
    }
    console.log(s);
}


function main() {
    let t = parseInt(readLine());
    let i = 0;
    for(;i<t;i++)
    {
        let n = parseInt(readLine());
        let obj = new Solution();
        let res = obj.pattern( n);
        printList(res, res.length)
    }
}// } Driver Code Ends





// } Driver Code Ends


//User function Template for javascript


/**
 * @param {number} n
 * @returns {number[]}
*/

class Solution{
    pattern(n){
        //code here
        if(n<=0){
            return
        }
        else{
            console.log(n)
            this.pattern(n-5)
            console.log(n)
        }
    }
}

