function positive(number) {
  console.log(`Valid number: ${number}`);
}

function negativeOrZero(number) {
  console.log(`Invalid number: ${number}`);
}

function kindOfNumber(number, positive, negativeOrZero) {
  if (number > 0) {
    positive(number);
  } else {
    negativeOrZero(number);
  }
}

kindOfNumber(0, positive, negativeOrZero);
