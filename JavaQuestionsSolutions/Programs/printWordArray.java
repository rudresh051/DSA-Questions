import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        String words = "One Two Three Four";
        String[] wordArray = words.split("\\s");
        
        // Print the word array
        System.out.println("Word Array: " + Arrays.toString(wordArray));
        
        // Print each word individually
        System.out.println("Individual Words:");
        for (String word : wordArray) {
            System.out.println(word);
        }
    }
}
