function reverse(value) {
  let newString = "";

  for (i = value.length - 1; i >= 0; i--) {
    newString += value[i];
  }

  return newString;
}

const string = "JavaScript";
const reverseString = reverse(string);
console.log(reverseString);
