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