# Var-args

In Java, **var-args** (short for **variable-length arguments**) is a feature that allows you to pass **zero or more arguments** of the **same type** to a method.

It is denoted using **three dots (`...`)** after the data type in the method parameter.


### ✅ Syntax:

```java
returnType methodName(dataType... variableName)
```

---

### ✅ Example:

```java
public class Example {
    static void printNumbers(int... numbers) {
        for (int num : numbers) {
            System.out.print(num + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        printNumbers();               // No arguments
        printNumbers(10);             // One argument
        printNumbers(1, 2, 3, 4, 5);  // Multiple arguments
    }
}
```

**Output:**

```
 
10 
1 2 3 4 5 
```

---

### 🔍 Key Points:

* Internally, the var-args parameter is treated as an **array**.
* Only **one var-args parameter** is allowed per method.
* It must be the **last parameter** in the method signature.

---

### ❌ Invalid Examples:

```java
// Error: Var-args must be last
void test(int... nums, String str) {}

// Error: Only one var-args allowed
void test(int... nums, String... names) {}
```

---

### ✅ Valid Combination:

```java
void test(String name, int... scores) {}
```


