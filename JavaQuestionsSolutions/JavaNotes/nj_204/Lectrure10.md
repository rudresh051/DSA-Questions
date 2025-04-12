## Inheritance

Inheritance in Java is a **fundamental object-oriented programming concept** that allows one class to **inherit properties and behaviors (fields and methods)** from another class.

![alt text](image-11.png)

### 🔑 Key Points:
- **Superclass (Parent class):** The class whose features are inherited.
- **Subclass (Child class):** The class that inherits the features of another class.
- The subclass gets access to the **public** and **protected** members of the superclass.
- The keyword used for inheritance in Java is `**extends**`.

---

### 🧠 Why Use Inheritance?
- **Code reusability:** Common code can be written once in the superclass.
- **Method overriding:** Subclasses can provide specific implementations.
- **Polymorphism:** Enables dynamic method dispatch.

---

### 📌 Syntax:
```java
class Animal {
    void eat() {
        System.out.println("This animal eats food.");
    }
}

class Dog extends Animal {
    void bark() {
        System.out.println("The dog barks.");
    }
}
```

### 👇 Usage:
```java
public class TestInheritance {
    public static void main(String[] args) {
        Dog d = new Dog();
        d.eat();  // inherited method
        d.bark(); // method from Dog class
    }
}
```

### 🧱 Types of Inheritance in Java:
1. **Single Inheritance**
2. **Multilevel Inheritance**
3. **Hierarchical Inheritance**

> 🚫 **Note:** Java doesn't support **multiple inheritance with classes** (to avoid ambiguity), but you can achieve it using **interfaces**.
