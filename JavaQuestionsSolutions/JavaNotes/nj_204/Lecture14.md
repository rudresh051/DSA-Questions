# Interface

In Java we have 3 types of valid structures
* Normal or concrete class (fully implemented structure)
* Abstract class(partial implemented structure)
* Interface(fully unimplemented structure)

Implemented means - Method with body

--java compiler generates .class file for all the above valid structure.
--with the help of an interface we achieve 100% abstraction in java.
an interface contains only abstract methods and constant variables(public static final)
--from java-8 onwards an interface can contains some special kinds of method, which will have body also.
--we create an interface by using **"interface"** keyword.example:

example - 

```java
interface Intr{
    int x = 10; // it will become public static final you mention or not
    abstract void funX(); // it will become public and abstract
    void funY();

}
```

Note - We can not create an interface object directly, we always create object of the implemented concrete class.

Interface is also one type of user-defined data type, so we can declare its variable also.