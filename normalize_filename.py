import unicodedata

"""
Este programa toma un nombre de archivo y lo normaliza de la siguiente manera:
- Convierte todas las letras a minúsculas.
- Elimina tildes y diéresis para garantizar compatibilidad.
- Mantiene la estructura del nombre del archivo pero sin caracteres especiales.
- Reemplaza los espacios por guiones.

Ejemplo:
Entrada: "Álgebra-Lineal-Básica.html"
Salida:  "algebra-lineal-basica.html"

Esto es útil para evitar problemas de compatibilidad en sistemas de archivos yb servidores web.
"""

def normalize_filename(filename):
    # Convertir a minúsculas y eliminar tildes/dieresis
    nfkd_form = unicodedata.normalize('NFKD', filename)
    # Eliminar los caracteres combinados (tildes, diéresis, etc.)
    filename_normalized = "".join([c for c in nfkd_form if not unicodedata.combining(c)]).lower()
    # Reemplazar los espacios por guiones
    filename_normalized = filename_normalized.replace(" ", "-")
    return filename_normalized

# Ejemplo de uso
filename = input("Ingresa el nombre el título con su extensión: ")
new_filename = normalize_filename(filename)
print(new_filename)
