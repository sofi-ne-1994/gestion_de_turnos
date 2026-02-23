from repositories.medicos_repositories import obtener_medicos

def listar_medicos():
    return obtener_medicos()
    """
    Servicio que obtiene la lista de médicos disponibles.

    Args:
        None

    Returns:
        list[dict]: Lista de médicos obtenidos desde el repositorio.
    """