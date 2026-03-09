class Solution {
    public ArrayList<Integer> getMinMax(int[] arr) {
        // code Here
        ArrayList<Integer> myList = new ArrayList<>();
        int max=arr[0];
        int min=arr[0];
        for(int i=1;i<=arr.length-1;i++){
            if(arr[i]>max){
                max = arr[i];
            }
            else{
                continue;
            }
        }
        for(int i=1;i<=arr.length-1;i++){
            if(arr[i]<min){
                min = arr[i];
            }
            else{
                continue;
            }
        }
        myList.add(min);
        myList.add(max);
        // System.out.println("min:" + min + " " + "max:" + max);
        return myList;
    }
}

// Concept used - ArrayList.
// Difference between Array and ArrayList
// add method - It is used to add number in a flexible array
// Question - can you initialize max = 1 and min = 1 ? why?
// can you do above using for-each loop?
// Remember - How to declare and syntax of ArrayList - It's very useful
