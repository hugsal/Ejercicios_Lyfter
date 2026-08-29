function wordCounter(letter) {
  const strings = letter
    .replace(/[.,\/#!$%\^&\*;:{}=\-_`~()¿?¡!]/g, "")
    .toLowerCase()
    .split(" ");

  const counter = {};

  for (const word of strings) {
    if (counter[word] === undefined) {
      counter[word] = 1;
      continue;
    }
    counter[word] = counter[word] + 1;
  }
  return counter;
}

const string = "This is a test. This test is simple.";
const counter = wordCounter(string);
console.log(counter);
