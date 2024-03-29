# Data types are divided into two groups:

Primitive data types - includes byte, short, int, long, float, double, boolean and char  
Non-primitive data types - such as String, Arrays and Classes 

## Primitive Data Types

A primitive data type specifies the size and type of variable values, and it has no additional methods.

There are eight primitive data types in Java:
| Data Type | Size    | Description                                                      |
|-----------|---------|------------------------------------------------------------------|
| byte      | 1 byte  | Stores whole numbers from -128 to 127                            |
| short     | 2 bytes | Stores whole numbers from -32,768 to 32,767                      |
| int       | 4 bytes | Stores whole numbers from -2,147,483,648 to 2,147,483,647        |
| long      | 8 bytes | Stores whole numbers from -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807 |
| float     | 4 bytes | Stores fractional numbers. Sufficient for storing 6 to 7 decimal digits |
| double    | 8 bytes | Stores fractional numbers. Sufficient for storing 15 decimal digits |
| boolean   | 1 bit   | Stores true or false values                                      |
| char      | 2 bytes | Stores a single character/letter or ASCII values                 |

### Java Numbers
**Integer types** stores whole numbers, positive or negative (such as 123 or -456), without decimals.   
Valid types are byte, short, int and long. Which type you should use, depends on the numeric value.

**Floating point** types represents numbers with a fractional part, containing one or more decimals.   
There are two types: float and double.

### Integer Types
#### Byte
The byte data type can store whole numbers from -128 to 127.   
This can be used instead of int or other integer types to save memory   
when you are certain that the value will be within -128 and 127:

`byte myNum = 100;`  

#### Short
The short data type can store whole numbers from -32768 to 32767:  
`short myNum = 5000;
`
#### Int
The int data type can store whole numbers from -2147483648 to 2147483647  
`int myNum = 100000;`

#### Long
The long data type can store whole numbers from -9223372036854775808 to 9223372036854775807  
`long myNum = 15000000000L;`

### Floating Types
Floating type should be used when we need decimal numbers
The float and double data types can store fractional numbers.  
Note that you should end the value with an "f" for floats and "d" for doubles:  
`float myNum = 5.75f;`  
`double myNum = 19.99d;`

**Scientific Numbers**
A floating point number can also be a scientific number with an "e" to indicate the power of 10:  
```
float f1 = 35e3f;
double d1 = 12E4d;
```  

## Java Boolean Data Types
Java has a boolean data type, which can only take the values true or false:
```
boolean isJavaFun = true;
boolean isFishTasty = false;
```  
### Java Characters
The char data type is used to store a single character.   
The character must be surrounded by single quotes, like 'A' or 'c':

`char myGrade = 'B';`

`char myVar1 = 65, myVar2 = 66, myVar3 = 67;`  

### Java Strings
The String data type is used to store a sequence of characters (text).  
String values must be surrounded by double quotes:  
`String greeting = "Hello World";`

# Non Primitive Data types
Non-primitive data types are called reference types because they refer to objects.

The main difference between primitive and non-primitive data types are:

* Primitive types are predefined (already defined) in Java.  
 Non-primitive types are created by the programmer and is not defined by Java (except for String).
* Non-primitive types can be used to call methods to perform certain operations, while primitive types cannot.
* A primitive type has always a value, while non-primitive types can be null.
* A primitive type starts with a lowercase letter, while non-primitive types starts with an uppercase letter.

Examples of non-primitive types are Strings, Arrays, Classes, Interface,