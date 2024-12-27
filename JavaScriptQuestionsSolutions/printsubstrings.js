var input = "thisracecarisgood"

function runProgram(input) {
  console.log(input.length)
  var substrings = []
//   Outerloop for starting index
  for(var i=0;i<=input.length-1;i++){
    //   inner loop for ending index
    for(var j=i+1;j<=input.length-1;j++){
        substrings.push(input.substring(i,j))
    }
  }
  console.log(substrings)
}

runProgram(input)