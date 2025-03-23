# Java Day4 Live Session : Object Collaboration
* Address.java

```java
package day4;

public class Address {
/*    Address
        Street
        House No
        Pin code
        */

    String street = "BTM1, Banglore";
    int houseNum = 17;
    int pinCode = 560029;
    void printMyAddress(){
        System.out.println("Address = " + street + " " + houseNum+ " " + pinCode);
    }


    // Implemented function
//    int add(int num1, int num2){
//        // int c is a local variable
//        int c = num1 + num2;
//        return c;
//    };

    // Function signature
    // => No curly braces
//    abstract void fun1();
}
```

* Instagram.java

```java
package day4;

public class Instagram {

/*    Instagram
        Name
        Address
        Followers
        ID
        Photos
        Videos
        Status
        */
    String name = "Shiv";
    String address = "Bangalore";
    static int id = 1;
    static Address myAddress = new Address();

    int add(int num1, int num2){
        int c = num1 + num2;
        return c;
    }


    // For below function "Address" is return type
    // so now inside this function should return an object of this Address
    Address getNewMyAddressObject(){
//       return myAddress;
        return new Address();
        // above line will create a new Object of "Address()"  It will just return
        // whatever the existing object that we have as our static variable
        // So the idea here is that we should understand that we can pass
        // the object and return the object from our function also
    }

    // Important - Passing an object example
    void printObjAddress(Address myObj){
        myObj.printMyAddress();
    }


    // you can have int or any other combinations. You can play around with that
    Address sample(Address obj1){
        return obj1;
    }

    public static void main(String[] args){
        // Creating object of the class
        Instagram i1 = new Instagram();

/*        System.out.println(id);
        System.out.println(i1.id);
        System.out.println(Instagram.id);*/

        i1.myAddress.printMyAddress();
        // System is a class, out is also an object, and out object has a println function
        System.out.println();

        Address newAddress = i1.getNewMyAddressObject();
        i1.printObjAddress(newAddress);

    }


}
```

## Polymorphism

Defining more than one functionality with the same name in the same class is known as  
polymorphism.
The main advantage of Polymorphism is "Flexibility".   

**We have 2 type of polymorphism:**

1. **Static polymorphism:** If the Polymorphism is existed at compilation time then it is  
called as Static Polymorphism. example: method overloading (same method name,
but the parameter will be different)  
It is also know as compile time polymorphism, i.e. which method will be called,  
decided at compile time only.

<!-- 
Number of parameters
Type of parameters
Order of parameters
        
Return type doesn't matter 
-->

2. **Dynamic Polymorphism:** If the Polymorphism is existed at runtime then that  
Polymorphism is called as Dynamic Polymorphism. example: method overriding:-  
(same method name ,and same parameter)
Method overriding we achieve through inheritance.  
It is also know as run time polymorphism, i.e. which method will be called , decided at  
runtime.


## ‘this’ keyword:

'this' keyword points to the current object.  
Whenever it is required to point an object from a method which is under execution because  
of that object then we use 'this' keyword.  

Following 3 main job of this keyword:  
1. Points to the current class obj.  
2. Differentiate between local and instance variable.  
3. Calling a constructor of a class from another constructor of the same class.  

* Pointing to the current class object

```
package com.masai;
public class Demo
{
//instance variable
int x=100;
void fun1(){
//local variable
Day4: Object Collaboration 20
int x=500;
System.out.println("inside fun1() of Demo");
System.out.println(this); //Demo@232323 current class obj
System.out.println(this.x); // 100
System.out.println(x); //500
}
public static void main(String[] args)
{
Demo d1=new Demo();
System.out.println(d1); // Demo@232323
d1.fun1();
//System.out.println(this); //Compilation Error
}
}

```

## Constructor

* It is a special type of non-static method, which will be executed automatically only at
the time of creating an object.

`Demo d1=new Demo();`


## Summary

* Class Collaboration
* Local variable
* Returning object
  * Getting the object
  * Passing the object
* Object - Default class
* 'this' keyword
* constructor - basically construct the objects