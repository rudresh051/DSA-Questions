// https://www.geeksforgeeks.org/problems/a-guy-with-a-mental-problem1604/1?page=1&sortBy=difficulty

//{ Driver Code Starts
// Initial Template for JavaScript
// Position this line where user code will be pasted.
function main() {
    const t = parseInt(readLine());
    for (let i = 0; i < t; i++) {
        const arr1 = readLine().split(' ').map(Number);
        const arr2 = readLine().split(' ').map(Number);
        const solution = new Solution();
        console.log(solution.minTime(arr1, arr2));
        console.log("~");
    }
}

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => { inputString += inputStdin; });

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => string.trim());
    main();
});

function readLine() { return inputString[currentLine++]; }

// } Driver Code Ends


class Solution {
    minTime(arr1, arr2) {
        // code here.
        var arr1EvenPlacesSum = 0
        var arr1OddPlacesSum = 0
        var arr2EvenPlacesSum = 0
        var arr2OddPlacesSum = 0
        
        for(var i=0;i<=arr1.length-1;i++){
            if(i%2==0){
                arr1EvenPlacesSum = arr1[i] + arr1EvenPlacesSum
            }
            else{
                arr1OddPlacesSum = arr1[i] + arr1OddPlacesSum
            }
        }
        
        // console.log(arr1EvenPlacesSum, arr1OddPlacesSum)
        
        
        for(var i=0;i<=arr2.length-1;i++){
            if(i%2==0){
                arr2EvenPlacesSum = arr2[i] + arr2EvenPlacesSum
            }
            else{
                arr2OddPlacesSum = arr2[i] + arr2OddPlacesSum
            }
        }
    //   console.log(arr2EvenPlacesSum, arr2OddPlacesSum)
       
       if((arr1EvenPlacesSum + arr2OddPlacesSum) < (arr1OddPlacesSum + arr2EvenPlacesSum)){
           return (arr1EvenPlacesSum + arr2OddPlacesSum)
       }
       else{
           return (arr1OddPlacesSum + arr2EvenPlacesSum)
       }
        
    }
}
