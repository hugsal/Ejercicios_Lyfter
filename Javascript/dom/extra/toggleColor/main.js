const colors = ["red", "blue", "green", "orange", "purple"];

const text = document.getElementById("text");
const toggleButton = document.getElementById("toggle");

toggleButton.addEventListener("click", () => {
  const index = Math.floor(Math.random() * colors.length);

  text.style.color = colors[index];
});
