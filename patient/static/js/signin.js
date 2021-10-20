window.addEventListener('load', () => {

  const errorlist = document.querySelector('.errorlist')
  const msgElement = document.querySelector('.error-msg')
  if(errorlist) {
    msgElement.textContent = 'Please enter correct Username and Password'
  } else {
    msgElement.remove()
  }

})