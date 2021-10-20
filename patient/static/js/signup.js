window.addEventListener('load', () => {

  const usernameField = document.querySelector('#id_username')
  const emailField = document.querySelector('#id_email')
  const confirmPasswordField = document.querySelector('#id_password1')

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
    }

  }

  const checkPasswordMatch = () => {
    const password = document.querySelector('#id_password1').value
    const username = usernameField.value
    const messages = []
    if(password.length < 8 ) messages.push(`<p class='error error-message'>Your password must contain at least 8 characters.<p/>`)
    if(password == username ) messages.push(`<p class='error error-message'>Your password can’t be too similar to your other personal information.<p/>`)

    messages.forEach(message => {
      confirmPasswordField.insertAdjacentHTML('afterend', message)
    })
  }
  
  usernameField.addEventListener('blur', checkUsernameAvailibility)
  confirmPasswordField.addEventListener('blur', checkPasswordMatch)
  usernameField.addEventListener('focus', clearErrorMessage)
  confirmPasswordField.addEventListener('focus', clearErrorMessage)

})