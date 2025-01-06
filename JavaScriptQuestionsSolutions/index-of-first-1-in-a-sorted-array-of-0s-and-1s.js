// https://www.geeksforgeeks.org/explore?page=1&sortBy=difficulty&itm_source=geeksforgeeks&itm_medium=main_header&itm_campaign=practice_header
//{ Driver Code Starts
// Position this line where user code will be pasted.
const readline = require('readline')
                     .createInterface({input : process.stdin, output : process.stdout});

const input = [];
readline.on('line', (line) => { input.push(line); }).on('close', () => {
    const t = parseInt(input[0], 10);
    for (let i = 1; i <= t; i++) {
        const arr = input[i].split(' ').map(Number);
        const ob = new Solution();
        console.log(ob.firstIndex(arr));
        console.log("~");
    }
});
// } Driver Code Ends

 
// User function Template for javascript

/**
 * @param {number[]} arr

 * @returns {number}
*/

class Solution {
    firstIndex(arr) {
        // code here
        for(var i=0;i<=arr.length-1;i++){
            if(arr[i]==1){
                return i
            }
            else if(arr[i]==0){
                continue
            }
        }
        return -1
    }
}
