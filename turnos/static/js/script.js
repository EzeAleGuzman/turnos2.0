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
   // Captura el evento de apertura del modal
$('#editarModal{{ turno.id }}').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget); // Botón que activó el modal
    var turnoId = button.data('turno-id');
    var turnoNombre = button.data('turno-nombre');
    var turnoApellido = button.data('turno-apellido');
    var turnoDni = button.data('turno-dni');
    var turnoMedico = button.data('turno-medico');
    var turnoHorario = button.data('turno-horario');

    // Actualiza los campos del formulario en el modal
    var modal = $(this);
    modal.find('[name="nombre"]').val(turnoNombre);
    modal.find('[name="apellido"]').val(turnoApellido);
    modal.find('[name="dni"]').val(turnoDni);
    modal.find('[name="medico"]').val(turnoMedico);
    modal.find('[name="horario"]').val(turnoHorario);
});


