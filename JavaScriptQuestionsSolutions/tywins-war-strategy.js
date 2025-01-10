// https://www.geeksforgeeks.org/problems/tywins-war-strategy0527/1?page=1&sortBy=difficulty
//{ Driver Code Starts
process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => { inputString += inputStdin; });

process.stdin.on('end', () => {
    inputString = inputString.trim().split('\n');
    main();
});

function readLine() { return inputString[currentLine++]; }

function main() {
    const t = parseInt(readLine(), 10);
    const solution = new Solution();

    for (let i = 0; i < t; i++) {
        const arr = readLine().split(' ').map(Number);
        const k = parseInt(readLine(), 10);
        console.log(solution.minSoldiers(arr, k));
        console.log("~");
    }
}

// } Driver Code Ends


class Solution {
    minSoldiers(arr, k) {
        // code here.
        var count = 0
        var halfLen = Math.ceil(arr.length/2) 
        console.log("halfLen",halfLen)
        for(let i=0;i<=arr.length-1;i++){
            if(arr[i]%k==0){
                count++
            }
            else{
                continue
            }
        }
        console.log("count",count)
        
        if(count < halfLen){
            // cost function code
        }
        else{
            return 0
        }
        
        
        
    }
}