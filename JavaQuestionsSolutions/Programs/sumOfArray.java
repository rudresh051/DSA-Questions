public class Main{
    public static void main (String[] args) {
        
        // decalaring and assigning values to the array
        int[] myArray = {1,5,10,25};
        int sum = 0;
        
        for (int i=0;i<=myArray.length-1;i++){
            sum = sum + myArray[i];
        }
        
        System.out.println(sum);
    }
}