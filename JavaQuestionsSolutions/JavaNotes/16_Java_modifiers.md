# Modifier
* In simple terms, Java modifiers are like tags or labels we put on different parts  
of a Java program to control who can access them and how they can be used.

* Java modifiers help us manage who can interact with different parts of our code.  

* They make sure everything stays organized and works smoothly when we're writing computer programs in Java.

e.g. 
`public class Main`

The public keyword is an access modifier, meaning that it is used to set the  
access level for classes, attributes, methods and constructors.

We divide modifiers into two groups:

**Access Modifiers** - controls the access level

**Non-Access Modifiers** - do not control access level, but provides other functionality

## Access Modifiers
For classess we can either use `public` or default

1. Public - The class is accessible by any other class
    * ```
            public class Main {
                public static void main(String[] args) {
                System.out.println("Hello World");
            }
        }

      ```
2. Default - The class is only accessible by classes in the same package. 
This is used when you don't specify a modifier.

```
    class MyClass {
        public static void main(String[] args) {
            System.out.println("Hello World");
        }
    }
```

**For attributes, methods and constructors** we can use the following modifier
1. `public` - The code is accessible for all classes  
e.g. 
```
public class Main {
  public String fname = "John";
  public String lname = "Doe";
  public String email = "john@doe.com";
  public int age = 24;
}
```
2. `private` - The code is only accessible within the declared class  
e.g. 
```
public class Main {
  private String fname = "John";
  private String lname = "Doe";
  private String email = "john@doe.com";
  private int age = 24;
  
  public static void main(String[] args) {
    Main myObj = new Main();
    System.out.println("Name: " + myObj.fname + " " + myObj.lname);
    System.out.println("Email: " + myObj.email);
    System.out.println("Age: " + myObj.age);
  }
}
```
3. default - The code is only accessible in the same package.  
e.g. 
```
class Person {
  String fname = "John";
  String lname = "Doe";
  String email = "john@doe.com";
  int age = 24;
  
  public static void main(String[] args) {
    Person myObj = new Person();
    System.out.println("Name: " + myObj.fname + " " + myObj.lname);
    System.out.println("Email: " + myObj.email);
    System.out.println("Age: " + myObj.age);
  }
}
```
4. Protected - The code is accessible in the same package and subclasses  
e.g.
```
class Person{
    protected String fname = "John";
    protected String lname = "Doe";
    protected String email = "john@doe.com";
    protected int age = 24;
}
class Student extends Person{
    private int graduationYear = 2018;
    public static void main(String[] args){
        Student myObj = new Student();
        System.out.println("Name: " + myObj.fname + " " + myObj.lname);
        System.out.println("Email: " + myObj.email);
        System.out.println("Graduation Year: " + myObj.graduationYear);
    }
}
```

# Non-Access Modifiers
For classes, you can use either `final` or `abstract`

1. **final** - The class cannot be inherited by other classes  
e.g.
```
final class Vehicle {
  protected String brand = "Ford";
  public void honk() {
    System.out.println("Tuut, tuut!");
  }
}

class Main extends Vehicle {
  private String modelName = "Mustang";
  public static void main(String[] args) {
    Main myFastCar = new Main();
    myFastCar.honk();
    System.out.println(myFastCar.brand + " " + myFastCar.modelName);
  }
}
```
2. **abstract** - The class cannot be used to create objects  
e.g. 

```
// abstract class
abstract class Main {
  public String fname = "John";
  public String lname = "Doe";
  public String email = "john@doe.com";
  public int age = 24;
  public abstract void study(); // abstract method 
}

// Subclass (inherit from Person)
class Student extends Main {
  public int graduationYear = 2018;
  public void study() {
  
```

For **attributes and methods**, you can use the one of the following:

1. final - Attributes and methods cannot be overridden/modified
2. static - Attributes and methods belongs to the class, rather than an object
3. abstract - can only used in an abstract class, and can only be used on methods
4. transient - Attributes and methods are skipped when serializing the object containing them
5. synchronized - Methods can only be accessed by one thread at a time
6. volatile - The value of an attribute is not cached thread-locally, and is always read from the "main memory"

# Final

If you don't want the ability to override existing attribute values, declare attributes as final:

```
public class Main {
  final int x = 10;
  final double PI = 3.14;

  public static void main(String[] args) {
    Main myObj = new Main();
    myObj.x = 50; // will generate an error: cannot assign a value to a final variable
    myObj.PI = 25; // will generate an error: cannot assign a value to a final variable
    System.out.println(myObj.x);
  }
}
```

# Static 
A static method means that it can be accessed without creating an object of the class, unlike public:  
Check below example to understand difference betwenn static and public 
```
public class Main {
  // Static method
  static void myStaticMethod() {
    System.out.println("Static methods can be called without creating objects");
  }

  // Public method
  public void myPublicMethod() {
    System.out.println("Public methods must be called by creating objects");
  }

  // Main method
  public static void main(String[ ] args) {
    myStaticMethod(); // Call the static method
    // myPublicMethod(); This would output an error

    Main myObj = new Main(); // Create an object of Main
    myObj.myPublicMethod(); // Call the public method
  }
}
```