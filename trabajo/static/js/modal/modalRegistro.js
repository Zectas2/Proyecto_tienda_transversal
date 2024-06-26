document.addEventListener('DOMContentLoaded', function() {
  // Manejar evento click en el botón de registro para mostrar el modal
  var botonRegistro = document.getElementById('botonRegistro');
  if (botonRegistro) {
    botonRegistro.addEventListener('click', function(event) {
      event.preventDefault(); // Evitar que el formulario se envíe automáticamente

      var myModal = new bootstrap.Modal(document.getElementById('myModal'));
      myModal.show();
    });
  }

  // Manejar evento click en el botón "Aceptar" dentro del modal
  var modalAcceptButton = document.getElementById('modalAcceptButton');
  if (modalAcceptButton) {
    modalAcceptButton.addEventListener('click', function(event) {
      // Envía el formulario cuando se hace clic en "Aceptar"
      document.getElementById('registrationForm').submit();
    });
  }

  // Manejar evento click en el botón "Cancelar" dentro del modal
  var modalCloseButton = document.getElementById('modalCloseButton');
  if (modalCloseButton) {
    modalCloseButton.addEventListener('click', function(event) {
      // Cierra el modal cuando se hace clic en "Cancelar"
      var myModal = new bootstrap.Modal(document.getElementById('myModal'));
      myModal.hide();
    });
  }
});