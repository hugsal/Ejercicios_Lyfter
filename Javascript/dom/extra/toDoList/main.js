const input = document.getElementById("input");
const addElementButton = document.getElementById("add-element");
const list = document.getElementById("list");

const addElement = () => {
  listLength = list.childElementCount;
  const value = input.value;
  if (value === "") return;
  const item = document.createElement("li");
  item.setAttribute("id", `element-${listLength + 1}`);
  const container = document.createElement("div");
  container.setAttribute("class", "list");
  const label = document.createElement("p");
  label.innerHTML = value;
  const button = document.createElement("button");
  button.setAttribute("id", listLength + 1);
  button.innerHTML = "Borrar";

  container.appendChild(label);
  container.appendChild(button);
  item.appendChild(container);
  list.appendChild(item);
  input.value = "";
};

document.addEventListener("click", (event) => {
  if (event.target.id === "add-element") {
    addElement();
    return;
  }

  const element = document.getElementById(`element-${event.target.id}`);
  element.remove();
});
