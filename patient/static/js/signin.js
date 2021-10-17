window.addEventListener('load', () => {

  const errorlist = document.querySelector('.errorlist')
  const msgElement = document.querySelector('.error-msg')
  if(errorlist) {
    msgElement.textContent = 'Please enter correct Username and Password'
  } else {
    msgElement.remove()
  }

  const usernameField = document.querySelector('#id_username')
  const passwordField = document.querySelector('#id_password')
  const submitButton = document.querySelector('.submit-btn')

  const validations = {
    isUsername: false,
    isPassword: false
  }

  const updateSubmitButtonStatus = () => {
    const validated = validations.isUsername && validations.isPassword
    submitButton.disabled = !validated
  }

  const checkUsername = () => {
    validations.isUsername = usernameField.value ? true : false
    updateSubmitButtonStatus()
  }

  const checkPassword = () => {
    validations.isPassword = passwordField.value ? true : false
    updateSubmitButtonStatus()
  }

  usernameField.addEventListener('blur', checkUsername)
  passwordField.addEventListener('blur', checkPassword)

})