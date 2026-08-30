const increase = document.getElementById("increase");
const decrease = document.getElementById("decrease");
const monitor = document.getElementById("monitor");
let value = Number(monitor.innerHTML);

const decreaseFunct = () => {
  if (value === 0) return;
  value--;
  monitor.innerHTML = value;
};

const increaseFunct = () => {
  value++;
  monitor.innerHTML = value;
};

increase.addEventListener("click", increaseFunct);
decrease.addEventListener("click", decreaseFunct);
