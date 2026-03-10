//Given an integer k and array arr. Your task is to return the position of the first occurrence of k in the given array and 
// if element k is not present in the array then return -1.

// User function Template for Java
class Solution {
    public int search(int k, ArrayList<Integer> arr) {
        // code here
        for( int i=0;i<=arr.size()-1;i++){
            if(arr.get(i)==k){
                return i+1;
            }
            else{
                continue;
            }
        }
        return -1;
    }
}