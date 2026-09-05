const profileId = document.getElementById("profile-id");
const profileName = document.getElementById("profile-name");
const profileEmail = document.getElementById("profile-email");
const logoutBtn = document.getElementById("logout-btn");

try {
  const user = localStorage.getItem("user");
  console.log(user);
  if (user === null) {
    window.location.href = "./register.html";
  } else {
    const userData = JSON.parse(user);

    profileId.textContent = userData.id;
    profileName.textContent = userData.name;
    profileEmail.textContent = userData.data.email;
  }
} catch (error) {
  alert(error.message);
}

const logout = () => {
  localStorage.removeItem("user");
  window.location.href = "./login.html";
};

logoutBtn.addEventListener("click", logout);
