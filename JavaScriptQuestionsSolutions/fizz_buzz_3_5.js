function fizzBuzz(num) {
  // Write code here
  for(var i=1;i<=num;i++){
      // console.log(i)
      
      if(i%5==0 && i%3==0){
          console.log("FizzBuzz")
          continue
      }
      else if(i%5==0){
          console.log("Buzz")
          continue
      }
      else if(i%3==0){
          console.log("Fizz")
          continue
      }
      else{
          console.log(i)
      }
  }
  
}