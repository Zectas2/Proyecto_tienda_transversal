document.addEventListener('DOMContentLoaded', function() {
    var logoutLink = document.getElementById('logout');

    if (logoutLink) {
      logoutLink.addEventListener('click', function(event) {
        // Mostrar mensaje de confirmación nativo
        var confirmLogout = confirm('¿Seguro que deseas cerrar sesión?');

        if (!confirmLogout) {
          event.preventDefault(); // Evitar que se realice la acción de logout
        }
      });
    }
  });