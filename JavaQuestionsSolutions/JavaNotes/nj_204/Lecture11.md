# Array

example - 

```java
class ArrayExamples
{
	public static void main(String[] args) 
	{
		int a=10;
		int[] array = new int[10];

		int[] array2 = {10,30,40};
		
		// index start with 0

		/*int value = array2[2];
		System.out.println(value);
		System.out.println(array2.length);*/

        // for loop
		for(int i=0; i<array2.length;i++){
			System.out.println(array2[i]);
		}

		// for each loop
		for(int val : array2){
			System.out.println(val);
		}	

        		
		// in reverse order
		for(int i=array2.length-1; i>=0;i--){
			System.out.println(array2[i]);
		}

        // sum of array
		int sum = 0;
		for(int data : array2){
			sum = sum + data;
		}
		System.out.println("sum = " + sum);

	}
}
```

## Multi Dimension Array
example - 

```java
class MultiDimArray 
{
	public static void main(String[] args) 
	{
		// Single
		int[] array = new int[10];
		int[][] multiArray = new int[3][3];

		int[][] multiDimen2 = {
			{1,2,3}, // 00 01 02
			{4,5,6}, // 10 11 12
			{7,8,9}	 // 20 21 22
		};

		// to access 7
		System.out.println(multiDimen2[2][0]);
	}
}
```
