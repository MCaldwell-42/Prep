

const MultiplyFn = (x, y) => {
    let answer = 0;
    let i = 0;
    while (i < y) {
        answer += x;
        i++;
    }
    return `answer is ${answer}`;
};

MultiplyFn(6, 3);