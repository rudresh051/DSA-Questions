// https://www.geeksforgeeks.org/problems/sum-of-distinct-elements4801/1?page=1&sortBy=difficulty
//{ Driver Code Starts
// Driver code
const readline = require('readline');
const rl = readline.createInterface({input : process.stdin, output : process.stdout});

let inputLines = [];
let currentLine = 0;

rl.on('line', (line) => { inputLines.push(line.trim()); });

rl.on('close', () => { main(); });

function readLine() { return inputLines[currentLine++]; }

function main() {
    let tc = parseInt(readLine());
    while (tc > 0) {
        let arr = readLine().split(' ').map(Number);
        let ob = new Solution();
        let ans = ob.findSum(arr);
        console.log(ans);
        // colsole.log("~");
        tc--;
    }
}
// } Driver Code Ends


// User function Template for javascript

class Solution {
    findSum(arr) {
        // code here
        // console.log("arr",arr)
        var obj = {}
        for(let i=0;i<=arr.length-1;i++)
        {
            obj[arr[i]] = arr[i]
        }
        // console.log("obj",obj)
        var sum = 0
        for (var key in obj){
            sum = sum + obj[key]
        }
        // console.log("sum",sum)
        return sum
        
    }
}