### Comparison between Array and ArrayList in Java, along with some distinctions in Python and JavaScript:
| Feature          | Array                                | ArrayList                                            | Python (List)                          | JavaScript (Array)                    |
|------------------|--------------------------------------|------------------------------------------------------|----------------------------------------|--------------------------------------|
| **Definition**   | A fixed-size collection of elements  | A dynamic-size collection of elements                | A dynamic-size collection of elements  | A dynamic-size collection of elements|
| **Declaration**  | Must specify size upon creation      | No need to specify size upon creation               | No need to specify size upon creation | No need to specify size upon creation|
| **Resize**       | Cannot resize after creation          | Automatically resized when needed                    | Automatically resized when needed     | Automatically resized when needed    |
| **Performance**  | Faster due to fixed size             | Slightly slower due to dynamic resizing              | Similar to ArrayList                   | Similar to ArrayList                  |
| **Type Safety**  | Fixed type, checked at compile time  | Dynamic type, checked at runtime                     | Dynamic type, checked at runtime       | Dynamic type, checked at runtime      |
| **Usage**        | Commonly used for primitive types    | Commonly used for objects and collections            | Similar to ArrayList                   | Similar to ArrayList                  |
|**Syntax Example**|`int[] numbers = new int[5];`|`ArrayList<Integer> numbers = new ArrayList<>();`|`numbers = [1, 2, 3, 4, 5]` |`let numbers = [1, 2, 3, 4, 5];` |



In Java, Array is a fixed-size collection of elements, whereas ArrayList   
is a dynamic-size collection. Java requires you to specify the size of an   
array upon creation, and arrays cannot be resized afterward. On the other   
hand, ArrayList can dynamically resize itself as needed.

In Python, lists are similar to Java's ArrayList. They are dynamically sized   
and can contain elements of different types. However, Python lists don't   
require a size specification upon creation and can be resized dynamically.

In JavaScript, arrays are similar to ArrayList in Java and lists in Python.   
They are dynamic and can hold elements of different types without requiring a   
size specification upon creation.

Overall, while all three languages provide dynamic collections, Java's Array   
is fixed in size, requiring a size specification upon creation, whereas Java's   
ArrayList, Python lists, and JavaScript arrays can dynamically resize themselves as needed.

```
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        // ArrayList examples for different data types
        ArrayList<Integer> intList = new ArrayList<>();
        intList.add(10);
        intList.add(20);
        
        ArrayList<String> stringList = new ArrayList<>();
        stringList.add("Hello");
        stringList.add("World");
        
        ArrayList<Double> doubleList = new ArrayList<>();
        doubleList.add(3.14);
        doubleList.add(2.718);
        
        // Array examples for different data types
        int[] intArray = new int[]{1, 2, 3, 4, 5};
        
        String[] stringArray = new String[]{"apple", "banana", "orange"};
        
        double[] doubleArray = new double[]{2.5, 3.7, 1.8};
        
        // Accessing elements
        System.out.println("ArrayList<Integer> intList: " + intList);
        System.out.println("ArrayList<String> stringList: " + stringList);
        System.out.println("ArrayList<Double> doubleList: " + doubleList);
        
        System.out.print("int[] intArray: ");
        for (int num : intArray) {
            System.out.print(num + " ");
        }
        System.out.println();
        
        System.out.print("String[] stringArray: ");
        for (String str : stringArray) {
            System.out.print(str + " ");
        }
        System.out.println();
        
        System.out.print("double[] doubleArray: ");
        for (double num : doubleArray) {
            System.out.print(num + " ");
        }
        System.out.println();
    }
}

```