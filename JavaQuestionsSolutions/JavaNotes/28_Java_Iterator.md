# Java Iterator
1. An Iterator is an object that can be used to loop through collections, like arraylist  
and HashSet. 
2. It is called an "Iterator" because "Iterating" is the technical term for looping.
3. To use an Iterator, you must import it from the `java.util` package

So in other words  
```
An iterator is an object that enables you to traverse through a collection of elements, 
one element at a time. It provides a uniform way of accessing elements within different 
types of collections, such as lists, sets, and maps, without exposing the underlying 
implementation of the collection.
The iterator interface is a part of the Java Collections framework and is defined 
in the java.util package. It provides methods like hasNext() to check if there are 
more elements it iterate over, and next() to retrieve the next element in the collection.
```

e.g. 
```
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class IteratorExample {
    public static void main(String[] args) {
        List<String> list = new ArrayList<>();
        list.add("Apple");
        list.add("Banana");
        list.add("Orange");

        // Obtain an iterator for the list
        Iterator<String> iterator = list.iterator();

        // Iterate through the list using the iterator
        while (iterator.hasNext()) {
            String element = iterator.next();
            System.out.println(element);
        }
    }
}
// output
Apple
Banana
Orange
```
In this example, we create an ArrayList containing strings,   
obtain an iterator for this list using the iterator() method,   
and then iterate through the list using a while loop and the   
hasNext() and next() methods of the iterator.