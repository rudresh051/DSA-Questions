# Java Classes/Objects
Java is an object-oriented programming language.

# Create a Class
To create a class, use the keyword `class`

e.g. Create a class named "Main" with a variable x:
```
public class Main {
  int x = 5;
}
```

# Create an Object
* In Java, an object is created from a class.
* To create an object of Main, specify the class name, followed by the object name, and use the keyword new:

e.g. Create an object called "myObj" and print the value of x:

```
public class Main {
  int x = 5;

  public static void main(String[] args) {
    Main myObj = new Main();
    System.out.println(myObj.x);
  }
}

```

## Multiple Objects
* You can create multiple objects of one class:

e.g. Create two objects of Main:

```
Result Size: 838 x 713
public class Main {
  int x = 5;
​
  public static void main(String[] args) {
    Main myObj1 = new Main();
    Main myObj2 = new Main();
    System.out.println(myObj1.x);
    System.out.println(myObj2.x);
  }
}
​
Output
5
5
```

## Using Multiple Classes
* You can also create an object of a class and access it in another class.  
* This is often used for better organization of classes (one class has all the attributes and methods,  
while the other class holds the main() method (code to be executed)).

Remember that the name of the java file should match the class name. In this example, we have created two files in the same directory/folder:

* Main.java  
    *   ```
        public class Main {
            int x = 5;
        }
        ```
* Second.java
    * ```
        class Second {
            public static void main(String[] args) {
                Main myObj = new Main();
                System.out.println(myObj.x);
            }
        }
        ```


# Java Class Attributes
* Class attributes are nothing but variables within a class.
* Another term for class attributes is fields.

e.g. Create a class called "Main" with two attributes: x and y:

```
public class Main {
  int x = 5;
  int y = 3;
}
```
## Accessing Attributes
* You can access attributes by creating an object of the class, and by using the dot syntax (.):

e.g. Create an object called "myObj" and print the value of x:

```
public class Main{
    int x=5;

    public static void main(String[] args){
        Main myObj = new Main();
        System.out.println(myObj.x);
    }
}

```
## Modify Attributes
Set the value x to 40 in above example

```
public class Main{
    x = 5;

    public static void main(String[] args){
        Main myObj = new Main();
        myObj.x = 40;
        System.out.println(myObj.x);
    }
}
```
* Use the `final` keyword if you don't want the ability to override the values
```
public class Main{
    final int x= 5;
    public static void main(String[] args){
        Main myObj = new Mani();
        myObj.x = 25; // It will generate an error: cannot assign a value to a final variable
        System.out.println(myObj.x);
    }
}
```

## Multiple Objects
If you create multiple objects of one class, you can change the   
attribute values in one object, without affecting the attribute values in the other:

e.g. Change the value of x to 25 in myObj2, and leave x in myObj1 unchanged:


```
public class Main {
  int x = 5;

  public static void main(String[] args) {
    Main myObj1 = new Main();  // Object 1
    Main myObj2 = new Main();  // Object 2
    myObj2.x = 25;
    System.out.println(myObj1.x);  // Outputs 5
    System.out.println(myObj2.x);  // Outputs 25
  }
}
```

## Multiple Attributes
* You can specify as many attributes as you want:

```
public class Main {
  String fname = "John";
  String lname = "Doe";
  int age = 24;

  public static void main(String[] args) {
    Main myObj = new Main();
    System.out.println("Name: " + myObj.fname + " " + myObj.lname);
    System.out.println("Age: " + myObj.age);
  }
}

```