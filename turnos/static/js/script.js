document.addEventListener('DOMContentLoaded', function () {
    // Abrir y cerrar el menú desplegable
    //creo una variable para cada elemento que quiero interactuar del html
    const menuButton = document.querySelector('.mobile-menu-button');
    const dropdown = document.querySelector('.dropdown');
    const backdrop = document.querySelector('.dropdown-backdrop');
    const closeButtons = document.querySelectorAll('.close-button');

    //creo un evento para esperar el click sobre menuButton para poder mostar el menu desplegable
    menuButton.addEventListener('click', function () {
        dropdown.style.transform = 'translateX(0)';
        backdrop.style.opacity = '1';
        backdrop.style.pointerEvents = 'auto';
    });

    // Evento para cerrar el menú desplegable al hacer clic en el fondo oscuro
    backdrop.addEventListener('click', function () {
        dropdown.style.transform = 'translateX(-100%)';
        backdrop.style.opacity = '0';
        backdrop.style.pointerEvents = 'none';
    });

    // Aqui lo hacemos a la inversa usamos el evento click del boton para cerrar el menu
    closeButtons.forEach(function (closeButton) {
        closeButton.addEventListener('click', function () {
            dropdown.style.transform = 'translateX(-100%)';
            backdrop.style.opacity = '0';
            backdrop.style.pointerEvents = 'none';
        });
    });
});



