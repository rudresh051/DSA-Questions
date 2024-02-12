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