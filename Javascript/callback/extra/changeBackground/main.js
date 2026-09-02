const colors = ["#FF5733", "#33FF57", "#3357FF", "#F5FF33", "#FF33F6"];

const square = document.getElementById("square");
const toggleButton = document.getElementById("toggle");
const colorText = document.getElementById("color-text");

function displayColorName(color) {
  colorText.textContent = `Color actual: ${color}`;
}

function getRandomColor(colorList, callback) {
  const index = Math.floor(Math.random() * colorList.length);
  const selectedColor = colorList[index];

  square.style.backgroundColor = selectedColor;

  callback(selectedColor);
}

toggleButton.addEventListener("click", () => {
  getRandomColor(colors, displayColorName);
});
