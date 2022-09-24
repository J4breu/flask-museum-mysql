const validateSubmit = () => {
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  if (email !== "" && password !== "") {
    document.querySelector("#submit").disabled = false;
  } else {
    document.querySelector("#submit").disabled = true;
  }
}

document.querySelectorAll("form input").forEach((input) => {
  input.addEventListener("keyup", validateSubmit);
});

document.querySelector("form").addEventListener("submit", (event) => {
  validateSubmit();
});

const warning = document.querySelector("#warningMessage").textContent

if (warning === "") {
  document.querySelector("#warningMessage").classList.remove("showMessage");
} else {
  document.querySelector("#warningMessage").classList.add("showMessage");
}