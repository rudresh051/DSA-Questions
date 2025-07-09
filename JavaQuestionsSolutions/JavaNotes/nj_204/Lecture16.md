# Var-args

In Java, **var-args** (short for **variable-length arguments**) is a feature that allows you to pass **zero or more arguments** of the **same type** to a method.

It is denoted using **three dots (`...`)** after the data type in the method parameter.


### ✅ Syntax:

```java
returnType methodName(dataType... variableName)
```

---

### ✅ Example:

```java
public class Example {
    static void printNumbers(int... numbers) {
        for (int num : numbers) {
            System.out.print(num + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        printNumbers();               // No arguments
        printNumbers(10);             // One argument
        printNumbers(1, 2, 3, 4, 5);  // Multiple arguments
    }
}
```

**Output:**

```
 
10 
1 2 3 4 5 
```

---

### 🔍 Key Points:

* Internally, the var-args parameter is treated as an **array**.
* Only **one var-args parameter** is allowed per method.
* It must be the **last parameter** in the method signature.

---

### ❌ Invalid Examples:

```java
// Error: Var-args must be last
void test(int... nums, String str) {}

// Error: Only one var-args allowed
void test(int... nums, String... names) {}
```

---

### ✅ Valid Combination:

```java
void test(String name, int... scores) {}
```

## Interface

An **Interface in Java** is defined as an abstract type used to specify the behaviour of a
class. An interface in Java is a blueprint of a class. A Java interface contains static
constants and abstract methods.
The interface in Java is a mechanism to achieve 100% **abstraction**. There can be only
abstract methods in the Java interface, not the method body. It is used to achieve
abstraction and multiple inheritance in Java. In other words, you can say that
interfaces can have abstract methods and variables. It cannot have a method body.


Java Interface also represents the IS-A relationship  
It cannot be instantiated just like the abstract class.  
Since Java 8, we can have default and static methods in an interface  

To declare an interface, use the interface keyword. It is used to provide total  
abstraction. That means all the methods in an interface are declared with an empty  
body and are public and all fields are public, static, and final by default. A class that  
implements an interface must implement all the methods declared in the interface. To  
implement an interface to a class we use implements keyword.

* Syntax

```java
interface InterfaceName{
// declare constant fields
// declare methods that is abstract by default.
}
```
### Example - 

```java
// Define an interface
interface Animal {
    void makeSound();        // abstract method
    void eat();              // another abstract method
}
```

```java
// Dog class implements Animal interface
class Dog implements Animal {
    @Override
    public void makeSound() {
        System.out.println("Dog barks: Woof! Woof!");
    }

    @Override
    public void eat() {
        System.out.println("Dog eats bones.");
    }
}
```

```java
public class Main {
    public static void main(String[] args) {
        Dog myDog = new Dog();
        myDog.makeSound();   // Output: Dog barks: Woof! Woof!
        myDog.eat();         // Output: Dog eats bones.
    }
}
```

* It is full unimplemented structure in java.
* Till jdk 1.7 interfaces use to contains only abstract methods and final variables.
* from jdk 1.8 we can place method with body also inside an interface.

X.java:

```java
package com.masai;

public interface X {

	public abstract void fun1();
	
	
}
```

```java
class A{

}
```
A.java
			          default constructor
>javac A.java-----------compiler------------A.class

>javac X.java -----java compiler----------> X.class

--.class file will be genereted for an interface also.
--constructor concept is not applicable with interface.

Note: inside an interface if we define any unimplemented method, that method is bydefault "public and abstract " whether we mention it or not.


--with the help of an interface we achive full abstraction.