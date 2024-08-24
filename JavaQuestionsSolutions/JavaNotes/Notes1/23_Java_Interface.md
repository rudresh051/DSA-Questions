# Java Interface

Abstraction is like having a big toy box with a label on it  
that says "Cars" or "Dolls." You don't need to know all the   
details about each toy inside the box, you just need to know   
what type of toys are in there.

Now, an interface is like a list of instructions on   
how to play with a specific toy. So, while abstraction   
organizes different types of toys into groups, interfaces   
tell you exactly what each toy can do and how to interact with it.

Notes  
1. An `interface` is a completely **"abstract class"** that is used to group related
methods with empty bodies:
e.g. 
```
// interface
interface Animal {
  public void animalSound(); // interface method (does not have a body)
  public void run(); // interface method (does not have a body)
}
```
2. To access the interface methods, the interface must be "implemented"   
(kinda like inherited) by another class with the implements keyword   
(instead of extends). The body of the interface method is provided by   
the "implement" class:
```
interface Animal {
  public void animalSound(); // interface method (does not have a body)
  public void sleep(); // interface method (does not have a body)
}

class Pig implements Animal {
  public void animalSound() {
    System.out.println("The pig says: wee wee");
  }
  public void sleep() {
    System.out.println("Zzz");
  }
}

class Main {
  public static void main(String[] args) {
    Pig myPig = new Pig();
    myPig.animalSound();
    myPig.sleep();
  }
}

```

### Notes on Interfaces:
* Like abstract classes, interfaces cannot be used to create  
objects.
* Interface methods do not have a body -  the body is provided by the implement class.
* On implementation of an interface, you must override all of its methods
* Interface methods are by default abstract and public
* Interface attributes are by default public, static and final
* An interface cannot contain a constructor (as it cannot be used to create objects)