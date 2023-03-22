imgInp.onchange = evt => {
  const [file] = imgInp.files
  if (file) {
    register-user-photo.src = URL.createObjectURL(file)
  }
}
