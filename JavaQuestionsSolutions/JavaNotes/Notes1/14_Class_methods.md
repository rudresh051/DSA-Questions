# Static vs. Public
* A static method, which means that it can be accessed without creating an object of the class,  
unlike public, which can only be accessed by objects:

e.g.
```
public classs Main(){
    static void myStaticMethod(){
        System.out.println("Static methods can be called without creating objects");
    }

    public void myPublicMethod(){
        System.out.println("Public methods must be called by creating objects");
    }

    // Main method
    public static void main(String[] args){
        myStaticMethod();

        Main myObj = new Main();
        myObj.myPublicMethod();
    }
}
```

# Access Methods With an Object
e.g. Create a Car object named myCar. Call the fullThrottle() and speed() methods on the myCar object,

```
public class Main(){
    <!-- Method names -->
    public void fullThrottle(){
        System.out.println("The car is going as fast as it can!");
    }

    public void speed(int maxSpeed){
        System.out.println("Mas speed is: " + maxSpeed);
    }

    <!-- Call the above methods/functions -->
    public static void main(String[] args){
        myCar.FullThrottle();

        Main myCar = new Main();
        myCar.speed(200);

    }

    Output:
    The car is going as fast as it can!
    Max speed is: 200

}
```
