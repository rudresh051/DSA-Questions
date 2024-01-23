function runProgram(input) {
  // Write code here
    // console.log(input)
    input1 = input.split("\n")
    // console.log("input1",input1)
    var arr1 = input1.shift()
    // console.log("input1",input1)
    var opsStack = []
    var minStack = []
    
    for(var i=0;i<=input1.length-1;i++){
        var temp = input1[i].split(" ")
        if(temp[0]=='push'){
            var val = parseInt(temp[1])
            opsStack.push(val)
            
            if(minStack.length===0 || val <= minStack[minStack.length-1]){
                minStack.push(val)
            }
        }
        else if(temp[0]=='pop'){
            if(opsStack.length > 0){
                var popped = opsStack.pop()
                if(popped === minStack[minStack.length-1]){
                    minStack.pop();
                }
            }
            else if(opsStack.length==0){
                continue
            }
            
        }
        else{
            // var minLen = opsStack.length
            // if(minLen!=0){
            // var minValue = Math.min(...opsStack)
            // console.log(minValue)
            // }
            // else if(opsStack.length==0){
            //     continue
            if(minStack.length > 0){
                console.log(minStack[minStack.length-1])
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
