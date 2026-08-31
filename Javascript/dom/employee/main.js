const options = document.querySelectorAll('input[name="empleado"]');
const extraInput = document.getElementById("extra");
const extraLabel = document.getElementById("label-extra");

const updateExtraVisibility = () => {
  const selected = document.querySelector('input[name="empleado"]:checked');
  const hide = selected ? selected.value === "0" : false;
  extraInput.hidden = hide;
  extraLabel.hidden = hide;
};

updateExtraVisibility();

options.forEach((radio) => {
  radio.addEventListener("change", updateExtraVisibility);
});
