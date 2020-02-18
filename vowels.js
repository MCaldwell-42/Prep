
const vowelsCheck = str => {
    const vowelsArray= str.split("");
    let i=0;
    for(let letter of vowelsArray) {
        if (letter === "a") {
            i += 1;
        } else if (letter === "e") {
            i += 1;
        }
         else if (letter === "i") {
            i += 1;
        }
         else if (letter === "o") {
            i += 1;
        }
         else if (letter === "u") {
            i += 1;
        }
    }
    return i;
}

vowelsCheck("beetle");


const findVowels = str => {
    let count = 0
    const vowels = ['a', 'e', 'i', 'o', 'u']
    for(let char of str.toLowerCase()) {
      if(vowels.includes(char)) {
        count++
      }
    }
    return count
  };


  const findVowels = str => {
    const matched = str.match(/[aeiou]/gi)
    return matched ? matches.length : 0
  };