# Java ArrayList

The **ArrayList** class is a resizable array, which can be found in the **java.util** package.  

The difference between a built-in array and an ArrayList in Java,   
is that the size of an array cannot be modified (if you want to add   
or remove elements to/from an array, you have to create a new one).   
While elements can be added and removed from an ArrayList whenever you want.   
The syntax is also slightly different:

e.g.  
Create an ArrayList object called cars that will store strings: 

```
import java.utel.ArrayList; // import the ArrayList class
ArrayList<String> cars = new ArrayList<String>(); // Create an ArrayList object
```
# Add Items
use `add()` method
cars.add("Volvo");

# Access an Item
use `get()` method and refer to the index number
cars.get(0)

# Change an Item
To modify an element, use the `set()` method and refer to the index number:

cars.set(0,"Opel");

# Remove an Item
To remove an element, use the **remove()** and refer to the index number  
`cars.remove(0);`

To remove all the elements in the ArrayList, use the **clear()** method.

# ArrayList Size
To find out how many elements an ArrayList have, use the `size` method:

`cars.size()`

# Loop Through an ArrayList
1. use for `loop` and use `size()` method
2. You can also loop through an `ArrayList` with the **for-each** loop
e.g.
```
import java.util.ArrayList;

public class Main { 
  public static void main(String[] args) { 
    ArrayList<String> cars = new ArrayList<String>();
    cars.add("Volvo");
    cars.add("BMW");
    cars.add("Ford");
    cars.add("Mazda");
    for (int i = 0; i < cars.size(); i++) {
      System.out.println(cars.get(i));
    }
  } 
}
```

e.g. with for-each loop
```
public class Main {
  public static void main(String[] args) {
    ArrayList<String> cars = new ArrayList<String>();
    cars.add("Volvo");
    cars.add("BMW");
    cars.add("Ford");
    cars.add("Mazda");
    for (String i : cars) {
      System.out.println(i);
    }
  }
}
```

## ArryList for other types
1. To use other types, such as int, you must specify an equivalent wrapper class: `Integer`
    * Use Boolean for boolean
    * Use Character for char
    * Double for double

```
import java.util.ArrayList;
public class Main(String[] args){
    ArrayList<Integer> myNumbers = new ArrayList<Integer>();
    myNumbers.add(10);
    myNumbers.add(15);
    myNumbers.add(20);
    myNumbers.add(25);
    for(int i:myNumbers){
        System.out.println(i);
    }
}
```

## Sort an ArrayList
Another useful class in the java.util package is the Collections class, which   include the sort() method for sorting lists alphabetically or numerically:  
```
import java.util.ArrayList;
import java.util.Collections; // Import the Collections class

public class Main{
    public static void main(String[] args){
        ArrayList<String> cars = new ArrayList<String>();
        cars.add("Volvo");
        cars.add("BMW");
        cars.add("Ford");
        cars.add("Mazda");
        Collections.sort(cars); //sort cars
        for (String i:cars){
            System.out.println(i);
        }
    }
}
```