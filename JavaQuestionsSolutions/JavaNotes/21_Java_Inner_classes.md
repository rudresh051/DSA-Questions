# Java Inner Classes

In Java, it is also possible to nest classes(a class within a class).  
The purpose of nested classes is to group classes that belong together, which  
makes the code more readable and maintainable.

e.g. 
```
class OuterClass{
    int x = 10;
    class InnerClass{
        int y = 5;
    }
}

public class Main{
    public static void main(String[] args){
        OuterClass myOuter = new OuterClass();
        OuterClass.InnerClass myInner = myOuter.new InnerClass();
        System.out.println(myInner.y + myOuter.x);
    }
}

output
15
```

## Private Inner Class
Unlike a "regular" class, an inner class can be private or protected. If you  
don't want outside objects to access the inner class, declare the class as  private:
## Static Inner Class
An inner class can also be static, which means that you can access it without creating an object of the outer class:

* One advantage of inner classes, is that they can access attributes and methods of the outer class:

e.g.
```
class OuterClass{
    int x = 10;

    class InnerClass{
        public int myInnerMethod(){
            return x;
        }
    }
}

public class Main{
    public static void main(String[] args){
        OuterClass myOuter = new OuterClass();
        OuterClass.InnerClass myInner = myOuter.new InnerClass();
        System.out.println(myInner.myInnerMethod());
    }
}
```