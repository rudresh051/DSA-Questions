### Example 1 - 

```java
class Demo 
{
	public void fun1(int i){
		System.out.println("inside fun1 of Demo");
		System.out.println("the value of i is" + " " + i);

	}

	public static void main(String[] args) 
	{
		Demo d1 = new Demo();

		// int x = 10;
		byte x = 10;
		d1.fun1(x);
	}
}
```

### Example 2 - 


 ```java
class Demo 
{
	public void fun1(A a1){
		System.out.println("inside fun1 of Demo");
		System.out.println("the value of a1 is" + " " + a1);
		a1.funA();

	}

	public static void main(String[] args) 
	{
		Demo d1 = new Demo();

		// pass ? - To a class variable only 3 values are allowed
		// same class object, It's child class object or null value

		
		// way1
		//A obj = new A();
		//d1.fun1(obj);

		// way2
		// d1.fun1(null); // It's a valid value but not a legal //value

		// way3
		// same class object
		d1.fun1(new A());

	}
}
```

### Example 3 - null pointer exception

```java
class A 
{
	int i=10;

	void funA(){
		System.out.println("inside funA of A");
	}
}
```



```java
class Demo 
{
	public void fun1(A a1){
		System.out.println("inside fun1 of Demo");
		System.out.println("the value of a1 is" + " " + a1);
		a1.funA();

	}

	public static void main(String[] args) 
	{
		Demo d1 = new Demo();

		// pass ? - To a class variable only 3 values are allowed
		// same class object, It's child class object or null value

		
		// way1
		//A obj = new A();
		//d1.fun1(obj);

		// way2
		d1.fun1(null);

		// way3
		// same class object
		//d1.fun1(new A());

	}
}
```

more robust method  

```java
class Demo 
{
	public void fun1(A a1){

		// robust method
		if(a1 !=null){
			System.out.println("inside fun1 of Demo");
		System.out.println("the value of a1 is" + " " + a1);
		a1.funA();
		}
		else{
			System.out.println("Don't pass null value");
		}
	}

	public static void main(String[] args) 
	{
		Demo d1 = new Demo();

		// pass ? - To a class variable only 3 values are allowed
		// same class object, It's child class object or null value

		
		// way1
		//A obj = new A();
		//d1.fun1(obj);

		// way2
		d1.fun1(null);

		// way3
		// same class object
		//d1.fun1(new A());

	}
}
```

### Example 4 - 

```java
class A 
{
	int i=10;

	void funA1(){
		System.out.println("inside funA of A1");
	}

	void funA2(){
		System.out.println("inside funA of A2");
	}
}

```

```java
class B extends A
{
	public void funB(){
		System.out.println("inside funB of B");
	}


	@Override
	void funA1(){
		System.out.println("inside funA! of B class");
	}
}
```

```java
class Demo 
{
	public void fun1(A a1){

		// robust method
		if(a1 !=null){
			System.out.println("inside fun1 of Demo");
			System.out.println("the value of a1 is" + " " + a1);
			a1.funA1(); // funA1 is common in both Class A and Class B . which one will be called? Overridden will be called. Overridden will be called // this is called dynamic polymorphism
			
            
            a1.funA2();
		}
		else{
			System.out.println("Don't pass null value");
		}
	}

	public static void main(String[] args) 
	{
		Demo d1 = new Demo();


		// same class object
		//d1.fun1(new A());

		// child class object
		d1.fun1(new B());

	}
}
```

```txt
inside fun1 of Demo
the value of a1 is B@28a418fc
inside funA! of B class
inside funA of A2
```

## polymorphism

* Same method name but the functionality will be different.

We have 2 type of polymorphism - 
1. Static polymorphism (Compile time polymorphism )
    * We achieve using method overloading
2. Dynamic polymorphism (Run time polymorphism)
    * We achieve using method overriding


### Example - Compile time polymorphism

