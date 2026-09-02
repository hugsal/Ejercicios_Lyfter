const colors = ["red", "blue", "green", "yellow", "cyan", "pink"];

const text = document.getElementById("text");
const toggleButton = document.getElementById("toggle");

toggleButton.addEventListener("click", () => {
  const index = Math.floor(Math.random() * colors.length);

  text.style.backgroundColor = colors[index];
});
