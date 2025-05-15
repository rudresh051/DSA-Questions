# Object class

### ✅ What is the `Object` Class in Java?

In Java, **`Object`** is the **root (super) class of all classes**.

* Every class in Java **implicitly** extends `Object`—either directly or indirectly.
* That means every Java object is an instance of a class that ultimately inherits from `Object`.

---

### 📌 Important:

```java
Object parent = new ChildClass();
```

* You are **upcasting** `ChildClass` → `Object`.
* This is valid, because `ChildClass` inherits from `Object`.

---

### ✅ What can you do with `parent`?

Only methods defined in `Object` class will be accessible:

```java
System.out.println(parent.toString());
System.out.println(parent.hashCode());
System.out.println(parent.equals(someOtherObj));
```

Even though the actual object is a `ChildClass`, you **cannot access** its specific methods unless you **downcast** it.

---

### 🧠 Common `Object` Class Methods:

| Method                | Description                                       |
| --------------------- | ------------------------------------------------- |
| `toString()`          | Returns a string representation of the object     |
| `equals(Object obj)`  | Compares two objects for equality                 |
| `hashCode()`          | Returns a hash code                               |
| `getClass()`          | Returns the runtime class of the object           |
| `clone()`             | Creates and returns a copy (requires `Cloneable`) |
| `finalize()`          | Called by garbage collector before reclaiming     |
| `notify()` / `wait()` | Used in multithreading for sync                   |

---

### 🔁 Example:

```java
class ChildClass {
    void customMethod() {
        System.out.println("Hello from child");
    }
}

public class Test {
    public static void main(String[] args) {
        Object obj = new ChildClass();

        // obj.customMethod(); // ❌ Error: method not found in Object

        // ✅ Downcast to access child methods
        ChildClass child = (ChildClass) obj;
        child.customMethod(); // ✅ Works now
    }
}
```

---

### ✅ Summary:

* `Object` is the superclass of all Java classes.
* You can assign any class object to an `Object` reference — that’s **upcasting**.
* Only `Object` class methods are accessible unless you downcast.
* It’s essential in **generic programming**, **collections**, and **method parameters** like:

  ```java
  public boolean equals(Object obj) { ... }
  ```

Example - 

```java
class ParentClass 
{
	void fun1(){
		System.out.println("I am parent function");
	}
	
}
```

```java
class ChildClass extends ParentClass
{

	void fun2() {
        System.out.println("I am child fun2");
    }

	@Override
	void fun1(){
		System.out.println("I am child fun");
	}

	public static void main(String[] args) 
	{
		ChildClass child = new ChildClass();
		child.fun1();


		Object parent = new ChildClass();

		if(parent instanceof Child2){
			Child2 c2 = (Child2) parent;
			c2.fun1();
		}else{
			ChildClass child22 = (ChildClass) parent;
			child22.fun1();
		}

		ParentClass parent = new ChildClass(); // upcasting
		// We're creating a ChildClass object and referring to it using a ParentClass reference. 
		// This is called upcasting.
		parent.fun1(); // it will call the child fun1 method i.e. the overridden one
		//parent.fun2();// error
	
		ParentClass parent2 = new Child2();
		parent2.fun1();

		ParentClass parent3 = new GrandChild();
		parent3.fun1();

	}
}
```

```java
class Child2 extends ParentClass 
{
	void funChild2(){
		System.out.println("I am child2 fun");
	}

	@Override
	void fun1(){
		System.out.println("I am child2 fun");
	}
}
```

```java
class GrandChild extends ChildClass 
{
	@Override
	void fun1(){
		System.out.println("I am grand child fun");
	}
}
```