```java
class Demo 
{
	public void fun1(A a1){

		// robust method
		if(a1 !=null){
			System.out.println("inside fun1 of Demo");
			System.out.println("the value of a1 is" + " " + a1);
			a1.funA1(); // funA1 is common in both Class A and Class B . which one will be called? Overridden will be called // this is called dynamic polymorphism

			a1.funA2();
		}
		else{
			System.out.println("Don't pass null value");
		}
	}


	public void fun1(){
		System.out.println("inside fun1() of Demo");
	}

	public static void main(String[] args) 
	{
		Demo d1 = new Demo();
		d1.fun1();

	}
}
```

```java
class A 
{
	int i=10;

	void funA1(){
		System.out.println("inside funA of A1");
	}

	void funA2(){
		System.out.println("inside funA of A2");
	}
}

```

```java
class B extends A
{
	public void funB(){
		System.out.println("inside funB of B");
	}


	@Override
	void funA1(){
		System.out.println("inside funA! of B class");
	}
}
```

### Example - Object class method

```java
public class Person {
    String name;
    int age;

    Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    // Override toString() method
    @Override
    public String toString() {
        return "Person[name=" + name + ", age=" + age + "]";
    }

    // Override equals() method
    @Override
    public boolean equals(Object obj) {
        if (this == obj)
            return true;
        if (!(obj instanceof Person))
            return false;
        Person p = (Person) obj;
        return this.name.equals(p.name) && this.age == p.age;
    }

    // Override hashCode() method
    @Override
    public int hashCode() {
        return name.hashCode() + age;
    }

    public static void main(String[] args) {
        Person p1 = new Person("John", 30);
        Person p2 = new Person("John", 30);

        // toString() - Automatically called when printing the object
        System.out.println(p1);  // Output: Person[name=John, age=30]

        // equals() - Compare object content
        System.out.println(p1.equals(p2));  // Output: true

        // getClass()
        System.out.println(p1.getClass().getName());  // Output: Person

        // hashCode()
        System.out.println(p1.hashCode());  // Output: some hash int
    }
}
```

* First write `.java` file(i.e. source code)
* Then compile it => **Java compiler** will **compile** it.
* After compilation it will give `.class` file
* `.class` file contains byte code
* Then give `.class` file to **jvm** which will **execute/run** the code

* IDE automatically compile internally
  

* Function of compiler
  * Scan the code e.g. syntax error
  * It gives a free constructor or default or zero argument constructor


## Static Polymorphism
Static polymorphism in Java refers to method overloading, where the method that gets called is determined at compile time, not at runtime.

Definition - Static polymorphism allows a class to have multiple methods with the same name but different parameter lists (i.e., method signatures).

This is called compile-time polymorphism because the Java compiler determines which method to call based on the number, types, or order of parameters.	

```java
public class Calculator {

    // Method with two int parameters
    public int add(int a, int b) {
        return a + b;
    }

    // Overloaded method with three int parameters
    public int add(int a, int b, int c) {
        return a + b + c;
    }

    // Overloaded method with double parameters
    public double add(double a, double b) {
        return a + b;
    }

    public static void main(String[] args) {
        Calculator calc = new Calculator();

        System.out.println(calc.add(2, 3));          // calls add(int, int)
        System.out.println(calc.add(2, 3, 4));       // calls add(int, int, int)
        System.out.println(calc.add(2.5, 3.5));      // calls add(double, double)
    }
}
```

**Dynamic polymorphism** in Java refers to **method overriding**, where the method that gets called is determined **at runtime** based on the **object type**, not the reference type.


### Definition:

Dynamic polymorphism (also called **runtime polymorphism**) occurs when a **subclass provides a specific implementation** of a method that is already defined in its superclass. The method that is actually executed is resolved at **runtime**, based on the actual object, not the reference.

### Example:

