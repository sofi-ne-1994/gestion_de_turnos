#Aca se gestiona la lógica  relacionada con la reserva y consulta de turnos médicos.
from repositories.turnos_repositories import obtener_turnos_por_medico, existe_turno, crear_turno

#Obtiene una lista de los turnos que tiene un médico específico.
def listar_turnos_medico(medico_id):
    return obtener_turnos_por_medico(medico_id)
    """
    Servicio que obtiene los turnos asociados a un médico específico.

    Args:
        medico_id (int): ID del médico.

    Returns:
        list[dict]: Lista de turnos del médico.
    """

#Reserva un turno para un médico en una fecha y hora determinada.
#consulta si los datos ingresados por el usuario ya existen, de existir tira error  e indica que el turno no esta disponible, en caso que no exista un turno con los datos  que pide el usuario se crea un turno.
def reservar_turno(medico_id, fecha_hora, paciente):
    if existe_turno(medico_id,fecha_hora):
        return {"error": "turno no disponible"},400

    crear_turno(medico_id, fecha_hora, paciente)
    return {"message": "turno reservado exitosamente"},201

    
    """
    Servicio que gestiona la reserva de un turno médico.

    Verifica si el turno ya existe para el médico en la fecha y hora indicadas.
    Si el turno está ocupado, devuelve un error.
    Si no existe, crea el turno y devuelve confirmación.

    Args:
        medico_id (int): ID del médico.
        fecha_hora (str): Fecha y hora del turno.
        paciente (str): Nombre del paciente.

    Returns:
        tuple[dict, int]: Mensaje de éxito o error y código HTTP correspondiente.
    """
