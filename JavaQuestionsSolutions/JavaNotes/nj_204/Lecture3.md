# Java Language Fundamentals

Java Naming Convention, coding standard.
* java is a case sensetive programming language, we use diff conventions for naming our classes, methods and variables.  
* All class names, abstract class names, interface names and Enum, names should follow **"PascalNamingConvention"**,  
which means, the first letter of every word should be in upper case
    * Example: String, ArrayList, InputStreamReaderIStringBuffer,Student, Employee,etc
* All Java variables, method names should follow **camelNamingConvention**, which means the first letter should be in  
lowercase and the subsequent word should start with Uppercase

Example (variables): in, studentName, pageContext  
Example (methods): concat(), forName(), getInputStream(), calculatelnterest()  
* All java **Constant variables** must be provided in Upper Case letters.  
(constant variables are the variables, whose values are fixed throughout the program)  
Example: MIN_PRIORITY, MAX_PRIORITY, NORM_PRIORITY

* Java programming language belongs to c family programming language, i.e. most of basic programming constructs of  
Java are similar to the c language with some minor changes


like :- operators, if-else, loops switch case, etc.

## Data Types
before representing the data , first we have to confirm type of the data, by using data types
in java there are 2 types of data types:-
l.primitive data types
2.user-defined data types

primitive data types:-
java supports total 8 primitive data types under 4 category:-
1. Integers:-
    * byte :- 8bit / 1 byte // 0 :- 127 to -128
    * Short - 16bit/2 byte // 0
    * int - 32 bit/4 byte// 0
    * long - 64 bit/8 byte// 0

2. Real numbers - 
    * float - 32 bit / 4 byte //0.0
    * double - 64 bit / 8 byte // 0.0

3. Character
    * char - 16bit or 2 byte(Unicode ) // ''

4. Boolean
    * 1 bit // true/false // false

*  Note - Any number with decimal point will be considered as double in java, not a float.

* Any non-decimal point digit is treated as int by default in java

## Type Casting
The procedure of converting one data type into its equivallent another data type is known as typecasting.

Note:- we can not typecast any datatype to any other data type, we can typecast only equivallent /compatible types.

--we have 2 types of typecasting:-
l.implicit typecasting :- (upcasting/ widening)
--smaller datatype value into the bigger data type ex:- from int to long

int x=10;
long y=x;