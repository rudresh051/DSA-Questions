# Java Arrays
* Array is used to store multiple values in a single variable
* To declare an array, define the variable type with square brackets:
* To insert values to it, you can place the values in a comma-separated list, inside curly braces:  
* The array should have the same data type. you cannot add string , numbers in same array
### Creating an Array - Method 1
* use the curly brackets to create array
* e.g. `String[] cars = {"volvo"}`
* e.g. `String[] cars = {"Volvo", "BMW", "Ford", "Mazda"};`
* e.g. `int[] numbers = new int[3];` // Array of integers with size 3
* e.g. `char[] characters = new char[4]` // An Array of characters with size 4 
* e.g. `String[] strings = new Strings[5]` // An Array of String with size 5

### Creating an Array - Method 2
```
class Food{
  String name;
  Food(String name){
    this.name = name;
  }
}

public class Main{
  public static void main(String[] args){
    // Creating an array with name refrigerator that can hold food objects for us
    Food[] refrigerator = new Food[3]; 
    // let's create 3 food objects
    Food food1 = new Food("Roti");
    Food food2 = new Food("Rice");
    Food food3 = new Food("Rajma");

    // Storing
    refrigerator[0] = food1;
    refrigerator[1] = food2;
    refrigerator[2] = food3;

    System.out.println(refrigerator[0].name); // Roti
    System.out.println(refrigerator[1].name); // Rice
    System.out.println(refrigerator[2].name); // Rajma
  }
}
```
### Access Elements from the array
* e.g. `cars[0]`
* Trying to access an element which is not present will give an exception
`ArrayIndexOutOfBoundException`
## Loop through the array
```
String[] cars = {"Volvo", "BMW", "Ford", "Mazda"};
for (int i = 0; i < cars.length; i++) {
  System.out.println(cars[i]);
}
```

### Multidimensional array 
* It is nothing but an array of arrays. Think of 2D Arrays as number of rows and columns.
To create a two-dimensional array, add each array within its own set of curly braces:

e.g.1
```
int[][] myNumbers = { {1, 2, 3, 4}, {5, 6, 7} };
```

e.g.2
```
public class Main{
  public static void main(String[] args){
    // declaration of size of 2d array or allocating memory 
    String[][] cars = new String[3][3];
    // let's assign some elements
    cars[0][0] = "Camaro";
    cars[0][1] = "Corvette";
    cars[0][2] = "Silverado"; 
    cars[1][0] = "Mustang";
    cars[1][1] = "Ranger";
    cars[1][2] = "F-150";
    cars[2][0] = "Ferrari";
    cars[2][1] = "Lambo";
    cars[2][2] = "Tesla";

    // Now let's display our 2d array using nested for loop
    for(int i=0;i<cars.length;i++) {
      System.out.println();
      for(int j=0;j<cars[i].length;j++) {
        System.out.print(cars[i][j] + " ");
      }
    }
  }
}

/* output
Camaro Corvette Silverado 
Mustang Ranger F-150 
Ferrari Lambo Tesla */ 
```

e.g.3 For above example we can assign values right away when we declared it.

```
public class Main{
  public static void main(String[] args){
    // declaration of size of 2d array
    String[][] cars =   {
                            {"Camero","Corvette","Silverado"},
                            {"Mustang","Ranger","F-150"},
                            {"Ferrari","Lambo", "Tesla"}
                        };
    // Now let's display our 2d array using nested for loop
    for(int i=0;i<cars.length;i++) {
      System.out.println();
      for(int j=0;j<cars[i].length;j++) {
        System.out.print(cars[i][j] + " ");
      }
    }
  }
}
/* output
Camaro Corvette Silverado 
Mustang Ranger F-150 
Ferrari Lambo Tesla */ 
```