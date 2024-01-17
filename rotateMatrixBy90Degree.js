function rotateBy90Clockwise(N, matrix){
  //write code here
  // console.log(N)
  // console.log(matrix)
  
  for(var layer=0;layer<Math.floor(N/2);layer++){
      for(var i=layer;i<=N-1-layer;i++){
          var temp = matrix[layer][i]
          matrix[layer][i] = matrix[N-1-i][layer]
          matrix[N-1-i][layer] = matrix[N-1-i][N-1-i]
          matrix[N-1-layer][N-1-i] = matrix[i][N-1-layer]
          matrix[i][N-1-layer] = temp
      }
  }
  
  console.log(matrix)

}
