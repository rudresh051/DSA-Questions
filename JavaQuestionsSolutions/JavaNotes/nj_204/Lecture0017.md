# lectures - 30927

* Abstract class
  * With the help of Abstract class we achieve partial abstraction

* Abstract method - Unimplemented method
* Abstract class mean to be extended.
  * > There is no meaning of abstract class until it is extended by child
  * Abstract class existence depend upon its child class

1. Full implemented structure(concrete class)
2. Partial implemented structure(AC)
3. Full unimplemented structure(interface)

## Interface 
- It is **full unimplemented structure** in java
- till jdk 1.7 interfaces use to contains only abstract methods and final variables
- from jdk 1.8 we can place method with body also inside an interface

first we will see for jdk 1.7  
> how we create the interface

![alt text](image-14.png)

Example -  
Below is an unimplemented . 
> Inside interface you need to place only abstract method only

```java
package com.masai;

public interface X {
	
	// don't start with interface name with small letters
	// Always start with capital letters. use pascal naming convention
	
	
	public abstract void fun1();
	
}
```

save X.java and then compile  
javac X.java (if you are using notepad). after this you will get Byte code which is produced by java compiler. And it is X.class

> .class file will be generated for an interface also  
> constructor concept is not applicable with interface

Note - inside an interface if we define any unimplemented method, than that method is bydefault "public and abstract" whether we mention or not.  

e.g.  

```java
package com.masai;
public interface X{

void fun1();
// Interface के अंदर method bydefault public और Abstract होता है चाहे हम mention करें या ना करें 
// Also remember - Above facility is not present for abstract class
}


// Abstract keyword is mandatory for abstract method in abstract class

![alt text](image-15.png)


- with the help of an interface we achieve full abstraction.

![alt text](image-16.png)

Example -  

X.java  
```java
package com.masai;
public interface X{
    void fun1();
    void fun2();
}
```

- as we extends a class to another class, we can implement an interface inside a class.

Rule -  
an interface can be implemented by any class, but if a class implements an interface, then that class must override all the abstract method of that interface otherwise we need to make that implemented class as an abstract class.

XImpl.java  

```java
package com.masai;

public class XImpl implements X {

	@Override
	public void fun1() {
		
		System.out.println("inside fun1 of XImpl");
	}

	@Override
	public void fun2() {
		System.out.println("inside fun2 of XImpl");
	}
	
	//specific method 
	public void fun3() {
		System.out.println("inside fun3 of XImpl");
	}

}

```
