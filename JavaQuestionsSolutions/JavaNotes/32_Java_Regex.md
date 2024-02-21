# Java Regular Expressions

## What is a Regular Expression?
1. A regular expression is a sequence of characters that forms a search pattern.  
2. When you search for data in a text, you can use this search pattern to describe what you are searching for.
3. A regular expression can be a single character, or a more complicated pattern.
4. Regular expressions can be used to perform all types of **text search** and **text replace** operations.
5. Java does not have a built-in Regular expression class,   
but we can import the   
`java.util.regex` package to work with regular expressions. The package includes the following classes:
* `Pattern Class` - Defines a pattern (to be used in a search)
* `Matcher Class` - Used to search for the pattern
* `PatternSyntaxException Class` - Indicates syntax error in a regular expression pattern

e.g.  Find out if there are any occurrences of the word "w3schools" in a sentence:

```
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Main {
  public static void main(String[] args) {
    Pattern pattern = Pattern.compile("w3schools", Pattern.CASE_INSENSITIVE);
    Matcher matcher = pattern.matcher("Visit W3Schools!");
    boolean matchFound = matcher.find();
    if(matchFound) {
      System.out.println("Match found");
    } else {
      System.out.println("Match not found");
    }
  }
}

// Output
Match found
```
**Explanation**
In this example, The word "w3schools" is being searched for in a sentence.

First, the pattern is created using the `Pattern.compile()` method. The first parameter   
indicates which pattern is being searched for and the second parameter has a flag to   
indicates that the search should be case-insensitive. The second parameter is optional.

The `matcher()` method is used to search for the pattern in a string. It returns a   
Matcher object which contains information about the search that was performed.  

The `find()` method returns true if the pattern was found in the string and false  
if it was not found



