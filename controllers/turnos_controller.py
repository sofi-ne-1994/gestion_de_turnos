from services.turnos_service import listar_turnos_medico, reservar_turno

def get_turnos_medico_controller(medico_id):
    turnos= listar_turnos_medico(medico_id)
    return turnos, 200
    """
    Controlador que obtiene los turnos de un médico específico.

    Args:
        medico_id (int): ID del médico.

    Returns:
        tuple[list[dict], int]: Lista de turnos y código HTTP 200.
    """

def crear_turno_controller(data):
    medico_id= data.get("medico_id")
    fecha_hora= data.get("fecha_hora")
    paciente= data.get("paciente")
    
    if not medico_id or not fecha_hora or not paciente:
        return {"error": "datos incompletos"}, 400
    
    return reservar_turno(medico_id, fecha_hora, paciente)
    
    """
    Controlador que valida los datos y gestiona la creación de un nuevo turno.

    Args:
        data (dict): Datos recibidos en el body de la petición en formato JSON.

    Returns:
        tuple[dict, int]: Mensaje de éxito o error y código HTTP correspondiente.
    """
