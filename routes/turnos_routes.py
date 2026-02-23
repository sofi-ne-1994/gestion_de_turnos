
from flask import Blueprint, request, jsonify
from controllers.turnos_controller import get_turnos_medico_controller, crear_turno_controller

turnos_bp = Blueprint("turnos", __name__)
#pidiendo inormacion
@turnos_bp.get("/turnos/<int:medico_id>")
def get_turnos(medico_id):
    response, status= get_turnos_medico_controller(medico_id) 
    return jsonify(response), status

    """
        Endpoint que devuelve los turnos de un médico específico.

        Args:
            medico_id (int): ID del médico.

        Returns:
            tuple[Response, int]: JSON con la lista de turnos y código HTTP.
    """


#mandando informacion
@turnos_bp.post("/turnos")
def post_turno():
    response, status= crear_turno_controller(request.get_json())
    return jsonify(response), status

    """
    Endpoint que permite crear un nuevo turno médico.

    Args:
        None: Los datos se reciben en el cuerpo de la petición (JSON).

    Body (JSON):
        medico_id (int): ID del médico.
        fecha_hora (str): Fecha y hora del turno.
        paciente (str): Nombre del paciente.

    Returns:
        tuple[Response, int]: Mensaje de confirmación o error y código HTTP.
    """

