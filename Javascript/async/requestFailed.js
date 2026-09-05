async function fetchData() {
  try {
    const response = await fetch("https://reqres.in/api/users/23");

    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.statusText}`);
    }

    const data = await response.json();
  } catch (error) {
    console.log("Caught an error:", error.message);
  }
}

const data = fetchData();
