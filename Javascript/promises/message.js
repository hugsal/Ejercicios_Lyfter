const words = ["very", "dogs", "cute", "are"];
const delays = [300, 100, 400, 200];
const output = [];

const promises = words.map((word, index) => {
  return new Promise((resolve) => {
    setTimeout(() => {
      output.push(word);
      resolve();
    }, delays[index]);
  });
});

await Promise.all(promises);

const sentence = output.join(" ");

console.log(sentence);
