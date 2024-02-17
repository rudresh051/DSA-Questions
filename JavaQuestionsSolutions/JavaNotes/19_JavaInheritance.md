# Java Inheritance (Subclass and Superclass)
In Java, it is possible to inherit attributes and methods from one class to another.  
* subclass(child) - the class that inherits from another class
* superclass(parent) - the class being inherited from

To inherit from a class, use the **extends** keyword.

e.g. In this example, the **Car** class (subclass) inherits the attributes and methods from the **Vehicle** class(superclass):

```
class Vehicle{
    protected String brand = "Ford";
    public void honk(){
        System.out.println("Tuut, tuut!");
    }
}
class Car extends Vehicle{
    private String modelName = "Mustang";
    public static void main(String[] args){
        Car myFastCar = newCar();
        myFastCar.honk();

        System.out.println(myFastCar.brand + " " + myFastCar.modelName);
    }
}

output
Tuut, tuut!
Ford Mustang
```

1. We set the brand attribute in Vehicle to a `protected` access modifier.

## Why and When to Use "Inheritance"?

* It is useful for code reusability

# The final keyword
If you don't want other classes to inherit from a class , use the **final** keyword.

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

output - It will throw an error
Main.java:9: error: cannot inherit from final Vehicle
class Main extends Vehicle {
                  ^
1 error)
```