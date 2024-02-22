# Java Constructors
```
Think of a constructor in Java like the blueprint for making something new, 
like assembling a piece of furniture. Let's say you're putting together a chair. 
The constructor is like the instruction manual that guides you through the process 
step by step. It helps you set up the chair properly, from attaching the legs to 
putting on the seat, ensuring everything is in the right place. In Java, when you 
want to create a new object, you use a constructor to initialize it correctly, 
ensuring it's ready for use just like assembling a chair according to its blueprint.
```
**Definition**  
A constructor is a special method that is called when an object is instantiated(Created)

* A constructor in Java is a special method that is used to initialize objects.
* The constructor is called when an object of a class is created.
* It can be used to set initial values for object attributes:  

e.g. 1
```
class Human{
    String name;
    int age;
    double weight;

    Human(String name, int age, double weight){
        this.name = name;
        this.age = age;
        this.weight = weight;
    }
}

public class Main {
    public static void main(String[] args){
        Human human1 = new Human("Rick", 65, 70);
        Human human2 = new Human("Morty", 16, 70);
        System.out.println(human1.name);
        System.out.println(human2.name);
    }
}
```

#### Why passing arguments to a constructor is useful?
=> This gives us the ability to create different objects that have different attributes
#### Why we are using this keyword in above example?
=> In Java, "this" is a special keyword used inside a class to refer   
to the current object. Think of it as a way for an object to refer   
to itself. In your example, when you create a new human   
(Human human1 = new Human("Rick", 65, 70);), you're telling Java to make a   
new human with the name "Rick", age 65, and weight 70. When you use   
this.name = name;, you're saying, "Set the name of this human to the name   
I provided when I created it."




e.g. 2
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

e.g. 2
```
public class Main{
    int modelYear;
    String modelName;

    public Main(int year, String name){ // passing multiple parameters to the constructor
        modelYear = year;
        modelName = name;
    }
    public static void main(String[] args){
        Main myCar = new Main(1970, "Mustang");
        System.out.println(myCar.modelYear + " " + myCar.modelName);
    }
}
```