## Java For loop
e.g.
```
for (int i = 0; i <= 10; i = i + 2) {
  System.out.println(i);
}
```
## For-Each Loop
There is also a "for-each" loop, which is used exclusively to loop through elements in an array:  
e.g.

```
public class Main {
  public static void main(String[] args) {
    String[] cars = {"Volvo", "BMW", "Ford", "Mazda"};
    for (String i : cars) {
      System.out.println(i);
    }    
  }
}
```
# Java while loop
The while loop loops through a block of code as long as a specified condition is true:

```
public class Main {
  public static void main(String[] args) {
    int i = 0;
    while (i < 5) {
      System.out.println(i);
      i++;
    }  
  }
}
Output
0
1
2
3
4
```

## Java do-while loop
The loop will always be executed at least once, even if the condition is false,   
because the code block is executed before the condition is tested:
e.g.
```
int i = 0;
do {
  System.out.println(i);
  i++;
}
while (i < 5);
```