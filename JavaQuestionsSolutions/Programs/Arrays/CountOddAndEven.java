class Solution {
    public int[] countOddEven(int[] arr) {
        // Code here
        
        ArrayList<Integer> myFirstArrayList = new ArrayList<>();
        
        int evenCount = 0;
        int oddCount = 0;
        
        for(int i=0;i<=arr.length-1;i++){
            if(arr[i]%2==0){
                evenCount = evenCount +1;
            }
            else if(arr[i]%2!=0){
                oddCount = oddCount+1;
            }
            
        }
        // myFirstArrayList.add(oddCount);
        // myFirstArrayList.add(evenCount);
        
        // return myFirstArrayList;
        return new int[]{oddCount, evenCount};
    }
}