```java
class Animal {
    void sound() {
        System.out.println("Animal makes a sound");
    }
}

class Dog extends Animal {
    @Override
    void sound() {
        System.out.println("Dog barks");
    }
}

class Cat extends Animal {
    @Override
    void sound() {
        System.out.println("Cat meows");
    }
}

public class Main {
    public static void main(String[] args) {
        Animal a1 = new Dog();   // Reference type: Animal, Object type: Dog
        Animal a2 = new Cat();   // Reference type: Animal, Object type: Cat

        a1.sound(); // Output: Dog barks
        a2.sound(); // Output: Cat meows
    }
}
```

---

### Key Points:

* Also called **method overriding**.
* Resolved **at runtime**, hence **dynamic**.
* Requires:

  * **Inheritance**
  * **Method overriding**
  * **Upcasting** (using superclass reference to point to subclass object)
* Promotes **flexibility and extensibility** in object-oriented design.

---

### 🔄 Difference from Static Polymorphism:

| Feature         | Static Polymorphism       | Dynamic Polymorphism |
| --------------- | ------------------------- | -------------------- |
| Also known as   | Compile-time polymorphism | Runtime polymorphism |
| Achieved by     | Method overloading        | Method overriding    |
| Resolution time | Compile time              | Runtime              |
| Binding         | Early binding             | Late binding         |
| Flexibility     | Less flexible             | More flexible        |

### Example - 
```java
class A 
{
	int i=10;

	void funA1(){
		System.out.println("inside funA of A1");
	}

	void funA2(){
		System.out.println("inside funA of A2");
	}
}
```

```java
class B extends A
{
	public void funB(){
		System.out.println("inside funB of B");
	}


	@Override
	void funA1(){
		System.out.println("inside funA! of B class");
	}
}
```

```java
class Demo 
{
	public void fun1(A a1){

		// robust method
		if(a1 !=null){
			System.out.println("inside fun1 of Demo");
			System.out.println("the value of a1 is" + " " + a1);
			a1.funA1(); // funA1 is common in both Class A and Class B . which one will be called? Overridden will be called // this is called dynamic polymorphism

			a1.funA2();
		}
		else{
			System.out.println("Don't pass null value");
		}
	}


	public void fun1(){
		System.out.println("inside fun1() of Demo");
	}

	public void fun1(int x){
		System.out.println("inside fun1() of Demo here");
	}

	public static void main(String[] args) 
	{
		Demo d1 = new Demo();
		//d1.fun1();
		d1.fun1(5);
	}
}
```

### Example - 
Conclusion - The method will be called from the parent, or the method will be called from the child(overridden method), it totally depend upon what the child class has overridden method or not. And it will be decided at runtime. That's why it's called runtime polymorphism

practise -  

```java
class A 
{
	int i=10;

	void funA1(){
		System.out.println("inside funA1 A-clsss");
	}

	void funA2(){
		System.out.println("inside funA2 A-class");
	}
}
```

```java
class B extends A
{
	public void funB(){
		System.out.println("inside funB of B-class");
	}


	@Override
	void funA1(){
		System.out.println("inside funA1 of B-class");
	}
}
```

```java
class Demo 
{
	public void fun1(A a1){

		// robust method
		if(a1 !=null){
			System.out.println("inside fun1 of Demo");
			System.out.println("the value of a1 is" + " " + a1);
			a1.funA1(); // funA1 is common in both Class A and Class B . which one will be called? Overridden will be called // this is called dynamic polymorphism
			a1.funA2();
		}
		else{
			System.out.println("Don't pass null value");
		}
	}



	public static void main(String[] args) 
	{
		Demo d1 = new Demo();
		//d1.fun1();
		//d1.fun1(new A());
		d1.fun1(new B());
	}
}
```

Example - 
```java
class Demo 
{
	public void fun1(Object obj){

		// robust method
		if(obj !=null){
			System.out.println("inside fun1 of Demo");
			String s = obj.toString();// we can call this one
			System.out.println(s);
		}
		else{
			System.out.println("Don't pass null value");
		}
	}



	public static void main(String[] args) 
	{
		Demo d1 = new Demo();
		d1.fun1(new A());
	}
}
```
