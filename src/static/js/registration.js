const Patterns = {
  firstName: /^[a-zA-ZÀ-ÿ]{1,12}$/,
  lastName: /^[a-zA-ZÀ-ÿ]{1,12}$/,
  email: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{1,255}$/,
  username: /^[a-z0-9\_\-]{4,16}$/,
  securityKey: /^[a-zA-ZÀ-ÿ]{1,12}$/,
  cardNumber: /^[0-9]{12,19}$/,
  cardName: /^[A-ZÀ-Ö\ ]{1,20}$/,
  ccv: /^[0-9]{3}$/
}

const Status = {
  firstName: 0,
  lastName: 0,
  email: 0,
  username: 0,
  securityKey: 0,
  cardNumber: 0,
  cardName: 0,
  expiration: 0,
  ccv: 0
}

const validateInput = (event) => {
  switch (event.target.name) {
    case "firstName":
      validateField(Patterns.firstName, event.target, "firstName");
      break;
    case "lastName":
      validateField(Patterns.lastName, event.target, "lastName");
      break;
    case "email":
      validateField(Patterns.email, event.target, "email");
      break;
    case "username":
      validateField(Patterns.username, event.target, "username");
      break;
    case "key1":
      validateSecurity(Patterns.securityKey, "securityKey");
      break;
    case "key2":
      validateSecurity(Patterns.securityKey, "securityKey");
      break;
    case "key3":
      validateSecurity(Patterns.securityKey, "securityKey");
      break;
    case "cardNumber":
      validateField(Patterns.cardNumber, event.target, "cardNumber");
      break;
    case "cardName":
      validateField(Patterns.cardName, event.target, "cardName");
      break;
    case "ccv":
      validateField(Patterns.ccv, event.target, "ccv");
  }
  validateSubmit();
}

const validateSelect = (event) => {
  switch (event.target.name) {
    case "month":
      validateExpiration("expiration");
      break;
    case "year":
      validateExpiration("expiration");
      break;
  }
  validateSubmit();
}

const validateField = (pattern, input, field) => {
  if (pattern.test(input.value)) {
    document.getElementById(`${field}Container`).classList.remove("incorrect");
    document.querySelector(`#${field}Container .inputMessage`).classList.remove("showMessage");
    document.getElementById(`${field}Container`).classList.add("correct");
    Status[field] = 1;
  } else {
    document.getElementById(`${field}Container`).classList.remove("correct");
    document.getElementById(`${field}Container`).classList.add("incorrect");
    document.querySelector(`#${field}Container .inputMessage`).classList.add("showMessage");
    Status[field] = 0;
  }
}

const validateSecurity = (pattern, field) => {
  if (pattern.test(key1.value) && pattern.test(key2.value) && pattern.test(key3.value)) {
    document.getElementById(`${field}Container`).classList.remove("incorrect");
    document.querySelector(`#${field}Container .inputMessage`).classList.remove("showMessage");
    document.getElementById(`${field}Container`).classList.add("correct");
    Status[field] = 1;
  } else {
    document.getElementById(`${field}Container`).classList.remove("correct");
    document.getElementById(`${field}Container`).classList.add("incorrect");
    document.querySelector(`#${field}Container .inputMessage`).classList.add("showMessage");
    Status[field] = 0;
  }
}

const validateExpiration = (field) => {
  if (month.value !== "Month" && year.value !== "Year") {
    document.getElementById(`${field}Container`).classList.remove("incorrect");
    document.querySelector("#expirationContainer .inputMessage").classList.remove("showMessage");
    document.getElementById(`${field}Container`).classList.add("correct");
    Status[field] = 1;
  } else {
    document.getElementById(`${field}Container`).classList.remove("correct");
    document.getElementById(`${field}Container`).classList.add("incorrect");
    document.querySelector("#expirationContainer .inputMessage").classList.add("showMessage");
    Status[field] = 0;
  }
}

const validateSubmit = () => {
  let validateStatus = 0, statusCounter = 0;
  for (let field in Status) { 
    validateStatus += Status[field];
    statusCounter++;
  }

  if (validateStatus === statusCounter && document.getElementById("check").checked) {
    document.querySelector("#submit").disabled = false;
  } else {
    document.querySelector("#submit").disabled = true;
  }
}

// * Select month content.
for(let i = 1; i <= 12; i++){
	let option = document.createElement('option');
	option.value = i;
	option.innerText = i;
	document.querySelector('#month').appendChild(option);
}

// * Select year content.
const dateYear = new Date().getFullYear() + 1;
for(let i = dateYear; i <= dateYear + 11; i++){
	let option = document.createElement('option');
	option.value = i;
	option.innerText = i;
	document.querySelector('#year').appendChild(option);
}

document.querySelectorAll("form input").forEach((input) => {
  input.addEventListener("keyup", validateInput);
  input.addEventListener("blur", validateInput);
  input.addEventListener("click", validateSubmit);
});

document.querySelectorAll("form select").forEach((select) => {
  select.addEventListener("keyup", validateSelect);
  select.addEventListener("click", validateSelect);
  select.addEventListener("click", validateSubmit);
});

document.querySelector("form").addEventListener("submit", () => {
  document.querySelectorAll(".correct").forEach((event) => {
    event.classList.remove("correct");
  });

  for (let field in Status) { Status[field] = 0; }
  validateSubmit();
});

document.querySelector("#next").addEventListener("click", () => {
  document.getElementById("next").classList.add("hide");
  document.getElementById("personalSection").classList.add("hide");
  document.getElementById("back").classList.remove("hide");
  document.getElementById("paymentSection").classList.remove("hide");
});

document.querySelector("#back").addEventListener("click", () => {
  document.getElementById("back").classList.add("hide");
  document.getElementById("paymentSection").classList.add("hide");
  document.getElementById("next").classList.remove("hide");
  document.getElementById("personalSection").classList.remove("hide");
});