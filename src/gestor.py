"""Módulo para gestionar artistas y canciones."""

def agregar_artista(diccionario, artista, canciones):
    """Agrega un nuevo artista con su lista de canciones."""
    if artista not in diccionario:
        diccionario[artista] = canciones

def agregar_cancion(diccionario, artista, cancion):
    """Agrega una canción a un artista existente."""
    if artista in diccionario:
        diccionario[artista].append(cancion)

def mostrar_canciones(diccionario, artista):
    """Devuelve la lista de canciones de un artista."""
    if artista in diccionario:
        return diccionario[artista]
    return "Artista no encontrado"

def buscar_cancion(diccionario, nombre_cancion):
    """Busca una canción y devuelve el artista que la canta."""
    for artista, canciones in diccionario.items():
        if nombre_cancion in canciones:
            return artista
    return "Canción no encontrada"
