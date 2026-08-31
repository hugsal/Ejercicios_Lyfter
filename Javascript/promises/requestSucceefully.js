async function fetchData() {
  const response = await fetch("https://reqres.in/api/users/2");
  const { data } = await response.json();
  return data;
}

fetchData().then((data) => console.log(data));
