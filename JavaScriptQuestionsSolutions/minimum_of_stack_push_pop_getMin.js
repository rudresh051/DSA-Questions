function runProgram(input) {
  // Write code here
    // console.log(input)
    input1 = input.split("\n")
    // console.log("input1",input1)
    var arr1 = input1.shift()
    // console.log("input1",input1)
    var opsStack = []
    for(var i=0;i<=input1.length-1;i++){
        // console.log("input1[i]",input1[i])
        var temp = input1[i].split(" ")
        // console.log("temp[0]" + " " + temp[0] + " " + "temp[1]" + " " + temp[1])
        if(temp[0]=='push'){
            // console.log("push - parseInt(temp[1])", parseInt(temp[1]))
            opsStack.push(parseInt(temp[1]))
            // console.log("push-opsStack",opsStack)
        }
        else if(temp[0]=='pop'){
            var popLen = opsStack.length;
            // console.log("popLen",popLen)
            if(popLen!=0){
                // console.log("pop - parseInt(temp[1])", parseInt(temp[1]))
                opsStack.pop(parseInt(temp[1]))
            // console.log("pop-opsStack",opsStack)
            }
            else if(opsStack.length==0){
                continue
            }
            
        }
        else{
            // console.log("getMin",opsStack)
            var minLen = opsStack.length
            // console.log("minLen",minLen)
            if(minLen!=0){
            var minValue = Math.min(...opsStack)
            console.log(minValue)   
            }
            else if(opsStack.length==0){
                continue
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
