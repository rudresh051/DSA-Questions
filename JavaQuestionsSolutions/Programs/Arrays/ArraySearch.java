class Solution {
    public int search(int arr[], int x) {
        // code here
        int ans=0;
        
        for(int i=0; i<=arr.length-1;i++){
            // System.out.println("arr[i]" + arr[i]);
            if(arr[i]==x){
                ans = i;
                return ans;
            }
            
        }
        return -1;
    }
}


// Concept - how to use return statement. what's the difference between break and return
// scope of the variable in java as compared to javascript