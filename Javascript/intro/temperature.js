const celsiusDegrees = [0, 30, 50, 100];

const fahrenheitDegrees = celsiusDegrees.map(
  (temperature) => temperature * (9 / 5) + 32,
);

console.log(fahrenheitDegrees);
