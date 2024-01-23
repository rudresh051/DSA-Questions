function anagramDetector(S1,S2){
  var S1SplitWithSpace = S1.split(" ")
  // console.log(S1SplitWithSpace)
  var S1JoinWithoutSpace = S1SplitWithSpace.join("")
  // console.log(S1JoinWithoutSpace)
  var S1WithCommaSeparated = S1JoinWithoutSpace.split("").sort()
  // console.log(S1WithCommaSeparated)
  
  var S2SplitWithSpace = S2.split(" ")
  var S2JoinWithoutSpace = S2SplitWithSpace.join("")
  var S2WithCommaSeparated = S2JoinWithoutSpace.split("").sort()
  // console.log(S2WithCommaSeparated)
  

  var object1 = {}
  for (var i in S1WithCommaSeparated){
      object1[i]=S1WithCommaSeparated[i]
  }
  // console.log(object1)
  
  var object2 = {}
  for (var i in S2WithCommaSeparated){
      object2[i]=S2WithCommaSeparated[i]
  }
  // console.log(object2)
  
  var countObject1 = {}
  for (var key in object1){
      var character = object1[key]
      if(countObject1[character]){
          countObject1[character]++
      }
      else{
          countObject1[character]=1
      }
  }
  // console.log(countObject1)
  
  var countObject2 = {}
  for (var i in object2){
      var character = object2[i]
      if(countObject2[character]){
          countObject2[character]++
      }
      else{
          countObject2[character]=1
      }
  }
  // console.log(countObject2)
  var a = JSON.stringify(object1)
  var b = JSON.stringify(object2)
  if(a==b){
      console.log('True')
  }
  else{
      console.log('False')
  }
}
// Topics - JavaScript Object, Object Methods,looping in Object, If-else, JSON Stringify Method
