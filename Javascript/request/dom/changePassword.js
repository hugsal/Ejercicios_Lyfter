const axiosInstance = axios.create({
  baseURL: "https://api.restful-api.dev",
  timeout: 1000,
  headers: { "content-type": "application/json" },
});

const form = document.getElementById("change-password-form");

form.addEventListener("submit", async (e) => {
  e.preventDefault();

  const id = document.getElementById("change-user-id").value;
  const oldPassword = document.getElementById("old-password").value;
  const newPassword = document.getElementById("new-password").value;
  const confirmPassword = document.getElementById("confirm-password").value;

  if (newPassword !== confirmPassword) {
    alert("Las contraseñas no coinciden");
    return;
  }

  const { data: user } = await axiosInstance.get(`/objects/${id}`);

  if (!user) {
    alert("Usuario no encontrado");
    return;
  }

  if (user.data.password !== oldPassword) {
    alert("Contraseña anterior incorrecta");
    return;
  }

  user.data.password = newPassword;
  user.name = "Lilo5";
  user.data.email = "tu@yo.com";

  await axiosInstance.put(`/objects/${id}`, user);

  alert("Contraseña cambiada exitosamente");
});
const user = { name, data: { email, password } };
