# route_planning.py

# Importamos las librerías necesarias
import heapq
import math
import time


# Definición de la clase Nodo
class Nodo:
    def __init__(self, identificador, coordenadas=None):
        self.identificador = identificador
        self.coordenadas = coordenadas  # Opcional, según el caso de uso

# Definición de la clase Grafo
class Grafo:
    def __init__(self):
        self.nodos = {}
        self.aristas = {}

    def agregar_nodo(self, nodo):
        self.nodos[nodo.identificador] = nodo

    def agregar_arista(self, origen, destino, costo):
        if origen in self.nodos and destino in self.nodos:
            if origen not in self.aristas:
                self.aristas[origen] = {}
            self.aristas[origen][destino] = costo

# Función heurística (por ahora, solo un placeholder)
def heuristica(nodo1, nodo2):
    # Implementación básica: distancia euclidiana (si hay coordenadas)
    if nodo1.coordenadas and nodo2.coordenadas:
        return math.sqrt((nodo1.coordenadas[0] - nodo2.coordenadas[0]) ** 2 + (nodo1.coordenadas[1] - nodo2.coordenadas[1]) ** 2)
    return 0

# Implementación mejorada del algoritmo A*
def a_star_mejorado(grafo, inicio, fin):
    if inicio not in grafo.nodos or fin not in grafo.nodos:
        return None, 0  # Si el inicio o fin no están en el grafo, retornar None

    cola_prioridad = []
    heapq.heappush(cola_prioridad, (0, inicio))
    camino = {}
    costo = {inicio: 0}

    tiempo_inicio = time.time()

    while cola_prioridad:
        _, nodo_actual = heapq.heappop(cola_prioridad)

        if nodo_actual == fin:
            tiempo_fin = time.time()
            camino_reconstruido, longitud = reconstruir_camino_y_longitud(camino, fin, grafo)
            return camino_reconstruido, longitud, tiempo_fin - tiempo_inicio

        for vecino, peso in grafo.aristas.get(nodo_actual, {}).items():
            nuevo_costo = costo[nodo_actual] + peso
            if vecino not in costo or nuevo_costo < costo[vecino]:
                costo[vecino] = nuevo_costo
                prioridad = nuevo_costo + heuristica(grafo.nodos[vecino], grafo.nodos[fin])
                heapq.heappush(cola_prioridad, (prioridad, vecino))
                camino[vecino] = nodo_actual

    return None, 0, time.time() - tiempo_inicio  # No se encontró camino

# Función para reconstruir el camino y calcular su longitud total
def reconstruir_camino_y_longitud(camino, fin, grafo):
    trayecto_reconstruido = []
    longitud_total = 0
    nodo_actual = fin

    while nodo_actual in camino:
        trayecto_reconstruido.insert(0, nodo_actual)
        nodo_anterior = camino[nodo_actual]
        # Sumar el peso de la arista entre el nodo actual y el nodo anterior
        longitud_total += grafo.aristas[nodo_anterior][nodo_actual]
        nodo_actual = nodo_anterior

    trayecto_reconstruido.insert(0, nodo_actual)  # Agregar el nodo inicial
    return trayecto_reconstruido, longitud_total

# Leer los datos del grafo desde un archivo
def leer_datos_grafo(ruta_archivo):
    with open(ruta_archivo, 'r') as archivo:
        lineas = archivo.readlines()

    nodos = []
    aristas = []
    leyendo_nodos = True

    for linea in lineas:
        if linea.strip() == 'Aristas (con pesos):':
            leyendo_nodos = False
            continue

        if leyendo_nodos and linea.strip():
            # Asumiendo que los nodos están listados bajo "Nodes:"
            nodos.append(linea.strip())
        elif linea.strip():
            # Procesar las aristas
            partes = linea.split()
            origen, destino, peso = partes[0], partes[2], int(partes[4].strip('()'))
            aristas.append((origen, destino, peso))

    return nodos, aristas

# Cargar los datos del grafo desde el archivo proporcionado
nodos, aristas = leer_datos_grafo('graph_data_0.txt')

# Construir el grafo a partir de los datos leídos
grafo_prueba = Grafo()
for nodo_id in nodos:
    grafo_prueba.agregar_nodo(Nodo(nodo_id))
for origen, destino, peso in aristas:
    grafo_prueba.agregar_arista(origen, destino, peso)

# Prueba del algoritmo mejorado en un entorno local

inicio = input("Ingrese el punto de inicio (A): ")
fin = input("Ingrese el punto de destino (B): ")

camino, longitud, tiempo_resolucion = a_star_mejorado(grafo_prueba, inicio, fin)
if camino:
    print(f"Camino más corto de {inicio} a {fin}: {camino}")
    print(f"Longitud del camino: {longitud}")
else:
    print("No se encontró un camino válido.")
print(f"Tiempo de resolución: {tiempo_resolucion:.6f} segundos")
