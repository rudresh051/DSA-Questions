// https://www.geeksforgeeks.org/problems/ishaan-loves-chocolates2156/1?page=1&sortBy=difficulty
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
        let arr = new Array(n);
        let input_ar1 = readLine().split(' ').map(x=>parseInt(x));
        for(let i=0;i<n;i++){
            arr[i] = input_ar1[i];
        }
        let obj = new Solution();
        let res = obj.chocolates(arr, n);
        console.log(res);
        
    
console.log("~");
}
}// } Driver Code Ends



// } Driver Code Ends


//User function Template for javascript



/**
 * @param {number[]} arr
 * @param {number} n
 * @returns {number}
*/

class Solution{
    chocolates(arr,n){
        console.log("arr",arr)
        
        while(arr.length > 1){
            var elemFirst = arr[0]
            var elemLast = arr[arr.length-1]
            
            if(elemFirst >= elemLast){
                arr.shift();
            }
            else{
                arr.pop();
            }
        }
        return arr[0]
        
    }
}

