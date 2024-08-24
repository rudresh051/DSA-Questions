# Enums
An enum is a special "class" that represents a group of constants()
(unchangeable variables, like **final** variables)

To create an enum, use the enum keyword(instead of class or interface),  
and seperate the constants with a comma.  
Note that they should be in uppercase letters:

```
enum Level {
  LOW,
  MEDIUM,
  HIGH
}

public class Main { 
  public static void main(String[] args) { 
    Level myVar = Level.MEDIUM; 
    System.out.println(myVar); 
  } 
}
```
* Enum is short for "enumerations", which means "specifically listed".

## Enum inside a Class
```
public class Main{
    enum Level{
        LOW,
        MEDIUM,
        HIGH
    }
    public static void main(String[] args){
        Level myVar = Level.MEDIUM;
        System.out.println(myVar);
    }
}
```

## Enum in a Switch Statement
## Loop through an Enum

## Difference between Enums and Classes
* An enum can, just like a class, have attributes and methods. The only difference  
is that enum constants are public, static and final (unchangeable - cannot be overridden).

* An enum cannot be used to create objects, and it cannot extend other classes  
(but it can implement interfaces).

## Why And when to use enums?
Use enums when you have values that you know aren't going to change, like month days, days,   
colors, deck of cards, etc.
