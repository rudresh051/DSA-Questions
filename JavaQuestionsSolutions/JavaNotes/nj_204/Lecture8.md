# String class

* In java String is an obj that represents a sequece of character

* String - java.lang

## How to create

String str1 = "Welcome to java";

```
class  String1
{
	public static void main(String[] args) 
	{
		// Shortcut way
		String str1 = "Welcome to Java";
		System.out.println(str1);

		// By using new operator
		String str2 = new String("Welcome to Java");
		System.out.println(str2);

		// What's the difference
	}
}
```


```java
package day4;

public class StringPractise {

    public static void main(String[] args){
        String str1 = "Welcome to Java";
        String str2 = "Welcome to Java";

        String str3 = new String("Welcome to Java");
        System.out.println(str1==str2);// true
        System.out.println(str1==str3);// false
    }

}
```

![alt text](image-8.png)


The image represents memory allocation in Java for `String` objects. It differentiates between the **String Constant Pool (SCP)** and the **Heap Area** in RAM.

### Explanation with your code:

```java
public class StringPractise {
    public static void main(String[] args) {
        String str1 = "Welcome to Java";
        String str2 = "Welcome to Java";
        String str3 = new String("Welcome to Java");

        System.out.println(str1 == str2); // true
        System.out.println(str1 == str3); // false
    }
}
```

### Memory Breakdown:
1. **String Constant Pool (SCP) - Inside Heap Area**
   - When `String str1 = "Welcome to Java";` is executed:
     - The literal `"Welcome to Java"` is stored in the **String Constant Pool (SCP)**.
     - `str1` refers to this object in the SCP.
   - When `String str2 = "Welcome to Java";` is executed:
     - Since `"Welcome to Java"` already exists in the SCP, `str2` points to the same memory location.
   - Hence, `str1 == str2` returns **true**, as both reference the same SCP object.

2. **Heap Area - New String Object**
   - When `String str3 = new String("Welcome to Java");` is executed:
     - A **new object** is explicitly created in the **Heap Memory** (outside the SCP).
     - `str3` refers to this new object.
   - This is why `str1 == str3` returns **false**, as they refer to **different objects** in memory.

### Image Correlation:
- The **SCP area** in the image contains the `"Hello"` string (analogous to `"Welcome to Java"` in your code).
- `str1` and `str2` both point to this SCP object.
- The **Heap area** contains a separate `"Hello"` object (analogous to `str3` in your code).
- `str3` points to this separate heap memory object.

### Key Takeaways:
- **String literals** are stored in the **SCP**, and duplicate literals refer to the same object.
- **Explicit `new String("value")` creates a new object in the Heap**, even if the same string exists in SCP.
- `==` checks **reference equality** (whether two references point to the same object).
- To compare actual string values, use `.equals()` instead of `==`. 

### **String Immutability in Java**
In Java, **Strings are immutable**, meaning their values **cannot be changed** after creation. This is achieved by declaring the `String` class as `final`, and its internal character array (`char[] value`) is also `final`, preventing modifications.

#### **Why are Strings Immutable?**
1. **String Pool Optimization (SCP)**  
   - Java uses a **String Constant Pool (SCP)** to store string literals.
   - If two variables reference the same string literal, they share the same memory location.
   - If strings were mutable, changing one would affect all references, leading to **unexpected behavior**.
  
2. **Security**  
   - Strings are commonly used in **user authentication, file paths, and network connections**.  
   - If a String were mutable, a hacker could modify sensitive information like database credentials.
  
3. **Thread-Safety**  
   - Since Strings are immutable, multiple threads can safely share them without worrying about **synchronization**.
  
4. **Caching & Performance**  
   - Java caches hash codes for Strings, so they don’t need to be recomputed multiple times.  
   - If Strings were mutable, their hash codes would change, making them **inefficient in HashMaps and Sets**.

---

### **Example of String Immutability**
```java
public class StringImmutableTest {
    public static void main(String[] args) {
        String str1 = "Hello";
        str1.concat(" World"); // This does NOT modify str1

        System.out.println(str1); // Output: Hello
    }
}
```
**Why didn't `str1` change?**  
- The `concat()` method **creates a new string** (`"Hello World"`) instead of modifying `str1`.  
- Since `str1` is immutable, it **still refers to `"Hello"`**.

To actually modify the value, we need to assign it:
```java
str1 = str1.concat(" World");
System.out.println(str1); // Output: Hello World
```

---

### **Mutable Alternative: StringBuilder**
If you need a **mutable** string, use `StringBuilder`:
```java
StringBuilder sb = new StringBuilder("Hello");
sb.append(" World"); // Modifies the same object
System.out.println(sb); // Output: Hello World
```
- `StringBuilder` allows modifications without creating new objects.
- It is more **efficient for frequent string manipulations**.

---

### **Conclusion**
- **String is immutable** for performance, security, and thread-safety.
- **SCP optimizes memory** by reusing literals.
- Use **`StringBuilder` or `StringBuffer`** when modifying strings frequently.


## Array

example
```
class  Array1
{
	public static void main(String[] args) 
	{
		int[] marks = new int[10];

		System.out.println(marks);
	}
}
```
