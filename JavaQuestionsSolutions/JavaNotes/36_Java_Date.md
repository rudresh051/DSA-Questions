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
