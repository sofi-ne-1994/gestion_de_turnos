from services.medicos_service import listar_medicos

def get_medicos_controller():
    medicos= listar_medicos()
    return medicos, 200

    """
    Controlador que obtiene la lista de médicos disponibles.

    Args:
        None

    Returns:
        tuple[list[dict], int]: Lista de médicos y código HTTP 200.
    """