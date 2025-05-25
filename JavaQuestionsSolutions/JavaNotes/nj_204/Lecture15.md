# Abstract Class

--abstract method is also called as unimplemented method.
--normal method is also called as implemented method or concrete method.

public void funA() // method signature
{ //method body

this body can contains zero or many statements

}


--the method which is having a method body is known as implemented or concrete method.(at least zero body)

--the method without body (only singnature) is called as unimplemened  method or abstract method.
--abstract keyword must be there in that method signature.


public abstract void funA();

****Note: inside a normal class (in concreate class) we can not have any abstract methods.

Abstract class:
===========
Encapsulation
Polymorphism
Inheritance
Abstraction :

### Abstract Class and Abstract Method – Simple Explanation

---

#### 🔹 **Abstract Class:**

An **abstract class** is a class that **cannot be instantiated directly** (i.e., you can’t create an object of it). It is meant to be a **blueprint** for other classes.

It **may contain:**

* **Abstract methods** (which have no body and must be implemented by child classes),
* **Non-abstract methods** (which have a body),
* Fields (variables),
* Constructors.

👉 **Purpose:** To provide a common base for multiple related classes.

##### Example in Java:

```java
abstract class Animal {
    abstract void makeSound();  // abstract method (no body)

    void eat() {
        System.out.println("This animal eats food.");  // concrete method
    }
}
```

---

#### 🔹 **Abstract Method:**

An **abstract method** is a method that:

* **Has no body** (just the method signature),
* **Must be overridden** in the subclass,
* Can only exist inside an abstract class (or interface).

##### Example:

```java
abstract void makeSound();  // No body — must be implemented in a subclass
```

---

#### 🔸 Subclass Example:

```java
class Dog extends Animal {
    @Override
    void makeSound() {
        System.out.println("Bark");
    }
}
```

---

### 🔍 Why Use Abstract Classes and Methods?

* To enforce a **common structure** across subclasses.
* To **avoid code duplication** (reuse common methods).
* To ensure that **certain methods are implemented** in all child classes.

---

### 🧠 Quick Recap:

| Feature             | Abstract Class         | Abstract Method                        |
| ------------------- | ---------------------- | -------------------------------------- |
| Can be instantiated | ❌ No                   | ❌ No                                   |
| Has method body     | ✅ Yes (some methods)   | ❌ No (must be overridden)              |
| Purpose             | Base for other classes | Enforce specific method implementation |

