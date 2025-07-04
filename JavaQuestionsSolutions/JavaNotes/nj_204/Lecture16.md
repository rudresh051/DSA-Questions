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
