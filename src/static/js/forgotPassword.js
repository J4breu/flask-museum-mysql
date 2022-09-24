const validateSubmit = () => {
  const email = document.getElementById("email").value;
  const key1 = document.getElementById("key1").value;
  const key2 = document.getElementById("key2").value;
  const key3 = document.getElementById("key3").value;

  if (email && key1 && key2 && key3 ) {
    document.querySelector("#submit").disabled = false;
  } else {
    document.querySelector("#submit").disabled = true;
  }
}

document.querySelectorAll("form input").forEach((input) => {
  input.addEventListener("keyup", validateSubmit);
  input.addEventListener("blur", validateSubmit);
});

document.querySelector("form").addEventListener("submit", () => {
  validateSubmit();
});

const warning = document.querySelector("#warningMessage").textContent

if (warning === "") {
  document.querySelector("#warningMessage").classList.remove("showMessage");
} else {
  document.querySelector("#warningMessage").classList.add("showMessage");
}