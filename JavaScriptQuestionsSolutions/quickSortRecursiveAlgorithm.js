function runProgram(input) {
  // Write code here
//   console.log(input)
  input = input.split("\n")
//   console.log(input)
  var arr = input[1].split(" ").map(function(val){
      return parseInt(val)
  })
//   console.log(arr)
  var n = arr.length
  
  function quickSort(arr,low,high){
      if(low<high){
          var pivotIndex = partition(arr,low,high)
          quickSort(arr,low,pivotIndex-1)
          quickSort(arr,pivotIndex+1,high)
      }
  }
  function partition(arr,low,high){
      var pivot = arr[high]
      var i=low-1
      for(var j=low;j<high;j++){
          if(arr[j]<pivot){
              i++
              swap(arr,i,j)
          }
      }
      swap(arr,i+1,high)
      return i+1
  }
  function swap(arr,i,j){
      var temp = arr[i]
      arr[i]=arr[j]
      arr[j]=temp
  }
  quickSort(arr,0,arr.length-1)
  console.log(arr.join(" "))
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