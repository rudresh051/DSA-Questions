# Difference between Main and main
e.g. 
```
public class Main
{
	public static void main(String[] args) {
		String words = "One Two Three Four";
		int countWords = words.split("\\s").length;
		System.out.println(countWords);
	}
}
```
1. Main:

* Main with an uppercase "M" is typically used as the name of a Java class.
* It's a convention in Java to capitalize the first letter of class names.
* When you declare a class with the name Main, it's just like any other class   
name, and it doesn't have any special significance to the Java runtime.

2. main:
* main with a lowercase "m" is a special method in Java.
* It's the entry point of a Java program, where the Java Virtual Machine (JVM)   
starts executing the program.
* The main method must have a specific signature: public static void main(String[] args).
* The JVM looks for this specific method signature when starting   
the program, and execution begins from the first line of code inside the main method.