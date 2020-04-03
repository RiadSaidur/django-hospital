window.addEventListener('load', () => {

  const burger = document.querySelector('aside img')
  const divs = document.querySelectorAll('nav div')
  const divArray = [...divs]

  burger?.addEventListener('click', () => {
    divArray.forEach(div => div.classList.toggle('menu'))
  })

  document
    .querySelector('main')
    .addEventListener('click', () => {
      divArray.forEach(div => div.classList.remove('menu'))
    })

})