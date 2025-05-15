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


## Bank example
Bank.java
```java
class TransactionClass
{
	public static void main(String[] args) 
	{
		HdfcBank hdfcBank = new HdfcBank(5.5, "BLR");
		SbiBank sbiBank = new SbiBank();

		System.out.println(hdfcBank.branchName);
		System.out.println(sbiBank.branchName);


		hdfcBank.withdraw(1000);
	}
}
```

```java
class HdfcBank extends Bank
{
	int interestRate;
	String homeLoan;
	String offerCard;


	HdfcBank(String intRate, String branchCode){
		super(branchCode);
		this.interestRate = intRate;
	}

	void getYourPA(){
		
	}

	@Override
	void withdraw(int amount){
		// use of super keyword
		if(amount > 0){
			super.withdraw(amount);// basically means call parent 
			// class method
		}
	}
}
```

```java
class SbiBank extends Bank 
{
	String waitTime;
	String onlineOffers;
	String creditCard;

	void getLunchTime(){
	
	}

	void getQueueLength(){
		
	}

}
```

```java
class TransactionClass
{
	public static void main(String[] args) 
	{
		HdfcBank hdfcBank = new HdfcBank(5.5, "BLR");
		SbiBank sbiBank = new SbiBank();

		System.out.println(hdfcBank.branchName);
		System.out.println(sbiBank.branchName);


		hdfcBank.withdraw(1000);
	}
}
```

## instanceof

```java
class A 
{
	String name = "A";

	A(String name){
		this.name = name;
	}
	
	A(){
		System.out.println("I am A contructor");
	}

	void fun1(){
		System.out.println("Im A's fun1");
	}
}
```

```java
class B extends A
{
	B(){
		//super("Hello");
		System.out.println("I am B constructor");
	}

	void fun1(){
		System.out.println("I am B's fun1");
		super.fun1();
	}
}
```

```java
class C extends A
{
	C(){
		System.out.println("I am C constructor");
	}

	void fun1(){
		System.out.println("I am C's fun1");
	}
}
```

```java
class Normal 
{

	A getNewObject(int objNumber){
			return new A();
		}

		B getNewObjectB(int objNumber){
			return new B();
		}


		//if only I want have one function
		// I cannot have 2 return type


		// return type object
		Object getAnyNewObj(int objNum){
			if(objNum == 1){
				return new A();
			}else{
				return new B();
			}
		}

	public static void main(String[] args) 
	{
		A a = new B();
		B b2 = (B)a;

		if(a instanceof A){
			// left side is => object
			// right side is => class
			System.out.println("true");
			System.out.println(a);
		}
		else{
			System.out.println("False");
			System.out.println(a);
		}


		B b = new B();

		// b.fun1();

		Normal normal = new Normal();
		A aObj = (A) normal.getAnyNewObj(1);
	}
}
```

## final keyword

The `final` keyword in Java is used to **restrict modification**. Depending on where it's used—**with variables, methods, or classes**—it serves different purposes.

---

### ✅ 1. `final` Variable (Constants)

* **Once assigned, the value cannot be changed.**
* It's commonly used to define constants.

#### Example:

```java
final int MAX_USERS = 100;
MAX_USERS = 200; // ❌ Compilation error
```

If it's a reference to an object:

```java
final List<String> list = new ArrayList<>();
list.add("Hello");         // ✅ Allowed: modifying the object
list = new ArrayList<>();  // ❌ Error: cannot reassign the reference
```

---

### ✅ 2. `final` Method

* **Prevents method overriding** in subclasses.
* Useful when you want the method's logic to remain unchanged in any child class.

#### Example:

```java
class Parent {
    final void show() {
        System.out.println("This cannot be overridden");
    }
}

class Child extends Parent {
    // void show() { ... }  // ❌ Error: Cannot override final method
}
```

---

### ✅ 3. `final` Class

* **Prevents inheritance.** No class can extend a final class.

#### Example:

```java
final class Utility {
    public static void print() {
        System.out.println("Utility class");
    }
}

class MyUtility extends Utility { // ❌ Error: Cannot subclass final class
}
```

---

### ✅ Summary Table

| Use Case         | Effect                                      |
| ---------------- | ------------------------------------------- |
| `final` variable | Value can't be changed after initialization |
| `final` method   | Cannot be overridden in a subclass          |
| `final` class    | Cannot be subclassed                        |
