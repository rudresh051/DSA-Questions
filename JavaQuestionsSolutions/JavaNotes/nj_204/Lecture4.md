# lectures - 29948

```java
package org.sdet;

public class Blueprint {
    // This is where execution starts
    public static void main(String[] args){
        
        /*
        Naming - Pascal
        For class name , For interface name
        e.g. MyClassName, MyInterfaceName

        Camelcase
        myVariableName
        myMethodName

        Invalid
        #myname
        1myVariable
        my-variable
         */
    }
}

```

## Java Language Fundamentals

1. Identifiers
2. Literals
3. Keywords/Reserved words
4. Operators

## Identifiers

The identifier is a name assigned to the programming elements like variables, methods,
classes, abstract classes, interfaces etc.

```java
int age = 25; int height; // default to be 0
height = 67;

here
int : data type
age : variable [identifier]
= : operator (assingment)
25 : value/constant [literal]
; : terminator
```

Note - To Provide identifiers in java programming, we have to use the following rules and regulations -

Identifiers should not be started with any number, identifiers may be started with an alphabet, '_'
symbol, '$' symbol, but, the subsequent symbols may be a number, an alphabet, '_' symbol, '$' symbol.

```java
// camelCase(recommendation, convention) = thisIsMe => variable names, Method names

// PascalCase = ThisIsMe => classes, interfaces, abstract classes

Identifiers are not allowing spaces in the middle.

ex : 
int employeeNumber = 111; //valid
String #address = "Pune"; // Invalid
String employee-Address = "Hyderabad"; //Invalid
getInputStream();//valid
get Input Stream(); // Invalid

In java applications, it is suggestible to provide identifiers with a particular meaning.
```

## Literals

Literal is a constant/value assigned to the variable.

To prepare java programs, JAVA has provided the following set of literal :

1. Integer/Integral Literals -
byte, short, int, long - 10, 20, 30, ....
char - 'A', 'B', ...

2. Floating Point Literals -
float - 10.22f, 23.345f, ...
double - 11.123, 456.345, ...

3. Boolean Literals -
boolean - true, false

4. String Literals -
String - "Welcome", "Hello", ....

## Keywords/Reserved Words

Keywords in Java convey a special meaning to the compiler therefore, these cannot be used as
identifiers.
Among the list of keywords list mentioned below the keywords goto and const are currently not in use.
They are reserved words (for future use)..

![alt text](image-1.png)

## Operators

An operator is a symbol, it will perform a particular operation over the provided operands.
To prepare java applications, JAVA has provided the following list of operators.

1. Arithmetic Operators
+, - , * ,/ , %, ++, --

2. Assignment Operators
=, +=, -=, *=, /=, %=

3. Comparison Operators
==, !=, < , >, <=, >=

4. Boolean Logical Operators
5. Bitwise Logical Operators
6. Short-Circuit Operators
7. Ternary Operator

Example1 -

```java
package com.masai;
public class Main{
    public static void main(String[] args){
        int a=10;
        System.out.println(a); //10
        System.out.println(a++);//10 //post-increment => (print, increase)
        System.out.println(++a);//12
        System.out.println(a--);//12
        System.out.println(--a);//10
        System.out.println(a);//10
    }
}
```

Outpus -
10
10
12
12
10
10

### Example 2

```java
package com.masai;
public class Main{
public static void main(String[] args){
int a=5;
System.out.println(++a - ++a);
}
}

// output = -1
```

### Example 3

```java
package com.masai;
public class Main{
public static void main(String[] args){
int a=5;
System.out.println((--a+--a)*(++a-a--)+(--a+a--)*(++a+a++));
}
}
```
output - 16
explanation - (4+3)*(4-4)+(2+2)*(2+2)

Example - Boolean Logical Operator

This operator can also be applied the boolean value as well as an integer.

![alt text](image-2.png)


### Example 4 - 

