window.addEventListener('load', () => {

  const usernameField = document.querySelector('#id_username')
  const emailField = document.querySelector('#id_email')
  const confirmPasswordField = document.querySelector('#id_password2')
  const submitButton = document.querySelector('.submit-btn')

  const validations = {
    avaiableUsername: false,
    isEmail: false,
    matchPassword: false
  }

  const updateSubmitButtonStatus = () => {
    const validated = validations.avaiableUsername && validations.matchPassword && validations.isEmail
    submitButton.disabled = !validated
  }

  const clearErrorMessage = () => {
    const errorMessage = document.querySelector('.error-message')
    if(errorMessage) errorMessage.remove()
  }

  const showUnavailableMessage = () => {
    const message = "<p class='error error-message'>Username is not available<p/>"
    usernameField.insertAdjacentHTML('afterend', message)
  }

  const checkUsernameAvailibility = async () => {
    const baseURL = window.location.origin
    const desiredUsername = usernameField.value

    if(!usernameField.value) return

    const response = await (await fetch(`${baseURL}/api/checkUsername/${desiredUsername}`)).json()

    if(!response.isAvailable) {
      showUnavailableMessage()
      validations.avaiableUsername = false
      updateSubmitButtonStatus()
    } else {
      validations.avaiableUsername = true
      updateSubmitButtonStatus()
    }

  }

  const checkEmail = () => {
    validations.isEmail = emailField.value ? true : false
  }

  const checkPasswordMatch = () => {
    const password1 = document.querySelector('#id_password1').value
    const password2 = confirmPasswordField.value
    validations.matchPassword = password1 === password2 && password1.length ? true : false
    updateSubmitButtonStatus()
  }
  
  usernameField.addEventListener('blur', checkUsernameAvailibility)
  usernameField.addEventListener('focus', clearErrorMessage)
  emailField.addEventListener('blur', checkEmail)
  confirmPasswordField.addEventListener('blur', checkPasswordMatch)

})