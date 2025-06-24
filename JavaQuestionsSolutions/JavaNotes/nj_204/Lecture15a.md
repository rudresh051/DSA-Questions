* Example 1 - 

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

* Example 2 - 


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

* Example 3 - null pointer exception

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