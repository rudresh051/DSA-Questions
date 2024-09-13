function runProgram(input) {
  input1  = input.split("\n")
//   console.log("input[0]",input1[0])
//   console.log("input[1]",input1[1])
  var arr1 = input1[0].split(".").map(function(value){
      return parseInt(value)
  })
//   console.log("arr1",arr1)
  var num1 = arr1.join("")
//   console.log("num1",num1)
//   console.log(typeof(num1))
  
  var arr2 = input1[1].split(".").map(function(value){
      return parseInt(value)
  })
//   console.log("arr2",arr2)
  var num2 = arr2.join("")
//   console.log("num2",num2)
//   console.log(typeof(num2))
  if(parseInt(num1)<parseInt(num2)){
      console.log("Version 1 is the latest.")
  }else{
      console.log("Version 2 is the latest.")
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
