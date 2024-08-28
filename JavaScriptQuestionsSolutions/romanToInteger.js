// https://leetcode.com/problems/roman-to-integer/

/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    var I = 1
    var V = 5
    var X = 10
    var L = 50
    var C = 100
    var D = 500
    var M = 1000
    var str1 = s.split("")
    var sum = 0
    for(var i=0;i<=str1.length-1;i++){
        // console.log("str1[i]",str1[i])
        if(str1[i]=='I'){
            // console.log("str1[i+1]",str1[i+1])
            if(str1[i+1]=='V'){
                sum = sum + 4
                i = i + 1
                continue
            }else if(str1[i+1]=='X'){
                sum = sum + 9
                i = i + 1
                continue
            }else{
                sum = sum + 1
            }
        }
        else if(str1[i] == 'V'){
            sum = sum + 5
        }
        else if(str1[i]== 'X'){
            if(str1[i+1]=='L'){
                sum = sum + 40
                i = i + 1
                continue
            }else if(str1[i+1]=='C'){
                sum = sum + 90
                i = i + 1
                continue
            }
            else{
            sum = sum + 10
            }

        }
        else if(str1[i]=='L'){
            sum = sum + 50
        }
        else if(str1[i]=='C'){
            if(str1[i+1]=='D'){
                sum = sum + 400
                i = i + 1
                continue
            }else if(str1[i+1]=='M'){
                sum = sum + 900
                i = i + 1
                continue
            }
            else{
             sum = sum + 100
            }
        }
        else if(str1[i]=='D'){
            sum = sum + 500
        }
        else if(str1[i]=='M'){
            sum = sum + 1000
        }
        // console.log("currentSum",sum)
    }
    
    return sum
};
