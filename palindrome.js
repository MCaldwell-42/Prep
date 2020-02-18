
const Palindrome = (string) => {
    let word1 = string.toLowerCase();
    let word2 = word1.split("").reverse().join("");
    if (word1 == word2) {
        return true
    } else {
        return false
    }
};

Palindrome("racecar");