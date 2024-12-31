// https://leetcode.com/problems/valid-parentheses/

/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    console.log("s",s)
    var s1 = s.split("")
    console.log("s1",s1)
    var stack = []
    var matchingBrackets = {
        ")" : "(",
        "}" : "{",
        "]" :"["
    }

    for(var i=0;i<=s1.length-1;i++){
        if(s1[i] == "(" || s1[i] == "{" || s1[i] == "["){
            stack.push(s1[i])
        }
        else if(s1[i] ==")" || s1[i] == "}" || s1[i] == "]"){
            if(stack.length==0 || stack.pop() !== matchingBrackets[s1[i]]){
                return false;
            }
        }
    }
   return stack.length ===0;
};