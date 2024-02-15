# Formatted Output in Java using printf()

## Formatting Using Java Printf()
printf() uses format specifiers for formatting. There are certain data types are mentioned below:

* For Number Formatting
* Formatting Decimal Numbers
* For Boolean Formatting
* For String Formatting
* For Char Formatting
* For Date and Time Formatting

### 1. For Number Formatting
The number itself includes Integer, Long, etc. The formatting Specifier used is %d.

e.g. 
```
// Java Program to demonstrate 
// Use of printf to 
// Formatting Integer 
import java.io.*; 
  
// Driver Class 
class GFG { 
      // main function 
    public static void main (String[] args) { 
        int a=10000; 
            
          //System.out.printf("%.d%n",a); 
          System.out.printf("%,d%n",a); 
    } 
} 

Output
10,000
```

