# Java Day4 Live Session : Object Collaboration
* Address.java

```java
package day4;

public class Address {
/*    Address
        Street
        House No
        Pin code
        */

    String street = "BTM1, Banglore";
    int houseNum = 17;
    int pinCode = 560029;
    void printMyAddress(){
        System.out.println("Address = " + street + " " + houseNum+ " " + pinCode);
    }


    // Implemented function
//    int add(int num1, int num2){
//        // int c is a local variable
//        int c = num1 + num2;
//        return c;
//    };

    // Function signature
    // => No curly braces
//    abstract void fun1();
}
```

* Instagram.java

```java
package day4;

public class Instagram {

/*    Instagram
        Name
        Address
        Followers
        ID
        Photos
        Videos
        Status
        */
    String name = "Shiv";
    String address = "Bangalore";
    static int id = 1;
    static Address myAddress = new Address();

    int add(int num1, int num2){
        int c = num1 + num2;
        return c;
    }


    // For below function "Address" is return type
    // so now inside this function should return an object of this Address
    Address getNewMyAddressObject(){
//       return myAddress;
        return new Address();
        // above line will create a new Object of "Address()"  It will just return
        // whatever the existing object that we have as our static variable
        // So the idea here is that we should understand that we can pass
        // the object and return the object from our function also
    }

    // Important - Passing an object example
    void printObjAddress(Address myObj){
        myObj.printMyAddress();
    }


    // you can have int or any other combinations. You can play around with that
    Address sample(Address obj1){
        return obj1;
    }

    public static void main(String[] args){
        // Creating object of the class
        Instagram i1 = new Instagram();

/*        System.out.println(id);
        System.out.println(i1.id);
        System.out.println(Instagram.id);*/

        i1.myAddress.printMyAddress();
        // System is a class, out is also an object, and out object has a println function
        System.out.println();

        Address newAddress = i1.getNewMyAddressObject();
        i1.printObjAddress(newAddress);

    }


}
```

## Polymorphism

Defining more than one functionality with the same name in the same class is known as  
polymorphism.
The main advantage of Polymorphism is "Flexibility".   

**We have 2 type of polymorphism:**

1. **Static polymorphism:** If the Polymorphism is existed at compilation time then it is  
called as Static Polymorphism. example: method overloading (same method name,
but the parameter will be different)  
It is also know as compile time polymorphism, i.e. which method will be called,  
decided at compile time only.

<!-- 
Number of parameters
Type of parameters
Order of parameters
        
Return type doesn't matter 
-->

2. **Dynamic Polymorphism:** If the Polymorphism is existed at runtime then that  
Polymorphism is called as Dynamic Polymorphism. example: method overriding:-  
(same method name ,and same parameter)
Method overriding we achieve through inheritance.  
It is also know as run time polymorphism, i.e. which method will be called , decided at  
runtime.


## ‘this’ keyword:

'this' keyword points to the current object.  
Whenever it is required to point an object from a method which is under execution because  
of that object then we use 'this' keyword.  

Following 3 main job of this keyword:  
1. Points to the current class obj.  
2. Differentiate between local and instance variable.  
3. Calling a constructor of a class from another constructor of the same class.  

* Pointing to the current class object

```
package com.masai;
public class Demo
{
//instance variable
int x=100;
void fun1(){
//local variable
Day4: Object Collaboration 20
int x=500;
System.out.println("inside fun1() of Demo");
System.out.println(this); //Demo@232323 current class obj
System.out.println(this.x); // 100
System.out.println(x); //500
}
public static void main(String[] args)
{
Demo d1=new Demo();
System.out.println(d1); // Demo@232323
d1.fun1();
//System.out.println(this); //Compilation Error
}
}

```

## Constructor

* It is a special type of non-static method, which will be executed automatically only at
the time of creating an object.

`Demo d1=new Demo();`

**In Java:**

A constructor:
* Has no return type (not even void).
* Has the same name as the class.
* Is used to initialize objects at the time of their creation.

✅ Example with a Constructor:
```java
class Main {
    String month;

    // Constructor
    public Main(String month) {
        this.month = month;
    }

    public void printMonths() {
        System.out.println("Month is: " + month);
    }

    public static void main(String[] args) {
        Main m = new Main("JAN");
        m.printMonths();
    }
}
```

