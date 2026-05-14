"""Programa principal para gestionar artistas."""
from src.gestor import agregar_artista, agregar_cancion, mostrar_canciones, buscar_cancion

def main():
    # Crear diccionario vacío
    artistas = {}

    # Agregar artistas
    agregar_artista(artistas, "El Kuelgue", ["Carta de Amor", "Buenas Noches"])
    agregar_artista(artistas, "La Vela Puerca", ["José Sabía", "El Viejo"])
    agregar_artista(artistas, "El Plan de la Mariposa", ["Rosa", "Hormigas"])

    # Agregar canciones
    agregar_cancion(artistas, "El Kuelgue", "Montón de Nada")
    agregar_cancion(artistas, "La Vela Puerca", "De Atar")

    # Mostrar canciones
    print("Canciones de El Kuelgue:", mostrar_canciones(artistas, "El Kuelgue"))

    # Buscar canción
    print("¿Quién canta 'Rosa'?", buscar_cancion(artistas, "Rosa"))

main()
