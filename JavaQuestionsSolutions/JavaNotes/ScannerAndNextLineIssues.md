# Why is Scanner skipping nextLine() after use of other next functions?

https://www.geeksforgeeks.org/why-is-scanner-skipping-nextline-after-use-of-other-next-functions/?ref=rp

When you use methods like next(), nextInt(), nextDouble(), etc. in Java's Scanner class   
to read input, they typically only consume the input up to the delimiter, which is usually  
whitespace. However, the nextLine() method reads the rest of the current line after any  
 tokens have been read.

So, if you use next(), nextInt(), or similar methods followed by nextLine(), the nextLine()  
call will consume the newline character left behind by the previous method, resulting in  
seemingly skipped input.

To avoid this, you can either use nextLine() after using methods like nextInt() to consume the  
newline character, or you can call nextLine() twice - once to consume the leftover newline character   
and once to read the actual input line.



