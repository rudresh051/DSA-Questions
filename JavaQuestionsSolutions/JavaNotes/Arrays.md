# Java Arrays
* To declare an array, define the variable type with square brackets:
* To insert values to it, you can place the values in a comma-separated list, inside curly braces:
e.g. 

`String[] cars = {"Volvo", "BMW", "Ford", "Mazda"};
`

## Loop through the array
```
String[] cars = {"Volvo", "BMW", "Ford", "Mazda"};
for (int i = 0; i < cars.length; i++) {
  System.out.println(cars[i]);
}
```

### Multidimensional array
To create a two-dimensional array, add each array within its own set of curly braces:

```
int[][] myNumbers = { {1, 2, 3, 4}, {5, 6, 7} };
```