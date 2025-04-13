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