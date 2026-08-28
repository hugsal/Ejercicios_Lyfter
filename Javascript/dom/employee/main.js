const options = document.querySelectorAll('input[name="empleado"]');
const extraInput = document.getElementById("extra");
const extraLabel = document.getElementById("label-extra");

options.forEach((radio) => {
  radio.addEventListener("change", (event) => {
    const hide = event.target.value === "0";
    extraInput.hidden = hide;
    extraLabel.hidden = hide;
  });
});
