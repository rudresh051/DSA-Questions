# Java Exceptions

When executing Java code, different errors can occur: coding errors made by the   
programmer, errors due to wrong input, or other unforeseeable things.  

When an error occurs, Java will normally stop and generate an error message.   
The technical term for this is: Java will throw an exception (throw an error).

```
Explain Java Exception from a non technical person POV - 

Imagine you're cooking your favorite dish in the kitchen. 
You've got all your ingredients laid out and you're following the recipe step by step.
 Suddenly, you realize you're out of one crucial ingredient, like salt. Without salt, 
 your dish won't taste quite right, and you might have to stop cooking until you can get more.

In Java, an exception is kind of like running into a problem while you're cooking. 
It's like discovering you're missing an ingredient or accidentally adding too much of something. 
When your Java program is running and it encounters an exception, it means something unexpected 
has happened that stops the program from working properly.

Just like in cooking, when you hit an exception in Java, you need to handle it. Handling an 
exception is like finding a workaround for the missing ingredient or adjusting your recipe 
to fix the mistake. You can write special code in your Java program to deal with exceptions 
when they occur, so your program can keep running smoothly even if something unexpected happens.

So, in simple terms, a Java exception is like hitting a bump in the road while you're running 
your program, and handling it is like finding a way to keep going despite the problem.
```

## Java try and catch
1. The `try` statement allows you to define a block of code to be tested for error while it is being executed.
2. The `catch` statement allows you to define a block of code to be executed, if  
an error occurs in the try block
3. The `try` and `catch` keywords come in pairs

**Syntax** 
```
try {
  //  Block of code to try
}
catch(Exception e) {
  //  Block of code to handle errors
}
``` 
e.g. 

```
public class Main {
  public static void main(String[] args) {
    int[] myNumbers = {1, 2, 3};
    System.out.println(myNumbers[10]);
  }
}

// output
Exception in thread "main" java.lang.ArrayIndexOutOfBoundsException: 10
        at MyClass.main(MyClass.java:4)
```
If an error occurs , we can use try...catch to catch the error and execute some  
code to handle it.  

```
public class Main {
  public static void main(String[ ] args) {
    try {
      int[] myNumbers = {1, 2, 3};
      System.out.println(myNumbers[10]);
    } catch (Exception e) {
      System.out.println("Something went wrong.");
    }
  }
}
```

# Finally 
The **finally** statements lets you execute code, after **try...catch**, regardless of the result.

e.g.  
```
public class Main{
  public static void main(String[] args){
    try{
      int[] myNumbers = {1,2,3};
      System.out.println(myNumbers[10]);
    }
    catch(Exception e){
      System.out.println("Something went wrong.");
    }finally{
      System.out.println("The 'try catch' is finished");
    }
  }
}

output 
Something went wrong.
The 'try catch' is finished.
```