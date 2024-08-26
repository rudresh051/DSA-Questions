// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

// You may assume that each input would have exactly one solution, and you may not use the same element twice.

// You can return the answer in any order.



/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    for(var i=0;i<=nums.length-1;i++){
        for(var j=i+1;j<=nums.length-1;j++){
            temp = nums[i] + nums[j]
            if(temp == target){
                indexFirst = i
                indexSecond = j
                arr = []
                arr.push(i)
                arr.push(j)
                return arr
            }
            else{
                continue
            }
        }
    }
};