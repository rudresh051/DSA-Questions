// User function Template for Java

class Solution {
    public static String reverseString(String s) {
        // code here
        
            String temp="";
        
            for(int i=s.length()-1;i>=0;i--){
                // System.out.println(s.charAt(i));
                temp = temp+s.charAt(i);
            }
        
            // System.out.println(temp);

            
            return temp;
    }
}