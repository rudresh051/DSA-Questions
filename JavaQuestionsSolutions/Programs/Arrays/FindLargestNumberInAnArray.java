class Solution {
    public static int largest(int[] arr) {
        // code here
        int max = arr[0];
        // System.out.println("arr[0]" + arr[0]);
        
        for(int i =0; i<=arr.length-1;i++){
            // System.out.println("arr[i]" + arr[i]);
            if(arr[i]>max){
                max = arr[i];
            }
        }
        return max;
    }
}


// Concepts - Looping through an array, How to update the value