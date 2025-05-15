# Inheritance
In Java, inheritance is one of the core concepts of Object-Oriented Programming (OOP). It allows a new class (called a subclass or child class) to acquire (or inherit) the fields (variables) and methods of an existing class (called a superclass or parent class).

In simple words:
Inheritance lets you create a new class based on an existing class, reusing code, and adding new features or modifying existing ones without rewriting the original code.

**Types of Inheritance in Java:**
Single Inheritance: One class inherits from another.

Multilevel Inheritance: A class inherits from a class which is itself a subclass.

Hierarchical Inheritance: Multiple classes inherit from a single parent class.

(Java does not support multiple inheritance with classes to avoid ambiguity; instead, it supports multiple inheritance through interfaces.)

![alt text](image-12.png)

Example - Multilevel Inheritance
Father.java
```java
class Father 
{
	String skinTone = "Brown";
	void drinks(){
		System.out.println("I like water")
	}	
}
```
SonClass.java
```java
public class SonClass extends Father
{
	String = "Shiv";

	void greet(){
		System.out.println("greet")
	}

	public static void main(String[] args) 
	{
		SonClass obj = new SonClass();
		obj.greet();

		obj.drinks();
	}
}
```

GrandSon.java
```java
class GrandSon extends SonClass
{
	public static void main(String[] args) 
	{
		GrandSon grandSon = new GrandSon();

		grandSon.drinks();
	}
}
```
All the properties are inherited by child class can have it's own thing

* Use `@Override` mentioning explicitely in child class if child class changes parent method


Downcasting  - 
```
public class SonClass extends Father
{
	String name = "Shiv";

	void greet(){
		System.out.println("greet");
	}

	public static void main(String[] args) 
	{
		SonClass obj = new SonClass();
		obj.greet();

		obj.drinks();

		Father father2 = new SonClass();
		father2.drinks();

		//SonClass sonObj = new Father();// you cannot create SonClass object
		// using Father Class

		SonClass sunObj = (SonClass) father2;
	}
}
```

Example - `Class A → Class B → Class C`

```java
// Base class (Parent)
class Animal {
    void eat() {
        System.out.println("This animal eats food.");
    }
}

// Derived class (Child of Animal)
class Dog extends Animal {
    void bark() {
        System.out.println("The dog barks.");
    }
}

// Another derived class (Child of Dog, Grandchild of Animal)
class Puppy extends Dog {
    void weep() {
        System.out.println("The puppy weeps.");
    }
}

// Main class to test multilevel inheritance
public class MultilevelInheritanceDemo {
    public static void main(String[] args) {
        Puppy puppy = new Puppy();

        // Methods from all three classes
        puppy.eat();   // from Animal
        puppy.bark();  // from Dog
        puppy.weep();  // from Puppy
    }
}
```