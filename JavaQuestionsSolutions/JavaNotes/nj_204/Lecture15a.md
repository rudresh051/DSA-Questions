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