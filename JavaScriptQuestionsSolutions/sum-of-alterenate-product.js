// https://www.geeksforgeeks.org/problems/minimize-sum-of-alternate-product2033/1?page=1&sortBy=difficulty
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
        let ans = ob.altProduct(arr);
        console.log(ans);
        console.log("~");
        tc--;
    }
}
// } Driver Code Ends


// User function Template for javascript
class Solution {
    altProduct(arr) {
        // Your code goes here
        // console.log("arr", arr)
        var arr2 = arr.sort((a,b) =>{
            return a-b
        })
        // console.log("arr2",arr2)
        

        var length = arr2.length
        var halfLength = length/2
        // console.log(length,halfLength)
        var num1
        var num2
        var currProduct
        var sum = 0
        for(var i=0;i<=halfLength-1;i++){
            num1 = arr2[i]
            num2 = arr2[length-i-1]
            // console.log("num1" + " " + num1 + " " + "num2" + " " + num2)
            currProduct = num1*num2
            // console.log(currProduct)
            sum = sum + currProduct
        }
        // console.log(sum)
        return sum
    }
}