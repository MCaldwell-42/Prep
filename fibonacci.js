const fibonnaci = n => {
    let fib = 0;
    let last_ans = 0;
    let next_ans = 1;
    if ( n === 1 ){
        return 0
    } else if ( n === 2 ) {
        return 1
    } else {
    for (i=3; i <= n; i++) {
        fib = last_ans + next_ans;
        last_ans = next_ans;
        next_ans = fib;
    }
    }
    return fib;
}

fibonnaci(4);


const fibonacci_2 = num => {
    // store the Fibonacci sequence you're going
    // to generate inside an array and
    // initialize the array with the first two
    // numbers of the sequence
    const result = [0, 1]
  
    for(let i = 2; i <= num; i++) {
      // push the sum of the two numbers
      // preceding the position of i in the result array
      // at the end of the result array
      const prevNum1 = result[i - 1]
      const prevNum2 = result[i - 2]
      result.push(prevNum1 + prevNum2)
    }
    // return the last value in the result array
    return result[num]
  }

  const fibonacci_3 = num => {
    // if num is either 0 or 1 return num
    if(num < 2) {
      return num
    }
    // recursion here
    return fibonacci_3(num - 1) + fibonacci_3(num - 2)
  }