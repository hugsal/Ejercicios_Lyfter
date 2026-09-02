function even() {
  console.log("The number is even!");
}

function odd() {
  console.log("The number is odd!");
}

function kindOfNumber(number, even, ood) {
  if (number % 2 === 0) {
    even();
  } else {
    ood();
  }
}

kindOfNumber(15, even, odd);
