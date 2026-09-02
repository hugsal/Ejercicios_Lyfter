const showButton = document.getElementById("add-content");
const input = document.getElementById("input-data");
const output = document.getElementById("output-data");

const showData = () => {
  const data = input.value;
  input.value = "";
  output.innerHTML = data;
};

showButton.addEventListener("click", showData);
