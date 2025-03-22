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

