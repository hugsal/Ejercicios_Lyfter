async function fetchData() {
  const response = await fetch("https://reqres.in/api/users/23");

  if (!response.ok) {
    throw new Error(`HTTP error! Status: ${response.statusText}`);
  }
}

fetchData().catch((error) => console.log(error.message));
