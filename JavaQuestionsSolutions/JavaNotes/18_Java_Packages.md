# Java Packages
A package in Java is used to group related classes.  
Think of it as a folder in a file directory.    
We use packages to avoid name conflicts, and to write a better maintainable code. 

**Packages are divided into two categories**:

1. **Built-in Packages** (packages from the Java API)
2. **User-defined Packages** (create your own packages)

## Built-in Packages
1. The Java API is a library of prewritten classes, that are free to use, included in the Java Development Environment.
2. Check this complete list
 https://docs.oracle.com/javase/8/docs/api/.
3. The library is divided into packages and classes.
4. To use a class or a package from the library, you need to use the import keyword.

```
import package.name.Class;   // Import a single class
import package.name.*;   // Import the whole package
```

## Import a Class
If you find a class you want to use, for example, the Scanner class, which is used to get user input, write the following code.  
e.g.   
`import java.util.Scanner;`

## Import a Package
To import a whole package, end the sentence with an asterisk sign (*)
e.g. `import java.util.*;`
## User defined Packages

To create a package, use the `package` keyword:
e.g. 
```
package mypack;

class MyPackageClass { 
  public static void main(String[] args) { 
    System.out.println("This is my package!"); 
  } 
}
```


