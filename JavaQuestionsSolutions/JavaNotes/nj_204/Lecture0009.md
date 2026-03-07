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


| Parameter      | String                         | StringBuilder                  | StringBuffer                    |
|--------------|--------------------------------|--------------------------------|--------------------------------|
| **Storage**   | Stored in the **String Pool** (if created using literals) or **Heap Memory** (if created using `new`). | Stored in **Heap Memory**.    | Stored in **Heap Memory**.    |
| **Mutability** | **Immutable** (Once created, cannot be changed). | **Mutable** (Can be modified without creating a new object). | **Mutable** (Can be modified without creating a new object). |
| **Thread Safe** | **Thread-Safe** (Since it's immutable, it can be shared across multiple threads without issues). | **Not Thread-Safe** (Multiple threads may cause inconsistency). | **Thread-Safe** (Uses synchronized methods to ensure safe usage in multi-threaded environments). |
| **Performance** | **Slow** (Every modification creates a new object, increasing memory usage). | **Fast** (Better performance than `String` and `StringBuffer` since it's not synchronized). | **Slower than `StringBuilder`** (Due to synchronization overhead). |
| **Syntax** | `String str = "Hello";` <br> `str = str + " World";` | `StringBuilder sb = new StringBuilder("Hello");` <br> `sb.append(" World");` | `StringBuffer sbf = new StringBuffer("Hello");` <br> `sbf.append(" World");` |

**Key Takeaways:**  
- Use **String** when you need **constant/unchangeable values**.  
- Use **StringBuilder** for **faster string manipulations in a single-threaded environment**.  
- Use **StringBuffer** when **thread safety** is required but performance is still a concern.  


* Example

```java
class Gmail 
{
	public static void main(String[] args) 
	{
		String name = "Shiv";
		String name2 = new String("Shiv");

		System.out.println(name);
		System.out.println(name2);

		if(name == name2){
			System.out.println("both are same");
		}
		else{
			System.out.println("both are different");
		}

    //example - 
    byte[] bytes = {100,102,103};
		String str1 = new String(bytes);
		System.out.println(str1);

    // example - 
    char chars1[] = {'r', 'u', 'd', 'r', 'a'};
		String s = new String(chars1);
		System.out.println(s);

    // StringBuilder
    StringBuilder s1 = new StringBuilder("ai");
		System.out.println(s1);


	}
}
```

### operations on strings

1. int length()
2. Char charAt(int i)
3. String substring(int i)
4. String substring(int i, int j)
5. String concat(String str)
6. int indexOf(String s)
7. int indexOf(String s, int)
8. int lastIndexOf(String s)
9. boolean equals(Object otherObj)
10. boolean equalsIgnoreCase(String anotherString)
11. int compareToIgnoreCase(String anotherString)
12. String toUpperCase()
13. String trim()
14. String replace(char oldChar, char newChar)
15. char[] toCharArray()

## Scanner Class in Java

The Scanner class is used to read the input data from different sources like input
streams, users, files, etc. This Scanner class belongs to java.util package.


The `System.in` parameter is used to take input from the standard input. It works just like taking input from the keyboard.

`Scanner input = new Scanner(System.in);`

To use the Scanner class inside our application, we need to import this class.

`import java.util.Scanner;`

example

```java
public class Test{
  public static void main(String[] args){
    Scanner input = new Scanner(System.in);
    String name = input.nextLine();
    System.out.println(name);
  }
} 


### Java Scanner Methods to Take Input

The `Scanner` class provides various methods that allow us to read inputs of different types.

```txt
nextInt() reads an int value from the user.
nextFloat() reads a float value form the user.
nextBoolean() reads a boolean value from the user
nextLine() reads a line of text from the user
next() reads a word from the user
nextLine() reads a whole line
nextByte() reads a byte value from the user
nextDouble() reads a doubl e value from the user
nextShort() reads a short value from the user.
nextLong() reads a long value from the user
```


Example - 

```java
import java.util.Scanner;
class GmailRudra {
	String email;
	String password;

	public static void main(String[] args) 
	{
		GmailRudra myGmail = new GmailRudra();

		Scanner myinput = new Scanner(System.in);
			
		System.out.println("Enter Email:");
		myGmail.email = myinput.nextLine();

		System.out.println("Enter password:");
		myGmail.password = myinput.nextLine();
		
		System.out.println("Email:" + myGmail.email);
		System.out.println("Pass:" + myGmail.password);

		if(myGmail.email.equals("rudreshwar@gmail.com") && myGmail.password.equals("1234567890")){
			System.out.println("Welcome to Home page");
		}
		else{
			System.out.println("Please enter correct credentials");
		}
	}
}
```

## JavaBean Class

A **JavaBean** class is a special type of Java class that follows certain conventions and is mainly used to encapsulate many objects into a single object (the bean). JavaBeans are commonly used in enterprise applications, especially in frameworks like Spring, JSP, and others, for transferring and managing data.

### ✅ **JavaBean Conventions**

A class is considered a JavaBean if it meets these rules:

1. **It must be public and have a no-argument constructor**  
   ```java
   public class Person {
       public Person() { }
   }
   ```

2. **It should have private fields**  
   - This is to ensure encapsulation.
   ```java
   private String name;
   private int age;
   ```

3. **It must provide public getter and setter methods**  
   - These allow read/write access to the properties.
   ```java
   public String getName() {
       return name;
   }

   public void setName(String name) {
       this.name = name;
   }

   public int getAge() {
       return age;
   }

   public void setAge(int age) {
       this.age = age;
   }
   ```

4. **It should be serializable (optional, but common)**  
   - Often used to allow saving the state of the object.
   ```java
   public class Person implements Serializable {
       ...
   }
   ```

---

### ✅ **Example of a JavaBean**
```java
public class Employee implements Serializable {
    private String name;
    private int id;
    
    // No-arg constructor
    public Employee() { }

    // Getters and setters
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
}
```

---

### 🔄 **Why Use JavaBeans?**
- Easy to manage data (especially in MVC frameworks).
- Supports **introspection** (automatic property detection using reflection).
- Works well with **JSP**, **Servlets**, **Spring**, and other Java EE frameworks.



### Example

```java
import java.util.Scanner;
import java.util.ArrayList;

class GmailRudra {

	ArrayList<JavaBean> accounts = new ArrayList<JavaBean>();
	

	public static void main(String[] args) 
	{
		GmailRudra myGmail = new GmailRudra();

		Scanner scanner = new Scanner(System.in);
		System.out.println("Enter 1 to Register or Enter 2 for signin");
		

		int choice = scanner.nextInt();
		scanner.nextLine();// consume the leftover line

		if(choice == 1){
		// show him register form

		// create object of JavaBean class. I guess I need to import it.
		JavaBean user = new JavaBean();

		System.out.println("Enter username");
		user.setName(scanner.nextLine());

		System.out.println("Enter Address");
		user.setAddress(scanner.nextLine());

		System.out.println("Enter user email");
		user.setEmail(scanner.nextLine());

		System.out.println("Enter user password");
		user.setPassword(scanner.nextLine());

		// arraylist has a method add. arraylist is basically an array
		myGmail.accounts.add(user);

		}
		else{
		// Login form
		System.out.println("Enter user email");
		String email = scanner.nextLine(); // using local variable here

		System.out.println("Enter user password");
		String password = scanner.nextLine();


		if(myGmail.accounts.size() > 0){
			for(int i=0; i<myGmail.accounts.size(); i++){
				if(myGmail.accounts.get(i).getEmail().equals(email) && 
					myGmail.accounts.get(i).getPassword().equals(password)	
				){
					System.out.println("Welcome " + myGmail.accounts.get(i).getName());
					break;
				
				}
				else{
					System.out.println("Please register");
				}
			}
		}

		}
	}
}
```


```java
class JavaBean 
{
	private String name;
	private String email;
	private String password;
	private String address;



	// getters
	public String getName(){
		return name;
	}
	public String getEmail(){
		return email;
	}
	public String getPassword(){
		return password;
	}
	public String getAddress(){
		return address;
	}

	// setters
	public void setName(String name){
		this.name = name;
	}

	public void setEmail(String email){
		this.email = email;
	}
	public void setPassword(String password){
		this.password = password;
	}
	public void setAddress(String address){
		this.address = address;
	}



	
	public static void main(String[] args) 
	{
		System.out.println("test");		
	}
}
```

