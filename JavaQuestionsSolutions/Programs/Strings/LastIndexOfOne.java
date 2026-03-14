// User function Template for Java

class Solution {
    public int lastIndex(String s) {
        
        for(int i=s.length()-1;i>=0;i--){
            // System.out.println("s.charAt(i)" + " " + s.charAt(i));
            if(s.charAt(i)=='1'){
                // System.out.println("i" + i);
                return i;
            }
            else{
                continue;
            }
        }
        return -1;
        
    }
}