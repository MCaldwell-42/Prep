const buildCharObj = str => {
    CharObj = {};
    for(let char of str.replace(/[^\w]/g).toLowerCase()) {
        // if the object has already a key value pair
        // equal to the value being looped over,
        // increase the value by 1, otherwise add
        // the letter being looped over as key and 1 as its value
        CharObj[char] = CharObj[char] + 1 || 1
      }
      return CharObj
    }


const isAnagram = (word1, word2) => {
    const CharObjA = buildCharObj(word1);
    const CharObjB = buildCharObj(word2);
    
    if(Object.keys(CharObjA).length !== Object.keys(CharObjB).length) {
        return false
      }

    for(let char in CharObjA) {
        if(CharObjA[char] !== CharObjB[char]){
            return false
        }
    }
    return true
};

isAnagram("beetle", "eteebl");