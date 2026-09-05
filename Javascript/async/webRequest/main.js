const input = document.getElementById("userId");
const button = document.getElementById("fetchDataBtn");
const result = document.getElementById("result");

async function fetchData(userId) {
  const response = await fetch(`https://reqres.in/api/users/${userId}`);

  if (!response.ok) {
    throw new Error(`HTTP error! Status: ${response.status}`);
  }

  return response.json();
}

button.addEventListener("click", async () => {
  try {
    const { data } = await fetchData(input.value);
    const { first_name, last_name, email } = data;
    result.textContent = `Name: ${first_name} ${last_name}\nEmail: ${email}`;
    result.style.color = "black";
  } catch (error) {
    result.textContent = error.message;
    result.style.color = "red";
  }
});
