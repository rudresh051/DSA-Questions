# Java User Input (Scanner)

1. The **Scanner** class is used to get user input, and it is found in the  
in the **java.util** package.
2. To use the `Scanner` class, create an object of the class and use any of the available methods found in the `Scanner` class documentation. 
3. In our example, we will use the nextLine() method, which is used to read Strings.

import java.util.Scanner;

class Main{
    public static void main(String[] args){
        Scanner myObj = new Scanner(System.in);
        String userName;
        
        // Enter username and press Enter
        System.out.println("Enter username"); 
        userName = myObj.nextLine();   
        
        System.out.println("Username is: " + userName);  
    }
}

## Input Types
1. nextBoolean()
2. nextByte()
3. nextDouble()
4. nextFloat()
5. nextInt()
6. nextLine()
7. nextLong()
8. nextShort()

