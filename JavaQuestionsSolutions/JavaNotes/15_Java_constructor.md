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