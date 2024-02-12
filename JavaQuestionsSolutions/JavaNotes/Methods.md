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

# Java Method Parameters
* Information can be passed to methods as parameter.
* Parameters act as variables inside the method.
e.g. 
```
public class Main {
  static void myMethod(String fname) {
    System.out.println(fname + " Refsnes");
  }

  public static void main(String[] args) {
    myMethod("Liam");
    myMethod("Jenny");
    myMethod("Anja");
  }
}
// Liam Refsnes
// Jenny Refsnes
// Anja Refsnes
```

* When a parameter is passed to the method, it is called an argument. So, from the example above: fname is a parameter, while Liam, Jenny and Anja are arguments.

### Multiple Parameters
e.g. 
```
public class Main {
  static void myMethod(String fname, int age) {
    System.out.println(fname + " is " + age);
  }

  public static void main(String[] args) {
    myMethod("Liam", 5);
    myMethod("Jenny", 8);
    myMethod("Anja", 31);
  }
}

// Liam is 5
// Jenny is 8
// Anja is 31
```

## Return Values
* The `void` keyword indicates that the method should  
not return a value.
* If you want the method to return a value, you can use a primitive data type  
 (such as int, char, etc.) instead of void, and use the return keyword inside the method:

e.g. 
```
public class Main {
  static int myMethod(int x) {
    return 5 + x;
  }

  public static void main(String[] args) {
    System.out.println(myMethod(3));
  }
}
// Outputs 8 (5 + 3)
```
e.g. 
```
public class Main {
  static int myMethod(int x, int y) {
    return x + y;
  }

  public static void main(String[] args) {
    System.out.println(myMethod(5, 3));
  }
}
// Outputs 8 (5 + 3)
```

* You can also store the result in a variable(recommended)
```
public class Main {
  static int myMethod(int x, int y) {
    return x + y;
  }

  public static void main(String[] args) {
    int z = myMethod(5, 3);
    System.out.println(z);
  }
}
// Outputs 8 (5 + 3)
```

e.g. If...else inside a method
```
public class Main {

  // Create a checkAge() method with an integer parameter called age
  static void checkAge(int age) {

    // If age is less than 18, print "access denied"
    if (age < 18) {
      System.out.println("Access denied - You are not old enough!"); 
      
    // If age is greater than, or equal to, 18, print "access granted"
    } else {
      System.out.println("Access granted - You are old enough!"); 
    }
    
  } 

  public static void main(String[] args) { 
    checkAge(20); // Call the checkAge method and pass along an age of 20
  } 
}

```

# Method overloading
With method overloading, multiple methods can have the same name with different parameters:
```
int myMethod(int x)
float myMethod(float x)
double myMethod(double x, double y)
```

e.g. It has two methods that add numbers of different type 
```
public class Main {
  static int plusMethodInt(int x, int y) {
    return x + y;
  }
  
  static double plusMethodDouble(double x, double y) {
    return x + y;
  }
  
  public static void main(String[] args) {
    int myNum1 = plusMethodInt(8, 5);
    double myNum2 = plusMethodDouble(4.3, 6.26);
    System.out.println("int: " + myNum1);
    System.out.println("double: " + myNum2);
  }
}

```

Instead of defining two methods that should do the same thing, it is better to overload one.

In the example below, we overload the plusMethod method to work for both int and double:

```
public class Main {
  static int plusMethod(int x, int y) {
    return x + y;
  }
  
  static double plusMethod(double x, double y) {
    return x + y;
  }
  
  public static void main(String[] args) {
    int myNum1 = plusMethod(8, 5);
    double myNum2 = plusMethod(4.3, 6.26);
    System.out.println("int: " + myNum1);
    System.out.println("double: " + myNum2);
  }
}

```