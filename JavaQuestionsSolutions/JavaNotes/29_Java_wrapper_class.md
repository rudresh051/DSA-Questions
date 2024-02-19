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