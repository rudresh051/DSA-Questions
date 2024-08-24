# Java Date and Time
1. Java does not have a built-in Date class, but we can import the Java.time   
package to work with date and time API.  
2. The package includes many date and time classes. 

|Class|Description|
|---------|-------|
|LocalDate|Represents a date(year,month,day (yyyy-MM-dd))|
|LocalTime|Represents a time (hour,minute,second and nanoseconds(HH-mm-ss-ns))|
|LocalDateTime|Represents both a date and a time (yyyy-MM-dd-HH-mm-ss-ns)|
|DateTimeFormatter|Formatter for displaying and parsing date-time objects|

## Display Current Date
To display the current date, import the `java.time.LocalDate` class, and use its `now()` method

e.g.1
```
import java.time.LocalDate;

public class Main{
    public static void main(String[] args){
        LocalDate myObj = LocalDate.now(); // Create a date object
        System.out.println(myObj); // Display the current date
    }
}
// Output
2024-02-25
```
## Display Current Time
To display the current time (hour, minute, second, and nanoseconds), import the   
`java.time.LocalTime` class, and use its `now()` method  
e.g.2  
```
import java.time.LocalTime; // import the LocalTime class
public class Main{
    public static void main(String[] args){
        LocalTime myObj = LocalTime.now();
        System.out.println(myObj);
    }
}
```

## Display Current Date and Time
To display the current date and time, import the `java.time.LocalDateTime` class, and use its `now()` method

e.g. 
```
import java.time.LocalDateTime; // import the LocalDateTime class
public class Main{
    public static void main(String[] args){
        LocalDateTime myObj = LocalDateTime.now();
        System.out.printlin(myObj);
    }
}
```
## Formatting Date and Time
The `"T"` in the example above is used to separate the date from the time.   
You can use the `DateTimeFormatter` class with the `ofPattern()` method in the   
same package to format or parse date-time objects. The following example will   
remove both the `"T"` and nanoseconds from the date-time:

```
import java.time.LocalDateTime; // Import the LocalDateTime class
import java.time.format.DateTimeFormatter; // Import the DateTimeFormatter class

public class Main {
  public static void main(String[] args) {
    LocalDateTime myDateObj = LocalDateTime.now();
    System.out.println("Before formatting: " + myDateObj);
    DateTimeFormatter myFormatObj = DateTimeFormatter.ofPattern("dd-MM-yyyy HH:mm:ss");

    String formattedDate = myDateObj.format(myFormatObj);
    System.out.println("After formatting: " + formattedDate);
  }
}
```
The `ofPattern()` method accepts all sorts of values, if you want to display the date   
and time in a different format.