document.addEventListener('DOMContentLoaded', function () {

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
})
});