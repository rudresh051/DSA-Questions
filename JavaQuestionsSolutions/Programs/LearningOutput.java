// https://www.geeksforgeeks.org/problems/learning-output4058/1?page=1&status=attempted&sortBy=difficulty
//{ Driver Code Starts
//Initial Template for Java

import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
    
    static String pos, neg, zero;
	public static void main(String[] args) throws IOException
	{
	        BufferedReader br =
            new BufferedReader(new InputStreamReader(System.in));
        int t =
            Integer.parseInt(br.readLine().trim()); // Inputting the testcases
        while(t-->0)
        {
            long n = Long.parseLong(br.readLine().trim());
            long a[] = new long[(int)(n)];
            // long getAnswer[] = new long[(int)(n)];
            String inputLine[] = br.readLine().trim().split(" ");
            for (int i = 0; i < n; i++) {
                a[i] = Long.parseLong(inputLine[i]);
            }
            
            
            Solution obj = new Solution();
            obj.Learning(a, n);
            
            System.out.println(pos);
            System.out.println(neg);
            System.out.println(zero);
            
        }
	}
}



// } Driver Code Ends


//User function Template for Java


class Solution {

    public void Learning(long arr[], long n)
    {
        // GFG.pos=1;
        // GFG.neg=2;
        // GFG.zero=3;
        // Your code goes here


         // Count variables for positive, negative, and zero integers
        int myPositiveCountIntegers = 0;
        int myNegativeCountIntegers = 0;
        int myZeroCountIntegers = 0;

        // Calculate counts of positive, negative, and zero integers
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] > 0) {
                myPositiveCountIntegers++;
            } else if (arr[i] < 0) {
                myNegativeCountIntegers++;
            } else {
                myZeroCountIntegers++;
            }
        }

        // Format the outputs based on the values
        GFG.pos = formatResult((double) n / myPositiveCountIntegers);
        GFG.neg = formatResult((double) n / myNegativeCountIntegers);
        GFG.zero = formatResult((double) n / myZeroCountIntegers);
    }

   
    private String formatResult(double value, int decimalPlaces) {
        if (value == (long) value) {
            return String.format("%.0f", value); // Format as integer if no decimal part
        } else {
            String format = "%." + decimalPlaces + "f";
            return String.format(format, value); // Format with the specified decimal places
        }
    }
   
   
   
   
   
   
}