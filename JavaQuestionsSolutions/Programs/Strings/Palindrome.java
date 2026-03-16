class Solution {
    boolean isPalindrome(String s) {
        // code here
        
        String s1 = "";
        
        for(int i=s.length()-1;i>=0;i--){
            // System.out.println(s.charAt(i));
            s1 = s1+s.charAt(i);
        }
        
        
        // if(s1.contentEquals(s)){
        //     return true;
        // }
        // else{
        //     return false;
        // }
        return s1.equals(s);
        
    }
}

/* 

StringBuilder s1 = new StringBuilder();

        for(int i = s.length()-1; i >= 0; i--){
            s1.append(s.charAt(i));
        }

        return s1.toString().equals(s);
*/
// Learn about String builder and methods in it