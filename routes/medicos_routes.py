from flask import Blueprint, jsonify
from controllers.medicos_controller import get_medicos_controller

medicos_bp = Blueprint("medicos", __name__)
#Un Blueprint en Flask es una forma de organizar y modularizar una aplicación dividiéndola en partes independientes. Permite separar rutas en distintos archivos.


@medicos_bp.get("/medicos")
def get_medicos():
    response, status= get_medicos_controller()
    return jsonify(response), status

    """
    Endpoint que devuelve la lista de médicos disponibles.

    Args:
        None

    Returns:
        tuple[Response, int]: JSON con la lista de médicos y código HTTP.
    """