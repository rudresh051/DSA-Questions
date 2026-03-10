class Solution {
    public void rotate(int[] arr) {
        // code here
    
        // store the last element in a variable
        int lastElement = arr[arr.length-1];
        // System.out.println("lastElement" + lastElement);
        
        
        // assign every value by its predecessor
        for(int i=arr.length-1;i>0;i--){
            arr[i] = arr[i-1];
        }
        
        arr[0] = lastElement;
        
        // return arr;
        
    }
}

// Concept used - First assigning last element in a variable. And using for loop from last element but greater than
//  zero to modify the array
// Also you need to return anything as return type is void 