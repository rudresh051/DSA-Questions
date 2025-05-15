# Questions

* When and why to create a constructor in Java?
* What is the use of `this` ?
* What is instance variable, class-level variable, method-level variable
* What is contructor and what's the syntax?
* Give me example of multilevel Inheritance in Java
* What is the use of super keyword in java? explain with an example
* what are types of constructor in java?
* What is use of initilization? is it mandatory?
* What is an object in java?




## Answers

## ✅ What is an **Object** in Java?

An **object** is a real-world **instance of a class** — it is created based on the **blueprint** (class), and it holds actual **data** and can perform **actions** (methods).

### 🧱 Think of it like:

* **Class** → Blueprint (e.g., design of a car)
* **Object** → Actual car you can drive, with its own color, number, fuel, etc.

---

### 🧠 In Java terms:

An **object**:

* Stores **state** → through **variables** (fields)
* Has **behavior** → through **methods**
* Is created using the `new` keyword

---

### 🔧 Example:

```java
class Dog {
    String name;
    int age;

    void bark() {
        System.out.println(name + " is barking");
    }
}

public class Main {
    public static void main(String[] args) {
        // Creating an object of Dog
        Dog d1 = new Dog();  // ← object created here

        // Initializing values
        d1.name = "Tommy";
        d1.age = 3;

        // Calling method
        d1.bark();  // Output: Tommy is barking
    }
}
```

---

## 🎯 So, what happens when you do `Dog d1 = new Dog();`?

* `Dog` is the **class type**
* `new` → allocates memory
* `Dog()` → calls the constructor
* `d1` → is the **reference variable** that holds the memory address of the object

---

## 🔄 Multiple Objects Example

```java
Dog d1 = new Dog();
Dog d2 = new Dog();

d1.name = "Bruno";
d2.name = "Rex";

d1.bark();  // Bruno is barking
d2.bark();  // Rex is barking
```

Each object (`d1`, `d2`) has its own **copy of data** and behaves **independently**.

---

## 🔍 Summary:

| Term        | Meaning                             |
| ----------- | ----------------------------------- |
| **Class**   | Blueprint or design of object       |
| **Object**  | Actual thing created from the class |
| **Fields**  | Data (variables) the object stores  |
| **Methods** | Actions object can perform          |

---

Want to write your own example with objects, and I’ll check and explain it?
