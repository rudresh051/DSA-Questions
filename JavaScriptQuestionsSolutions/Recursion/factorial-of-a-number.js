function fact(n) {

    // BASE CONDITION
    if (n === 0)
        return 1;
    
    return n * fact(n - 1);
}

console.log("Factorial of 5 : " + fact(5));