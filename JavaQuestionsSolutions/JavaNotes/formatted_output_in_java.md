# Formatted Output in Java using printf()
**Syntax**  
1. An optional method to control, format, and display text to the console window  
2. two arguments = format string + (object/variable/value)
3. % [flags] [precision] [width] [conversion-character]


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
### For Decimal Number Formatting
Decimal Number Formatting can be done using print() and format specifier %f .

e.g. 
```
// Java Programs to demonstrate 
// Use of Printf() for decimal 
// Number Formatting 
import java.io.*; 

// Driver Class 
class GFG { 
	// main function 
	public static void main(String[] args) 
	{ 
		// declaring double 
		double a = 3.14159265359; 

		// Printing Double Value with 
		// different Formatting 
		System.out.printf("%f\n", a); 
		System.out.printf("%5.3f\n", a); 
		System.out.printf("%5.2f\n", a); 
	} 
}

Output
3.141593
3.142
 3.14

```
### For Boolean Formatting
Boolean Formatting can be done using printf and ( ‘%b’ or ‘%B’ ) depending upon the result needed.  

e.g.  
```
// Java Programs to demonstrate 
// Use of Printf() for decimal 
// Boolean Formatting 
import java.io.*; 

// Driver Function 
class GFG { 
	// main function 
	public static void main(String[] args) 
	{ 
		int a = 10; 
		Boolean b = true, c = false; 
		Integer d = null; 

		// Fromatting Done using printf 
		System.out.printf("%b\n", a); 
		System.out.printf("%B\n", b); 
		System.out.printf("%b\n", c); 
		System.out.printf("%B\n", d); 
	} 
}

```