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