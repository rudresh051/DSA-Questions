// Optimized Code
function runProgram(input) {
  // console.log(input)
  var arr1 = input.split("\n")
  // console.log("arr1", arr1)
  var arr2 = arr1.shift()
  // console.log("arr1", arr1)
  arr3 = arr1.map(function(val){
      return parseInt(val)
  })
  // console.log("arr3", arr3)
  
  for(var i=0;i<=arr3.length-1;i++){
      // console.log("i" + " " + i + " " +  "arr3[i]" + " " + arr3[i])
      checkPrime(arr3[i])
  }
  
  function checkPrime(arrayReceived){
      // console.log("arrayReceived", arrayReceived)
      var currentArrayNumber = arrayReceived
      if(currentArrayNumber == 1){
          console.log("No")
      }
      else if(currentArrayNumber==2){
          console.log("Yes")
      }
      else if(currentArrayNumber > 2){
          flag = true
          // var count = 0
          for(var j=2;j<=Math.sqrt(currentArrayNumber);j++){
              // console.log(`The value of j is ${j} and currentArrayNumber is ${currentArrayNumber}`)
              // console.log(`The value of currentArrayNumber ${currentArrayNumber} divided by current j ${j} is ${currentArrayNumber%j}`)
              
              if(currentArrayNumber%j==0){
                  // count=count+1
                  flag = false; // If a divisior is found, set flag to false
                  break;
              }
          }
          // if(count > 2){
          //     // console.log("Inside if current count value",count)
          //     console.log("No")
          // }
          // else{
          //     console.log("Yes")
          // }
          if(flag){
              console.log("Yes")
          }
          else{
              console.log("No")
          }
      }
      
      
  }
  
}

if (process.env.USER === "") {
runProgram(``);
} else {
process.stdin.resume();
process.stdin.setEncoding("ascii");
let read = "";
process.stdin.on("data", function (input) {
  read += input;
});
process.stdin.on("end", function () {
  read = read.replace(/\n$/, "");
  read = read.replace(/\n$/, "");
  runProgram(read);
});
process.on("SIGINT", function () {
  read = read.replace(/\n$/, "");
  runProgram(read);
  process.exit(0);
});
}