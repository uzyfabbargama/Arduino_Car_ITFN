import numpy as np
import pandas as pd

# ----------------------------------------------------
# 1. DEFINICIÓN DEL DATASET (LA TABLA DE VERDAD)
# ----------------------------------------------------

# Entradas (X): [Frontal, Izquierda, Derecha, Trasero]
# 1 = Lejos (OK), 0 = Cerca (Obstáculo)
X = np.array([
    [1, 1, 1, 1],
    [1, 1, 1, 0],
    [1, 1, 0, 1],
    [1, 1, 0, 0],
    [1, 0, 1, 1],
    [1, 0, 1, 0],
    [1, 0, 0, 1],
    [0, 1, 1, 1],
    [0, 1, 1, 0],
    [0, 1, 0, 1],
    [0, 1, 0, 0],
    [0, 0, 1, 1],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [0, 0, 0, 0]
])

# Salidas (Y): [Adelante, Luz_Freno, Giro_Izq]
# Adelante: 1=Adelante, 0=Detener
# Luz_Freno: 1=ON, 0=OFF
# Giro_Izq: 1=Girar, 0=No Girar
Y = np.array([
    [1, 0, 0],  # Avanza Normal
    [1, 0, 0],
    [1, 0, 0],
    [1, 0, 0],
    [1, 0, 0],
    [1, 0, 0],
    [1, 0, 0],
    [0, 1, 1],  # Detener, Freno ON, Gira Izq
    [0, 1, 1],
    [0, 1, 1],
    [0, 1, 1],
    [0, 1, 0],  # Detener, Freno ON, No Gira
    [0, 1, 0],
    [0, 1, 0],
    [0, 1, 0]
])

print("Dimensiones de las Entradas (X):", X.shape)
print("Dimensiones de las Salidas (Y):", Y.shape)
#-----------------------------------------
#=           Simulación de IA            =
#-----------------------------------------
def traducir_salidas(output_vector):
    """Traduce el vector binario de salida a un comportamiento legible."""
    Adelante, Luz_Freno, Giro_Izq = output_vector
    
    comportamiento = ""
    if Adelante == 1:
        comportamiento += "¡AVANZAR!"
    else:
        comportamiento += "¡DETENER!"

    if Luz_Freno == 1:
        comportamiento += " (Luz Freno: ON)"
    
    if Giro_Izq == 1:
        comportamiento += " -> GIRAR IZQUIERDA"
        
    return comportamiento

def predecir_comportamiento(sensor_inputs):
    """Busca la fila en X y devuelve la salida Y correspondiente."""
    # Convertimos la entrada a un array para la comparación
    input_array = np.array(sensor_inputs)
    
    # Buscamos la fila que coincide exactamente con las entradas
    # np.all(X == input_array, axis=1) devuelve un array booleano de coincidencias
    coincidencia = np.all(X == input_array, axis=1)
    
    if coincidencia.any():
        # Tomamos el índice de la primera coincidencia
        idx = np.where(coincidencia)[0][0]
        output_vector = Y[idx]
        comportamiento = traducir_salidas(output_vector)
        return output_vector, comportamiento
    else:
        return None, "ERROR: Combinación de sensores no definida en la Tabla."
#L_____________________L#
#|  Pruebas de código  |#
#L_____________________L#

print("\n--- TEST 1: Caminando en Campo Abierto ---")
# Entradas: [Frontal, Izquierda, Derecha, Trasero] -> [1, 1, 1, 1]
inputs_1 = [1, 1, 1, 1] 
output_1, desc_1 = predecir_comportamiento(inputs_1)
print(f"Sensores (X): {inputs_1}")
print(f"Salidas (Y): {output_1}")
print(f"Comportamiento: {desc_1}")

print("\n--- TEST 2: Atrapado por Delante, Izquierda y Derecha (Caso Crítico) ---")
# Entradas: [Frontal, Izquierda, Derecha, Trasero] -> [0, 0, 0, 1]
inputs_2 = [0, 0, 0, 1] 
output_2, desc_2 = predecir_comportamiento(inputs_2)
print(f"Sensores (X): {inputs_2}")
print(f"Salidas (Y): {output_2}")
print(f"Comportamiento: {desc_2}")
