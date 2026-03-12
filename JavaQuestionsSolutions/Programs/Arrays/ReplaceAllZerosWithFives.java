class Solution {
    int convertfive(int num) {
        // Your code here
        
        // converting number to string
        StringBuffer s = new StringBuffer(String.valueOf(num));
        
        for(int i=0;i<=s.length()-1;i++){
            if(s.charAt(i)=='0'){
                s.setCharAt(i,'5');
            }
            else{
                continue;
            }
        }
        // converting string to integer
        num = Integer.parseInt(String.valueOf(s));
        return num; 
        
    }
}

// Try above problem without converting into string
// hint - use modulos operator