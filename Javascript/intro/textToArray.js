const example = "This is a string!";

const words = [];
let word = "";
for (const char of example) {
  if (char !== " ") {
    word += char;
  } else {
    words.push(word);
    word = "";
  }
}
if (word.length > 0) words.push(word);
console.log(words);