Above can be done with this method also

✅ Example with a Setter Method:
```java
class Main {
    String month;

    public void setMonth(String month) {
        this.month = month;
    }

    public void printMonths() {
        System.out.println("Month is: " + month);
    }

    public static void main(String[] args) {
        Main m = new Main();
        m.setMonth("JAN");
        m.printMonths();
    }
}
```

Great question — and the answer depends on **what you’re building** and **how you want to structure your code**.

Let’s break it down:

---

### ✅ **Use a Constructor When:**

| Scenario                                                      | Why constructor is better                                 |
| ------------------------------------------------------------- | --------------------------------------------------------- |
| You **must initialize** data at the time of object creation   | Guarantees object is ready to use                         |
| You want to make your class **more robust and cleaner**       | Reduces chance of using uninitialized data                |
| You’re working on **larger or real-world projects**           | Follows OOP design practices (encapsulation, abstraction) |
| You want **immutability** (no changes allowed after creation) | Constructor-only setup supports that                      |

#### ✔️ Example Use Case:

```java
Main m1 = new Main("JAN"); // Ready to use immediately
m1.printMonths();
```

---

### ✅ **Use Setters or Without Constructor When:**

| Scenario                                                       | Why setter/no-constructor works well |
| -------------------------------------------------------------- | ------------------------------------ |
| You want **more flexibility** to assign or change values later |                                      |
| You’re creating objects with **optional fields**               |                                      |
| You’re just learning or prototyping quickly                    |                                      |
| You might reuse the same object with **different values**      |                                      |

#### ✔️ Example Use Case:

```java
Main m1 = new Main();
m1.setMonth("JAN");
m1.printMonths();
```

---

### 🧠 **Analogy**

Think of constructors as a **restaurant chef** who prepares your dish as soon as you order it.
Setters are like a **DIY salad bar**, where you can customize things later.

---

### 💡 **Best Practice (in real-world Java apps):**

* Use **constructors** when essential values must be provided.
* Use **setters** when values are optional or may change over time.
* Use **constructor + setters** in combination for flexibility.

---

### 🔧 Recommendation for You (as you're learning):

Start using constructors more often — it will help you think in an **object-oriented way**, which is essential for writing clean, scalable code.

Let me know if you want to try a small challenge to reinforce constructor usage 👨‍💻


✅ Example Code
```java
import java.util.*;

class ChefDish {
    String ingredient;  // This is like the variable you want to work with

    // 👨‍🍳 Constructor: Chef receives the ingredient from the user
    public ChefDish(String ingredient) {
        this.ingredient = ingredient;
        System.out.println("Chef received: " + ingredient);
    }

    // Method to prepare a dish using the ingredient
    public void prepareDish() {
        if (ingredient.equalsIgnoreCase("Potato")) {
            System.out.println("Preparing French Fries 🍟");
        } else if (ingredient.equalsIgnoreCase("Tomato")) {
            System.out.println("Preparing Tomato Soup 🍅🥣");
        } else {
            System.out.println("Chef is still experimenting with: " + ingredient);
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter an ingredient for the chef:");
        String userInput = scanner.nextLine();

        // 👇 Chef gets the ingredient when object is created
        ChefDish dish = new ChefDish(userInput);

        // 👨‍🍳 Chef is ready to cook right away
        dish.prepareDish();
    }
}
```

## Constructor Chaining
* Constructor can call other constructors of the
same class or superclass
* Constructor call from a constructor must be
the first step. (call should appear in the first
line)
* Such series of invocation of constructors is
known as constructor chaining.
* super() or this() 
  * First line of constructor is either super() or this()(by default super())
  * Constructor never contains super() and this() both
Explain the output of below program - 
A1  
B2  
B1  
```java
class A
{
	public A(){

		System.out.println("A 1");
	}
}

class B extends A
{
	public B(){
		//super();// if we don't write this
		// compiler will automatically write
		this(4);// here this represent same class constructor
		System.out.println("B 1");
	}
	public B(int k){
		System.out.println("B 2");
	}

}

public class Example
{
	public static void main(String[] args){
		B o1 = new B();
	}
}
```

## Summary

* Class Collaboration
* Local variable
* Returning object
  * Getting the object
  * Passing the object
* Object - Default class
* 'this' keyword
* constructor - basically construct the objects