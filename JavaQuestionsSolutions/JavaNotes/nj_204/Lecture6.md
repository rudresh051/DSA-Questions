# Java Day4 Pre Class Video: Object Collaboration

In an Object Oriented Programming language like Java, multiple classes collaborate with each other and provide the  
services(solution to a perticular problem).
--the classes which will try to collaborate each other, should be in **same path.**  
--we can define a class as a instance member of another class as well , by this we establish "Has-A" relationship between 2
objects.  



* Default value of any reference value is null

Keep both files in same path
```java
class  A
{
	int i = 10;
	void funA(){
		System.out.println("inside function of A");
		
	}
}

```



```java
//package day4;

public class Demo {

	/* int x = 100;
	A a1 = new A(); */

	int x;
	A a1;

    public static void main(String[] args) {
        System.out.println("inside main method of Demo class");


/*		Demo d1 = new Demo();
		
		// creating object of different class here
		// it is possible condition is both class should be in the same path

		A a1 = new A();

		System.out.println(d1);
		System.out.println(a1); */
		
		Demo d1 = new Demo();
		System.out.println(d1.x);
		System.out.println(d1.a1);

		//d1.a1.funA();

    }
}
```

* NullPointerException - It happens when we try to access a member from a null value

```java
//package day4;

public class Demo {

	/* int x = 100;
	A a1 = new A(); */

	int x;
	A a1;

    public static void main(String[] args) {
        System.out.println("inside main method of Demo class");


/*		Demo d1 = new Demo();
		
		// creating object of different class here
		// it is possible condition is both class should be in the same path

		A a1 = new A();

		System.out.println(d1);
		System.out.println(a1); */
		
		Demo d1 = new Demo();
		System.out.println(d1.x);//0
		System.out.println(d1.a1);// null

// a1 is holding null value
		d1.a1.funA();

    }
}
```

![alt text](image-7.png)


```java
//package day4;

public class Demo {

	/* int x = 100;
	A a1 = new A(); */

	int x;
	A a1;

    public static void main(String[] args) {
        System.out.println("inside main method of Demo class");


/*		Demo d1 = new Demo();
		
		// creating object of different class here
		// it is possible condition is both class should be in the same path

		A a1 = new A();

		System.out.println(d1);
		System.out.println(a1); */
		
		Demo d1 = new Demo();
		System.out.println(d1.x);//0
		System.out.println(d1.a1);// null

		//d1.a1.funA();

		d1.a1 = new A(); // a1 is non static variable. it can accessed by d1.a1

    }
}
```


## Methods

In java we use methods to perform certain actions, we define a method to reuse the code, define the code once and reuse it  
many times.

* Java doesnot support nested method definition. It will give compiler time error. We can call a method inside a method.


```java
//package day4;

public class Demo {


	
	// method author
	static void funX(A a1){
		System.out.println("inside funX of Demo" + a1);
		a1.funA();
	}

    public static void main(String[] args) {
        System.out.println("inside main method of Demo class");


		// 3 possibility - i.e. pass value to a reference variable of a class
		//1. It's own class object
		/* A obj = new A();
		funX(obj);*/

		// 2. to a class variable - any child object. if a particular class is a child of A class
		/* A obj = new AChild();
		funX(obj) */

		// 3. is null
		A obj = null;
		funX(obj);
		
    }
}
```

* Handling null value

```java
//package day4;

public class Demo {


	
	// method author
	static void funX(A a1){
		if(a1 !=null){
		
		System.out.println("inside funX of Demo" + a1);
		a1.funA();
		}
		else{
			System.out.println("Please don't pass null value");
		}

	}

    public static void main(String[] args) {
        System.out.println("inside main method of Demo class");


		// 3 possibility - i.e. pass value to a reference variable of a class
		//1. It's own class object
		/* A obj = new A();
		funX(obj);*/

		// 2. to a class variable - any child object. if a particular class is a child of A class
		/* A obj = new AChild();
		funX(obj) */

		// 3. is null
		A obj = null;
		funX(obj);
		
    }
}
```

* Method with  a return type

```java
//package day4;

public class Demo {	
	// method author
	static int funX(){
		System.out.println("inside funX of Demo" );
		int x = 100;
		return x;
	}

    public static void main(String[] args) {
        System.out.println("inside main method of Demo class");
		int result = funX();
		System.out.println(result);	
    }
}
```

* Method with a **class** return type

```java
//package day4;

public class Demo {


	
	// method author
	static A funX(){
		System.out.println("inside funX of Demo" );
		// returning own class object
		A a1 = new A();
		return a1;

		//or

		// use child class object
		// or use null to return

	}

    public static void main(String[] args) {
        System.out.println("inside main method of Demo class");
		funX();
    }
}


```

## Polymorphism

--defining more than one functionality with the same name in the same class is known as polymorphism.  

we have 2 type of polymorphism:-  
l.**static polymorphism** :- method overloading (same method name,but the parameter will be different)  
--is also know as compile time polymorphism, i.e which method will be called , decided at compile time only.  

2.**dynamic polymorphism** :- method overriding:- (same method name And same parameter,) method overriding we achive throught inheritance  

--is also know as run time polymorphism, i.e which method will be called , decided at runtime.


```java
class Demo
{
    void fun1(byte b){
        System.out.println("inside fun1(byte) of Demo");
    }

    void fun1(int i){
        System.out.println("inside fun1(int) of Demo");
    }


    public static void main(String[] args){
        Demo d1 = new Demo();
        byte x = 20;
        d1.fun1(x); // it will give the priority to the nearest one.

        or
        // d1.fun1(20); It will call the fun1 with int argument
    }
}

## Summary
* How to compile in CMD
`javac A.java`

* How to run
`java A`

* When an object is instantiated
	* Memory is allocated
	* Constructor
	* Object existence

* Null pointer exception
* Function signature
* Methods in Java
	* Return type - void, int, class

