
function runProgram(input) {
  //   console.log(input)
    input1 = input.split("\n")
  //   console.log(input1)
    
    var arr1 = input1.shift()
  //   console.log("input1",input1)
    for (var i=0;i<=input1.length-1;i++){
        if(checkPowerOf2(input1[i])){
            console.log("True")
        }
        else{
            console.log("False")
        }
    }
    
    function checkPowerOf2(currentNumber){
        var Quotient
        Quotient = currentNumber/2
        if(Quotient==1){
          // Stopping the recursion
            return true
        }
        else if(Quotient > 1) {
            dividend = currentNumber/2
            return checkPowerOf2(dividend)
        }
        else{
            return false
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