function checkPalindrome(N, str) {
  //write code here
  // console.log(N)
  // console.log(str)
  var str1 = str.join("")
  // console.log(str1,str)
  var arr1 = []
  var len = str.length-1
  // console.log(len)
  
  for(var i=str.length-1;i>=0;i--){
      // console.log(str[i])
      arr1.push(str[i])
  }
  // console.log(arr1)
  var str2 = arr1.join("")
  // console.log(str2)
  if(str1==str2){
      console.log("Yes")
  }
  else{
      console.log("No")
  }
}