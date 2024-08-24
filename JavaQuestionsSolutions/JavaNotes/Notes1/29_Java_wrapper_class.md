# Java Wrapper Classes

Wrapper classes provide a way to use primitive data type(int,boolean, etc..) as objects.  

Imagine you have a present that you want to give to your friend, but instead of   
just handing it to them directly, you decide to put it in a fancy gift box first.   
The gift box makes the present look nicer and also provides some extra protection.  


In Java, primitive data types like integers, floats, and characters are like the presents,   
and wrapper classes are like the gift boxes. Wrapper classes "wrap" around primitive data   
types and provide additional functionality and features.

For example, let's say you have an integer value.   
Instead of just using the integer directly, you can put it   
inside an Integer wrapper class. This wrapper class adds some   
extra methods and functionality that you can use with the integer   
value. It's like adding a fancy cover to your integer!

**So, in simple terms, a Java wrapper class is like a fancy box that wraps around   
primitive data types to provide extra features and functionality.**

The table below shows the primitive type and the equivalent wrapper class:

|Primitive Data type| Wrapper class|
|--------------------|-----------------|
|byte|Byte|
|short|Short|
|int|Integer|
|long|Long|
|float|Float|
|double|Double|
|boolean|Boolean|
|char|Character|

* Some times you must use wrapper classes, for example when working with Collection  
objects, such as `ArrayList`, where primitive types cannot be used (the list can only store objects):

`ArrayList<int> myNumbers = new ArrayList<int>(); // Invalid`


`ArrayList<Integer> myNumbers = new ArrayList<Integer>(); // Valid`

```
import java.util.ArrayList;

public class Main{
    public static void main(String[] args){
        ArrayList<Integer> myNumbers = new ArrayList<Integer>();
        myNumbers.add(10);
        myNumbers.add(15);
        myNumbers.add(20);
        myNumbers.add(25);

        for (int i:myNumbers){
            System.out.printlin(i);
        }
    }
}
```

## Creating Wrapper Objects
* To create a wrapper object, use the wrapper class instead of the primitive type.  
* To get the value, you can just print the object.

e.g. 
```
public class Main{
    public static void main(String[] args){
        Integer myInt = 5;
        Double myDouble = 5.99;
        Character myChar = 'A';
        System.out.println(myInt);
        System.out.println(myDouble);
        System.out.println(myChar);
    }
}
```

Since you're now working with objects, you can use certain methods to get 
information about the specific object.

For example, the following methods are used to get the value associated   
with the corresponding wrapper object: intValue(), byteValue(), shortValue(),   
longValue(), floatValue(), doubleValue(), charValue(), booleanValue().

This example will output the same result as the example above:

```
public class Main{
    public static void main(String[] args){
        Integer myInt = 5;
        Double myDouble = 5.99;
        Character myChar = 'A';
        System.out.println(myInt.intValue());
        System.out.println(myDouble.doubleValue());
        System.out.println(myChar.charValue());
    }
}
// Output
5
5.99
A
```
Another useful method is the toString() method, which is used to convert wrapper objects to strings.  

In the following example, we convert an `Integer` to a `String` , and use the `length()` method of the `String` class to output the length of the "string":

```
public class Main {
  public static void main(String[] args) {
    Integer myInt = 100;
    String myString = myInt.toString();
    System.out.println(myString.length());
  }
}
```