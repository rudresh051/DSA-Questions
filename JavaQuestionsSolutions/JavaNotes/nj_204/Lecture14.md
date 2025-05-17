# Interface

In Java we have 3 types of valid structures
* Normal or concrete class (fully implemented structure)
* Abstract class(partial implemented structure)
* Interface(fully unimplemented structure)

Implemented means - Method with body

--java compiler generates **.class file** for all the above valid structure.  
--with the help of an interface we achieve 100% abstraction in java.  
an interface contains only abstract methods and constant variables(public static final)  
--from java-8 onwards an interface can contains some special kinds of method, which will have body also.  
--How to create an Interface?  
we create an interface by using **"interface"** keyword.example:

example -

```java
interface Intr{
    int x = 10; // Important - It will become public static final you mention or not
    abstract void funX(); // it will become public and abstract
    void funY();

}
```


--as we extends a class inside another class, we implement an interface inside another class.  
--if a class is implementing an **interface** , then that class must   override all the abstract methods present inside that interface otherwise we need to mark that implementation class as **abstract class**.


**Note -** We can NOT create an interface object directly, we always create object of the implemented concrete class.

Interface is also one type of user-defined data type, so we can declare its variable also.


## var-args (variable-arguments)
--this concept allows us to define a
single method, which can take **zero or multiple arguments.**  
--before this concept, we use either method overloading or array as a method paramater,but they were not efficient , they
may raise maintanence problem.  

example -  
public void funi(int...i){

    //
}

example - 
```java
class Main 
{


	static void fun1(int... i){
		System.out.println("inside fun1 of Main");
		for(int a:i){
			System.out.println(a);
		}
	}

	public static void main(String[] args) 
	{
		fun1(10,20,30,40,50);
	}
}
```

## Enum in java:
--with the help of Enum, we can create our **own data type (enumerated type)** which will going to contains some fixed set of
constants.

**Declaring enum:-** either inside a class or as a external file.  
java compiler will generate the **.class file** for an enum also.  
--we can declare the main method also inside an enum and we can run a enum file as a class also.  
Every enum is internally implemented by using Class concept.  
Every enum constant represents an object of type enum.

example - external enum
```java
enum Color 
{
	RED, GREEN, PINK, YELLOW;
}
```

example - internal enum

```java
class Main1 
{
	enum Color{
		GREEN, RED, PINK, YELLOW;
	}
	public static void main(String[] args) 
	{
		Color c = Color.YELLOW;
	}
}
```

