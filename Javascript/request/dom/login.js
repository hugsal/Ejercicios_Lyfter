try {
  const user = localStorage.getItem("user");
  if (user) {
    window.location.href = "./profile.html";
  }
} catch (error) {
  alert(error.message);
}

const axiosInstance = axios.create({
  baseURL: "https://api.restful-api.dev",
  timeout: 1000,
  headers: { "content-type": "application/json" },
});

const form = document.getElementById("login-form");
const message = document.getElementById("login-message");

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const id = document.getElementById("login-id").value;
  const password = document.getElementById("login-password").value;
  let data = null;
  try {
    const response = await axiosInstance.get(`/objects/${id}`);
    data = response.data;
  } catch (error) {
    alert("Usuario o contraseña incorrectos");
    return;
  }

  if (data.data.password !== password) {
    alert("Usuario o contraseña incorrectos");
    return;
  }

  localStorage.setItem("user", JSON.stringify(data));
  window.location.href = "./profile.html";
});
