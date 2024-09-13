function runProgram(input) {
    input1  = input.split("\n")
    console.log("input[0]",input1[0])
    console.log("input[1]",input1[1])
    if(input1[0]<input1[1]){
        console.log("Version 1 is the latest")
    }else{
        console.log("Version 2 is the latest")
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