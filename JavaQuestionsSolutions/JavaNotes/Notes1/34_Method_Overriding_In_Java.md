# Method overriding
### Explanantion - 1
```
Imagine you have a toy robot that can make different sounds when you press 
its buttons. Now, suppose you have two toy robots, one that makes car sounds 
and another that makes animal sounds. Even though they're both robots, they 
each make different sounds because they have special abilities. That's a bit 
like overriding in Java – it's when we give a special ability to a toy robot 
that's similar to another robot, but it does something a little different.
```

### Explanation - 2
```
In Java, overriding is like customizing or modifying the behavior   
of a method that is already defined in a class or its superclass.   
It allows a subclass to provide a specific implementation of a method   
that is already defined in its superclass. This is useful when you want   
to change how a method works in a subclass to better suit its particular   
needs, while still keeping the same method name and parameters.

```

### Explanation - 3
In Java, overriding is a mechanism that allows a subclass to   
provide a specific implementation of a method that is already defined   
in its superclass. This is achieved by declaring a method in the subclass   
with the same name, return type, and parameter list as the method in the   
superclass. When an object of the subclass is used, the overridden method   
in the subclass is called instead of the method in the superclass.

e.g.1
```
class Animal {
    public void makeSound() {
        System.out.println("Animal makes a sound");
    }
}

class Dog extends Animal {
    @Override
    public void makeSound() {
        System.out.println("Dog barks");
    }
}

public class Main {
    public static void main(String[] args) {
        Animal animal = new Animal();
        animal.makeSound(); // Output: Animal makes a sound

        Dog dog = new Dog();
        dog.makeSound(); // Output: Dog barks
    }
}

```
In this example, the Dog class overrides the makeSound() method of   
the Animal class to provide its own implementation. When the makeSound()   
method is called on a Dog object, it prints "Dog barks" instead of the   
default "Animal makes a sound" message from the superclass. This allows   
for customization of behavior in subclasses while maintaining a consistent   
interface across different types of objects.



e.g. 2
```
class Animal{
    void speak(){
        System.out.println("The animal speaks")
    }
}

class Dog extends Animal{
    // So here speak here in dog child class is called overriding method
    void speak(){
        System.out.println("The dog goes *bark*")
    }
}
public class Main{
    public static void main(String[] args){
        // Method overriding = Declaring a method in sub class,
        // which is already present in parent class.
        // done so that a child can give its own implementation

        Dog dog = new Dog();
        dog.speak();
    }
}
```

