const numbers = [1, 2, 3, 2, 4, 1, 5];

const setNumbers = [];

for (const number of numbers) {
  if (setNumbers.includes(number)) continue;
  setNumbers.push(number);
}

console.log(setNumbers);
