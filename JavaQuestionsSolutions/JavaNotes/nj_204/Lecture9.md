# String - L

String is basically an object that represents sequence of char values. OR An array of characters.

## String Pool

* It is just like a CARPOOL. Like String are stored in a box

What does that means?

* String Pool is a storage area in Java Heap where only string literals stores.
* Also known as **String Intern Pool** or **String Constant Pool**
  * **String Caching**
  * **Reusable Strings**
  * The **distinc**t values are stored.

* Strings are Immutable. That means Strings cannot be changed.
  * But it can be changed with other way


```java
package day4;

public class StringPractise {

    public static void main(String[] args){
        String str1 = "Cat";
        String str2 = "Cat";

		System.out.println(str1==str2);// true
    }

}
```

## Benefits

* Increase the performance
* Decrease the memory load.
* To decrease the number of String objects.

![alt text](image-9.png)

![alt text](image-10.png)

## String Builder and String Buffer

* Both used to create the Strings
* Both StringBuilder and StringBuffer are mutable
* Both are exactly same.

e.g.  
`StringBuffer stringBuffer = new StringBuffer("spartans");`  

`StringBuilder stringBuilder = new StringBuilder("spartans");`

### StringBuffer

* Thread Safe
  * All methods are synchronized in StringBuffer.
  * Only one thread is allowed to operate to it.
  * Next thread has to wait until previous thread complete its task.

### StringBuilder

* Not Thread Safe
  * All ...

### String vs StringBuilder vs StringBuffer

Parameter - Storage, Mutability, Thread Safe, Performance, Syntax