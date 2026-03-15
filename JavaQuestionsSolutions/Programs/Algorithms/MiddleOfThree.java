// User function Template for Java

class Solution {
    int middle(int a, int b, int c) {
        // code here
    
        
        if((a>b && a<c)|| (a>c && a<b)){
            // System.out.println("test");
            return a;
        }
        else if((b>a && b<c)||(b>c && b<a)){
            return b;
        }
        else{
            return c;
        }
        
    }
}

// Check for few cases and also try to get answer first with pen-paper