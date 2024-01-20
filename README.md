# Algoritmos-de-Busqueda
ACO (Algoritmo de Colonia de Hormigas) y A*. ACO simula el comportamiento colectivo de las hormigas para encontrar rutas óptimas, mientras que A* es un eficiente algoritmo de búsqueda heurística.

#### Introducción
Este repositorio, creado por HonroAvispa, es una colección integral de herramientas para la planificación y optimización de rutas. Incluye implementaciones del Algoritmo de Colonia de Hormigas (ACO), el Algoritmo A*, y un generador de grafos para facilitar la experimentación y visualización de rutas.

#### Instalación y Requisitos
Para utilizar estos scripts, necesitarás Python 3 y algunas bibliotecas específicas como `networkx` y `numpy`. Instala las dependencias que te sean necesarias.

#### Algoritmos Implementados
- **Algoritmo A*** (`route_planning.py`): Encuentra rutas óptimas en un grafo usando el enfoque de búsqueda heurística A*.
- **Algoritmo de Colonia de Hormigas** (`aco_algorithm.py` y `main.py`): `aco_algorithm.py` implementa la lógica del ACO, y `main.py` lo ejecuta con un grafo de entrada.
- **Generador de Grafos** (`grafos_creator.py`): Crea grafos aleatorios o conectados para probar los algoritmos.

#### Uso
Ejecuta los algoritmos con:
```bash
python main.py
```

#### Ejemplos de Uso
![grafo_0](https://github.com/HonroAvispa0001/Algoritmos-de-Busqueda/assets/73007200/0cb86980-7609-4932-808c-6cd33377c3c4)

#Grafo generado con el grafos_creator.py

1er ejemplo llegar de 3 a 7
#### Solución con ACO
![image](https://github.com/HonroAvispa0001/Algoritmos-de-Busqueda/assets/73007200/f67c58ae-1b2a-4228-8090-f75ecc0f1fb3)
#### Solución con A*
![image](https://github.com/HonroAvispa0001/Algoritmos-de-Busqueda/assets/73007200/e376f1d9-6e8a-432b-948b-f498da9971b8)


#### Contribuciones
Las mejoras y sugerencias son siempre bienvenidas. Si tienes ideas para mejorar el código o añadir nuevas características, considera contribuir a través de 'pull requests' o 'issues'.

Ref: https://inaoe.repositorioinstitucional.mx/jspui/bitstream/1009/394/1/IbarraBMN.pdf

