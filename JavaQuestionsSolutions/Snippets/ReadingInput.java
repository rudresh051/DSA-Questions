import java.util.*;
import java.util.Scanner;

public class ReadingInput {

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("Hello... please give input: ");
        int x = sc.nextInt();
        int y = sc.nextInt();
        System.out.println("input is: " + x);
//        int y = sc.nextInt();
        System.out.println("input is: " + y);

        sc.close();
    }
}
