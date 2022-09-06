const validateSubmit = () => {
  const text = document.getElementById('text').value;
  const password = document.getElementById('password').value;

  if (text !== '' && password !== '') {
    document.querySelector('#submit').disabled = false;
  } else {
    document.querySelector('#submit').disabled = true;
  }
}

document.querySelectorAll('form input').forEach((input) => {
  input.addEventListener('keyup', validateSubmit);
});

document.querySelector('form').addEventListener('submit', (event) => {
  validateSubmit();
});