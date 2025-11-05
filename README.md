# Arduino_Car_ITFN
It's the future now.

### Análisis de la arquitectura
El artículo describe una arquitectura simple pero muy efectiva para una primera aproximación al control basado en "IA" (en este caso, una red neuronal muy sencilla que actúa como un clasificador o sistema de reglas):

• **Sensores de Entrada (Las "Entradas"):** Utilizan sensores ultrasónicos (HC-SR04) para medir distancias. Esto simula la **percepción** del vehículo.

• **"Cerebro" (La Red Neuronal):** El **núcleo** del proyecto. Una red neuronal simple (probablemente con una capa de entrada, una oculta y una de salida) entrena un modelo para asociar las distancias percibidas con la acción correcta a tomar. Este modelo es luego implementado en el Arduino.

• **Actuadores (Las "Salidas"):** Motores de corriente continua controlados por un driver (como el L298N o similar) para mover el coche (adelante, atrás, girar). Estas son las acciones del vehículo.

Este enfoque es sumamente **interesante** debido a los **siguiente:** 
1. **Aplica el Principio de Machine Learning a Nivel Micro:** Demuestra que los conceptos de training, feedforward, y clasificación se pueden aplicar incluso en sistemas embedded con recursos limitados como Arduino.
2. **Solución Práctica de Control:** Es un método eficiente para generar un sistema de control reactivo y adaptativo sin tener que codificar manualmente cada regla `IF-THEN-ELSE` para todas las posibles combinaciones de distancias.

### **🧠 Propuesta de Expansión del Proyecto en Google Colab**
  ---
  **➕ Nuevas Entradas (Simulación de Sensores)**
  ---
  Propongo agregar las siguientes **2 nuevas entradas** para experimentar con el proyecto y aumentar su capacidad de decisión:
  1. `Obstáculo:Trasero` **(Booleano/Distancia):** Un sensor ultrasónico trasero.
    • **Propósito:** Prevenir colisiones al retroceder o alertar sobre un vehículo muy cercano detrás.
  2. `Linea_Negra_Abajo` **(Booleano):** Un sensor infrarrojo de línea (como el CNY70) apuntando al suelo.
     • **Propósito:** Añadir la funcionalidad de **seguimiento de línea**, dándole un segundo "modo" de operación.
### **⚙️ Nueva Salida (Simulación de Actuador)**
  También sería mejor una nueva salida de la red neuronal para enriquecer la acciones del coche
  1. `Luz_Freno` **(Booleano):** Un LED rojo simple en la parte trasera.
    • **Propósito:** Un indicador visual de que el coche ha detectado un peligro frontal inminente y está a punto de detenerse o reducir la velocidad drásticamente.
### 📝 El Misterio de la Tabla de Verdad (¡El Corazón de la IA!) 
Resolveremos cada caso como detectives 🕵️🕵️, y resolveremos el caso de las verdades desaparecidas, ya que al agregar más entradas, nuestra tabla de verdad, se expande, así que, ¡MANOS A LA OBRA!

| Entrada: Frontal (0/1) | Entrada: Izquierda (0/1) | Entrada: Derecha (0/1) | Entrada Trasero (0/1) | Salida: Mover | Salida: Luz_Freno (0/1) | Salida: Giro Izq (0/1) | Comportamiento |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| :---: | :---: | :---: | :---: | :--- |
| 1 | 1 | 1 | 1 | Adelante | 0 | 0 | Avanza Normal. |
| 1 | 1 | 1 | 0 | Adelante | 0 | 0 | Avanza Normal. |
| 1 | 1 | 0 | 1 | Adelante | 0 | 0 | Avanza Normal. |
| 1 | 1 | 0 | 0 | Adelante | 0 | 0 | Avanza Normal. |
| 1 | 0 | 1 | 1 | Adelante | 0 | 0 | Avanza Normal. |
| 1 | 0 | 1 | 0 | Adelante | 0 | 0 | Avanza Normal. |
| 1 | 0 | 0 | 1 | Adelante | 0 | 0 | Avanza Normal. |
| 0 | 1 | 1 | 1 | Freno    | 1 | 1 | Obstáculo Frontal: Gira Izq.     |
| 0 | 1 | 1 | 0 | Freno    | 1 | 1 | Obstáculo Frontal/Trasero: Gira Izq.     |
| 0 | 1 | 0 | 1 | Freno    | 1 | 1 | Obstáculo Frontal/Derecho: Gira Izq.     |
| 0 | 1 | 0 | 0 | Freno    | 1 | 1 | Obstáculo Frontal/Derecho/Trasero: Gira Izq.     |
| 0 | 0 | 1 | 1 | Freno    | 1 | 0 | Obstáculo Frontal/Izquierdo: Frena.          |
| 0 | 0 | 1 | 0 | Freno    | 1 | 0 | Obstáculo Frontal/Izquierdo/Trasero: Frena.          |
| 0 | 0 | 0 | 1 | Freno    | 1 | 0 | Obstáculo Frontal/Izquierdo/Derecho: Frena (Atrapado).          |
| 0 | 0 | 0 | 0 | Freno    | 1 | 0 | Obstáculo Total: Frena (Atrapado).          |
