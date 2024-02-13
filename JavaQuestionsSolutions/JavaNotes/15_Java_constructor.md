# Java Constructors
* A constructor in Java is a special method that is used to initialize objects.
* The constructor is called when an object of a class is created.
* It can be used to set initial values for object attributes:

e.g. 
```
// Create a Main class
public class Main{
    int x; // Create a clss attribute
    
    // Create a class constructor for the Main class
    public Main(){
        x = 5; // set the initial value for the class attribute x
    }

    public static void main(String[] args){
        Main myObj = new Main(); // Create an object of class Main
        System.out.println(myObj.x);
    }

    // output 5
}
```
* Note 1 - The constructor name must match the class name, and it cannot have a return type (like void).
* Note 2 - The constructor is called when the object is created.
* All classes have constructor by default: if you do not create a class constructor yourself,  
 Java creates one for you. However, then you are not able to set initial values for object attributes

## Constructor Parameters
* Constructors can also take parameters, which is used to initialize attributes.
* In the below example adds an `int y` parameter to the constructor. Inside the constructor we set x to y (x=y).
* When we call the constructor, we pass a parameter to the constructor(5), which will set the vlaue x to 5:
e.g.
```
public class Main{
    int x;
    public Main(int y){ // adding int y parameter to the constructor
        x = y;
    }
    public static void main(String[] args){
        Main myObj = new Main(5);
        System.out.println(myObj.x);
    }
}
// output 5
```