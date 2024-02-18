# Java Abstraction
Imagine you're building a house. You know you want a door to get in and out,  
but you don't need to know how the door was made or what materials were used.   
You only need to know how to use it: push or pull to open or close it.

In Java, abstraction is like that door. It hides the complex inner workings of   
something and provides a simplified interface for you to interact with.   
You don't need to know all the nitty-gritty details of how a particular   
piece of code works; you just need to know how to use it. This makes programming   
more manageable because you can focus on what you need to do rather than how it's   
being done behind the scenes.


## Abstract Classes and Methods
Data **abstraction** is the process of hiding certain details and showing only   
essential information to the user.  
Abstraction can be achieved with either **abstract classes** or **interfaces**.

The `abstract` keyword is a non-access modifier, used for classes and methods:
* **Abstract class:** is a restricted class that cannot be used to create objects   
(To access it, it must be inherited from another class).   
* **Abstract method:** can only be used in an abstract class, and it does not have a body. The body is provided by the subclass (inherited from).

