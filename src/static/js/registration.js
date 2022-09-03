const Patterns = {
  firstName: /^[a-zA-ZÀ-ÿ\s]{1,12}$/,
  lastName: /^[a-zA-ZÀ-ÿ\s]{1,12}$/,
  email: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{1,255}$/,
  username: /^[a-z0-9\_\-]{4,16}$/,
  password: /^.{4,32}$/
}

const Status = {
  firstName: false,
  lastName: false,
  email: false,
  username: false,
  password: false
}

const validateForm = (event) => {
  switch (event.target.name) {
    case 'firstName':
      validateField(Patterns.firstName, event.target, 'firstName');
      break;
    case 'lastName':
      validateField(Patterns.lastName, event.target, 'lastName');
      break;
    case 'email':
      validateField(Patterns.email, event.target, 'email');
      break;
    case 'username':
      validateField(Patterns.username, event.target, 'username');
      break;
    case 'password':
      validateField(Patterns.password, event.target, 'password');
      validatePassword();
      break;
    case 'repeatPassword':
      validatePassword();
      break;
  }
  validateSubmit();
}

const validateField = (pattern, input, field) => {
  if (pattern.test(input.value)) {
    document.getElementById(`${field}Container`).classList.remove('incorrect');
    document.querySelector(`#${field}Container .inputMessage`).classList.remove('showMessage');
    document.getElementById(`${field}Container`).classList.add('correct');
    Status[field] = true;
  } else {
    document.getElementById(`${field}Container`).classList.remove('correct');
    document.getElementById(`${field}Container`).classList.add('incorrect');
    document.querySelector(`#${field}Container .inputMessage`).classList.add('showMessage');
    Status[field] = false;
  }
}

const validatePassword = () => {
  const password = document.getElementById('password').value;
  const repeatPassword = document.getElementById('repeatPassword').value;

  if (password === repeatPassword) {
    document.getElementById('repeatPasswordContainer').classList.remove('incorrect');
    document.querySelector('#repeatPasswordContainer .inputMessage').classList.remove('showMessage');
    document.getElementById('repeatPasswordContainer').classList.add('correct');
    Status['password'] = true
  } else {
    document.getElementById('repeatPasswordContainer').classList.remove('correct');
    document.getElementById('repeatPasswordContainer').classList.add('incorrect');
    document.querySelector('#repeatPasswordContainer .inputMessage').classList.add('showMessage');
    Status['password'] = false;
  }
}

const validateSubmit = () => {
  let validateStatus = false;
  for (let field in Status) { validateStatus += Status[field]; }

  if (validateStatus && document.getElementById('check').checked) {
    document.querySelector('#submit').disabled = false;
  } else {
    document.querySelector('#submit').disabled = true;
  }
}

document.querySelectorAll('form input').forEach((input) => {
  input.addEventListener('keyup', validateForm);
  input.addEventListener('blur', validateForm);
  input.addEventListener('click', validateSubmit);
});

document.querySelector('form').addEventListener('submit', (event) => {
  document.querySelector('form').reset();

  document.querySelectorAll('.correct').forEach((event) => {
    event.classList.remove('correct');
  });

  for (let field in Status) { Status[field] = false; }
  validateSubmit();
});