function vowelAndConsonantCount(N, str) {
    let vowels = "aeiouAEIOU";
  
  let vowelCount = 0;
  let consonantCount = 0;
  
  for (let i = 0; i < N; i++) {
      let char = str[i];
      
      if (vowels.includes(char)) {
          vowelCount++;
      } else if (char.match(/[a-zA-Z]/)) {
          consonantCount++;
      }
  }
  console.log(vowelCount, consonantCount)
    
  }
  