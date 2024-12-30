// # Median of Two Sorted Arrays
// https://leetcode.com/problems/median-of-two-sorted-arrays/description/
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
    // use strict;
    var arr1 = []
    for(let i=0;i<=nums1.length-1;i++){
        arr1.push(nums1[i])
    }

    for(let i=0;i<=nums2.length-1;i++){
        arr1.push(nums2[i])
    }
    // console.log("arr1",arr1)
    // Now since arr1 may contain duplicates values we need to sort arr1 once and then find out the median

    var arr2 = arr1.sort(function(a,b){
        return (a-b)
    })
    console.log("arr2", arr2)
    // two cases for median when number of values in the array can be either even or odd. If odd then median value will be directly the middle value. 
// take the floor of array length divided by 2
    // If even then the median value will be value at array length divided by 2.
    // And array length value -1.
    // sum both values and divided by 2 again.
    var median1
    var median2
    var arr2Len = arr2.length
    // console.log("arr2 length", arr2Len)
    if(arr2Len % 2 !== 0){
        var index = Math.floor(arr2Len/2)
        // console.log("index",index)
        median1 = arr2[index]
        // console.log("median1",median1)
        return median1
    }else{
        var index1 = Math.floor(arr2Len/2)
        var valueAtIndex1 = arr2[index1]
        var valueAtIndexMinus1 = arr2[index1-1]
        median2 = (valueAtIndex1 + valueAtIndexMinus1)/2
        // console.log("median2",median2)
        return median2
    }    
};