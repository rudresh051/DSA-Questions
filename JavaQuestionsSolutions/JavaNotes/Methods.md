# Java Methods

A method is a block of code which only runs when it is called.

You can pass data, known as parameters, into a method.

Methods are used to perform certain actions, and **they are also known as functions**.

Why use methods? To reuse code: define the code once, and use it many times.

## Create a Method
e.g.
```
public class Main {
  static void myMethod() {
    // code to be executed
  }
}
```  
* A method must be declared within a class. 
* It is defined with the name of the method, followed by parentheses ()
* `myMethod()` is the name of the method
* `static` means that the method belongs to the Main class and not an object of the Main class
* `void` means that this method does not have a return value.

## Call a Method

* To call a method in Java, write the method's name followed  
by two parentheses () and a semicolon;  

e.g. Inside main, call the myMethod() method:

```
public class Main {
  static void myMethod() {
    System.out.println("I just got executed!");
  }

  public static void main(String[] args) {
    myMethod();
  }
}

Output
I just got executed!
```
* A method can also be called multiple times:
```
public class Main {
  static void myMethod() {
    System.out.println("I just got executed!");
  }

  public static void main(String[] args) {
    myMethod();
    myMethod();
    myMethod();
  }
}
```


