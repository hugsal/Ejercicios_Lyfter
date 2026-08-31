const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

const pairs = [];
for (const number of numbers) {
  if (number % 2 === 0) {
    pairs.push(number);
  }
}

const pairs2 = numbers.filter((number) => number % 2 === 0);

console.log(pairs);
console.log(pairs2);
