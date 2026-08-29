function eraseDuplicates(numbers) {
  const setNumbers = [];

  for (const number of numbers) {
    if (setNumbers.includes(number)) continue;
    setNumbers.push(number);
  }
  return setNumbers;
}

const numbers = [1, 2, 3, 2, 4, 1, 5];
const cleanNumbers = eraseDuplicates(numbers);
console.log(cleanNumbers);
