# Object downcast example

```java
class Demo 
{
	public static void main(String[] args) 
	{
		// same class variable and same class object
		//LgOldTv remote = new LgOldTv();

		//remote.start();
		//remote.increaseVolume();
		// remote.changeChannel();// old way

		//LgSmartTv remote = new LgSmartTv();
		//remote.start();
		//remote.increaseVolume();
		//remote.changeChannel();// smart way
		//remote.playGame();
		
		// same or child class object
		LgOldTv remote = new LgSmartTv();
		remote.start();
		remote.increaseVolume();
		remote.changeChannel();// smart way i.e. over ridden method
		//remote.playGame();

		//LgSmartTv sremote = new LgSmartTv();
		//sremote.playGame();
		// why you want to create two object of same class
		// in the memeory

		// so use object downcast

		LgSmartTv sremote = (LgSmartTv)remote;// here we are 
		// downcast parent reference variable to  child and 
		// then accessing child methods.
		sremote.playGame();


	}
}
```

```java
class LgOldTv extends Object
{

	public void start(){
		System.out.println("TV starting");
	}
	public void increaseVolume(){
		System.out.println("Volume increased");
	}

	public void changeChannel(){
		System.out.println("Channel changed in old way");
	}

	public static void main(String[] args) 
	{
		System.out.println("Hello World!");
	}
}
```

```java
class  LgSmartTv extends LgOldTv
{
	@Override
	public void changeChannel(){
		System.out.println("Change channel in smart way");
	}

	// It can have it's own method
	public void playGame(){
		System.out.println("Game starts");
	}
}
```


Note - If a method is returning some value either in the same type of data or bigger than that type data. 
Example -   

```java
class Demo 
{

	// method signature, method body, method author
	// defining a method
	public int fun1(){
		System.out.println("inside fun1 of Demo");
		return 10;
	}

	public static void main(String[] args) 
	{
		Demo d1 = new Demo();
		long b = d1.fun1(); 
		// fun1 is called on the d1 object by main method.
	}
}
```

Note - Static members does not participate in inheritance  

Example - 
```java
class Demo 
{
	public A fun1(){
		System.out.println("inside fun1 of Demo");
		A a1 = new A();	

		return a1; // legal return value
		// same class object => new A() or a1;
		// it's child object => 
		// null
	}

	public static void main(String[] args) 
	{
		Demo d1 = new Demo();
		//d1.fun1();// we didn't catch the value and it will 
		// go to garbage collector

		// where to  hold it
		A a2 = d1.fun1(); // same type of variable

		// one more type - same or bigger type me

		Object obj = d1.fun1(); // bigger type
		// obj can call method present in Object class i.e. to the 
		// left hand side and any overridden methods which are present
		// to right hand side

	}
}
```

Example - 

```java
class Demo 
{
	public A fun1(){
		System.out.println("inside fun1 of Demo");
		A a1 = new A();	
		return a1;
	}

	public static void main(String[] args) 
	{
		Demo d1 = new Demo();
		A a1 = d1.fun1();
		if(a1 !=null){
			a1.funA();
		}
		else{
			System.out.println("Object is returning null value");
		}
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