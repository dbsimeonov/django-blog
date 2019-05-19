/*
 * Declaring variables.
 */
const titleInput = document.querySelector('input[name=title]')
const slugInput = document.querySelector('input[name=slug]')

/**
 * Slugify regex
 * @param  {String}
 * @return {String}
 */
const slugify = val => val.toString().toLowerCase().trim().replace(/&/g, '-and-').replace(/[\s\W-]+/g, '-')

/**
 * Slugifying event listener.
 * @param  {event}
 */
titleInput.addEventListener('keyup', e => {
  slugInput.setAttribute('value', slugify(titleInput.value))
})