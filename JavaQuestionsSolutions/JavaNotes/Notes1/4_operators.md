Java divides the operators into the following groups:

* Arithmetic operators => `+, -, *, /, %, ++, --`
* Assignment operators
    * It is used to assign values to variable
    * e.g. `=, +=, -=, *=, /=, %=, &=, |=, ^=, >>=, <<=`
* Comparison operators
    * Comparison operators are used to compare two values (or variables)  
    * The return value of a comparison is either **true** or **false**
    * e.g. `==, !=, >, <, >=, <=`
* Logical operators
    * You can also test for true or false values with logical operators.
    * e.g. `&&, ||, !`
* Bitwise operators
    * Bitwise operators are used to performing the manipulation of individual bits of a number. 
    * They can be used with any integral type (char, short, int, etc.). 
    * They are used when performing update and query operations of the Binary indexed trees.
    * e.g. Bitwise OR(|), Bitwise AND(&), Bitwise XOR(^), Bitwise complement(~) 
    
```
a = 5 = 0101 (In Binary)
b = 7 = 0111 (In Binary)

Bitwise OR Operation of 5 and 7
  0101
| 0111
 ________
  0111  = 7 (In decimal) 
```  
```
// Java program to illustrate
// bitwise operators

public class operators {
	public static void main(String[] args)
	{
		// Initial values
		int a = 5;
		int b = 7;

		// bitwise and
		// 0101 & 0111=0101 = 5
		System.out.println("a&b = " + (a & b));

		// bitwise or
		// 0101 | 0111=0111 = 7
		System.out.println("a|b = " + (a | b));

		// bitwise xor
		// 0101 ^ 0111=0010 = 2
		System.out.println("a^b = " + (a ^ b));

		// bitwise not
		// ~00000000 00000000 00000000 00000101=11111111 11111111 11111111 11111010
		// will give 2's complement (32 bit) of 5 = -6
		System.out.println("~a = " + ~a);

		// can also be combined with
		// assignment operator to provide shorthand
		// assignment
		// a=a&b
		a &= b;
		System.out.println("a= " + a);
	}
}

```  
**Output**
```
a&b = 5
a|b = 7
a^b = 2
~a = -6
a= 5
```

