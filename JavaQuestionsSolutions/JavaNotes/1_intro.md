# Introduction to Java
1. It is an object oriented programming language
2. The Java platform provides a complete environment for application development  
on desktops and servers and deployment in embedded environments.
3. Java was developed by James Gosling in 1995, at Sun Microsystems which was  
later acquired by Oracle in 2010.
4. It was originally called OAK after an OAK tree that stood outside Gosling’s Office,  
later it was renamed “Green” and was finally renamed to “Java” inspired by Java  
Coffee, that’s why its logo looks like a cup of coffee. 

## Java Edition
We have 3 editions of Java for building a different kinds of applications
1. **Java Standard Edition (JSE)**
```
This is the core Java platform, it is a specification, which contains the core libraries to
develop standalone, networking, database, GUI, multithreaded types of applications.
In addition to the core API, the Java SE platform consists of the virtual machine,
Day1: Java Introduction 2
development tools, deployment technologies and other class libraries and toolkit
commonly used in Java application

```
2. **Java Enterprise Edition (JEE)**
```
The Java EE platform provides an API and runtime environment for developing and
running large-scale, multi-tiered, scalable, reliable, and secure network applications.
```
3. **Java Micro Edition (JME)**
```
It is a subset of Java SE, designed used for microdevices and embedded development
like mobile phones, sensors, micro-controller, TV set-top boxes etc.

```
## Features of Java
1. **Object-Oriented** - Java is object oriented, it supports all the OOPS characteristics.  
This makes java applications easy to develop and maintain, compared to structured  
programming language

2. **Portable and Platform Independent** - Java source code is compiled and  
converted into bytecode. this bytecode can run on multiple platforms i.e. Write Once  
and Run Anywhere(WORA), we can compile the java code in one Operating  
System and execute it on another Operating System.  

3. **Secure** - Java has provided an implicit component inside JVM in the form of a "Security Manager" to provide implicit security against malicious code.

4. **Robust** - Java is having a very good memory management system in the form of  
a heap memory management system.

5. **Multithreaded** - Java supports multithreading to enhance performance





## Variables
type variableName = value;
```
int myNum = 5;
float myFloatNum = 5.99f;
char myLetter = 'D';
boolean myBool = true;
String myText = "Hello";
```
### Declaring multiple variables
```
int x = 5, y = 6, z = 50;
System.out.println(x + y + z);
```  

```
int x, y, z;
x = y = z = 50;
System.out.println(x + y + z);
```  

**The general rules for naming variables are:**

Names can contain letters, digits, underscores, and dollar signs  
Names must begin with a letter  
Names should start with a lowercase letter and it cannot contain whitespace  
Names can also begin with $ and _ (but we will not use it in this tutorial)  
Names are case sensitive ("myVar" and "myvar" are different variables)  
Reserved words (like Java keywords, such as int or boolean) cannot be used as names  