```java
package com.masai;
public class Main{
public static void main(String[] args{
boolean b1=true;
boolean b2=false;
System.out.println(b1&b1);//true
System.out.println(b1&b2);//false
System.out.println(b2&b1);//false
System.out.println(b2&b2);//false
System.out.println(b1|b1);//true
System.out.println(b1|b2);//true
System.out.println(b2|b1);//true
System.out.println(b2|b2);//false
System.out.println(b1^b1);//false
System.out.println(b1^b2);//true
System.out.println(b2^b1);//true
System.out.println(b2^b2);//false
}
```

### Example 5 - 

```java
package com.masai;
public class Main{
    public static void main(String[] args){
    int a=10;
    int b=2;
    System.out.println(a&b);
    System.out.println(a|b);
    System.out.println(a^b);
    System.out.println(a<<b);
    System.out.println(a>>b);
    }
}
```

### Example 6

```java
int a=10;// 1010
int b=2;// 0010
a&b--->10&2--> 0010-----> 2
a|b--->10|2--> 1010-----> 10
a^b--->10^2--> 1000-----> 8
a<<b ---> 10<<2 -----> 00001010
00101000---> 40
--> Remove 2 symbols at left side and append 2 0's at right side.
a>>b ---> 10>>2 -----> 00001010
00000010
--> Remove 2 symbols at right side and append 2 0's at left side.
Note: Removable Symbols may be o's and 1's but appendable symbols must be 0's.
```

Example - Short-Circuit Operators
The main intention of Short-Circuit operators is to improve java applications performance.
&&  
||  
| vs ||

In the case of Logical-OR operator, if the first operand value is true then it is not required
to check second operand value, directly, we can predict the result of overall expression is
true.
In the case of '|' operator, even first operand value is true , still, JVM evaluates second
operand value then only JVM will get the result of overall expression is true, here
evaluating second operand value is unnecessary, it will increase execution time and it will
reduce application performance.
In the case of '||' operator, if the first operand value is true then JVM will get the overall
expression result is true with out evaluating second operand value, here JVM is not
evaluating second operand expression unnecessarily, it will reduce execution time and it
will improve application performance.
Note: If the first operand value is false then it is mandatory for JVM to evaluate second
operand value in order to get overall expression result.

Example - 

```java
package com.masai;
public class Main{
    public static void main(String[] args {
        int a=10;
        int b=10;
        if( (a++ == 10) | (b++ == 10) )
        {
            System.out.println(a+" "+b);//OUTPUT: 11 11
        }
        int c=10;
        int d=10;
        if( (c++ == 10) || (d++ == 10) )
        {
        System.out.println(c+" "+d);//OUTPUT: 11 10
        }
    }
}
```

& vs && 

In the case of Logical-AND operator, if the first operand value is false then it is not
required to check second operand value, directly, we can predict the result of overall
expression is false.
In the case of '&' operator, even first operand value is false , still, JVM evaluates second
operand value then only JVM will get the result of overall expression is false, here
evaluating second operand value is unnecessary, it will increase execution time and it will
reduce application performance.
In the case of '&&' operator, if the first operand value is false then JVM will get the overall
expression result is false with out evaluating second operand value, here JVM is no evaluating second
operand expression unnecessarily, it will reduce execution time and it
will improve application performance.
Note: If the first operand value is true then it is mandatory for JVM to evaluate second
operand value in order to get overall expression result.

Data Types:
Java is strictly a typed programming language, where in java applications before
representing data first we have to confirm which type of data we representing. In this
context, to represent type of data we have to use "data types".
In java applications , data types are able to provide the following advantages.
1. We are able to identify memory sizes to store data.
example :
 int i=10;--> int will provide 4 bytes of memory to store 10 value.
2. We are able to identify range values to the variable to assign.
example:
byte b=130;---> Invalid
byte b=125;---> Valid

Reason: 'byte' data type is providing a particular range for its variables like -128 to 127, in
this range only we have to assign values to byte variables.

To prepare java applications, JAVA has provided the following data types.

A. Primitive Data types :
1. Numeric Data Types
a. Integral data types/ Integer Data types:
byte ------> 1 bytes ----> 0
short------> 2 bytes-----> 0
int--------> 4 bytes-----> 0
long-------> 8 bytes-----> 0