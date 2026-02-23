from db import get_connection

def obtener_turnos_por_medico(medico_id):
    conn=get_connection()
    cursor=conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM turnos WHERE medico_id = %s",(medico_id,))

    turnos= cursor.fetchall()

    cursor.close()
    conn.close()

    return turnos
    """
    Obtiene los turnos asociados a un médico específico desde la base de datos.

    Args:
        medico_id (int): ID del médico.

    Returns:
        list[dict]: Lista de turnos del médico.
    """


def existe_turno(medico_id, fecha_hora):
    conn=get_connection()
    cursor=conn.cursor(dictionary=True)

    cursor.execute("SELECT id FROM turnos WHERE medico_id = %s AND fecha_hora = %s",(medico_id, fecha_hora))

    turno= cursor.fetchone()

    cursor.close()
    conn.close()

    return turno 

    """
    Verifica si ya existe un turno para un médico en una fecha y hora determinada.

    Args:
        medico_id (int): ID del médico.
        fecha_hora (str): Fecha y hora del turno.

    Returns:
        dict | None: Datos del turno si existe, o None si no existe.
    """

def crear_turno(medico_id, fecha_hora, paciente):
    conn=get_connection()
    cursor=conn.cursor()

    cursor.execute("INSERT INTO turnos (fecha_hora, nombre_paciente, medico_id) VALUES (%s, %s, %s)", (fecha_hora, paciente, medico_id))
    conn.commit()

    cursor.close()
    conn.close()

    """
    Crea un nuevo turno en la base de datos.

    Args:
        medico_id (int): ID del médico.
        fecha_hora (str): Fecha y hora del turno.
        paciente (str): Nombre del paciente.

    Returns:
        None
    """
