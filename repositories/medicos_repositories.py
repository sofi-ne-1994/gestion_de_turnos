from db import get_connection

def obtener_medicos():
    conn=get_connection()
    cursor=conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM medicos")
    medicos= cursor.fetchall()

    cursor.close()
    conn.close()
    return medicos

    """
    Obtiene la lista completa de médicos registrados en la base de datos.

    Args:
        None

    Returns:
        list[dict]: Lista de médicos.
    """