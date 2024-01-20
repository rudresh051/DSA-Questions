function runProgram(input) {
  // Write code here
//   console.log(input)
  input = input.split("\n")
//   console.log(input)
  size = input.shift()
//   console.log(input)
    input = input[0].split(" ").map(function(val){
        return parseInt(val)
    })
    // console.log(input)
  var arr1 = input
//   console.log(arr1)
    var swapCount = 0
  for(var i=0;i<arr1.length-1;i++)
  {
      var swapped = false; // Flag to check if any swaps were made during this iteration 
      for(var j=0;j<arr1.length-i-1;j++)
      {
          if(arr1[j] > arr1[j+1])
          {
              
            //   swap arr1[j],arr1[j+1]
            swapCount=swapCount+1
            var temp = arr1[j]
            arr1[j]=arr1[j+1]
            arr1[j+1]=temp
            swapped=true;
          }
      }
      if(!swapped){
        //   If no swaps were made, the array is already sorted, break out of the loop
          break;
      }
  }
//   arr1 now should be sorted in ascending order
// console.log("arr1",arr1)
  console.log(`Array is sorted in ${swapCount} swaps`)
  console.log(`First Element: ${arr1[0]}`)
  console.log(`Last Element: ${arr1[arr1.length-1]}`)
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