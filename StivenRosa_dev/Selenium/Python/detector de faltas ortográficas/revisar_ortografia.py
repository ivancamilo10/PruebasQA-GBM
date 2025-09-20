from spellchecker import SpellChecker

# Crear objeto SpellChecker en español
spell = SpellChecker(language='es')

def revisar_ortografia(parrafo):
    """
    Recibe un párrafo de texto y devuelve:
    - 1 si hay errores ortográficos, 0 si no
    - Lista de palabras mal escritas
    """
    palabras = parrafo.split()
    errores = list(spell.unknown(palabras))
    resultado = 1 if errores else 0
    return resultado, errores

# Ejemplo de uso
texto = "Holaa, esttoy probando un detector de ortogrfia."
estado, palabras_malas = revisar_ortografia(texto)

print("Errores detectados:", estado)          # 1 si hay errores, 0 si no
print("Palabras mal escritas:", palabras_malas)  # Lista con palabras incorrectas
