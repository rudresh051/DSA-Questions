// https://leetcode.com/problems/palindrome-number/description/
/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    var y = x.toString();
    // console.log(typeof(y))
    var z = y.split("")
    var str1 = z.join("")
    // console.log("str1",str1)
    // console.log("z", z)
    var arr1 = []
    var size = z.length;
    // console.log("size",size)
    for(var i=size-1;i>=0;i--){
        arr1.push(z[i])
    }
    // console.log("arr1",arr1)
    var str2 = arr1.join("")
    // console.log("str2",str2)
    if(str1==str2){
        return true
    }
    else{
        return false
    }  
};