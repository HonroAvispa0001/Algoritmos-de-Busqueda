import networkx as nx
import matplotlib.pyplot as plt
import random

def crear_grafo_conectado(num_nodos, dirigido=False):
    """Crear un grafo conectado con el número dado de nodos."""
    if dirigido:
        G = nx.DiGraph()
    else:
        G = nx.Graph()

    # Agregar el primer nodo
    G.add_node(0)

    # Asegurar que todos los otros nodos estén conectados
    for i in range(1, num_nodos):
        # Conectar el nuevo nodo a un nodo existente aleatorio
        conectar_a = random.randint(0, i - 1)
        peso = random.randint(1, 10)
        G.add_edge(i, conectar_a, weight=peso)

        # Opcionalmente agregar más aristas para hacer el grafo más denso
        for j in range(0, i):
            if random.random() > 0.5:
                peso = random.randint(1, 10)
                G.add_edge(i, j, weight=peso)

    return G

def dibujar_grafo(G, guardar_en_archivo=False, nombre_archivo="grafo.png"):
    """Dibujar el grafo con etiquetas para los pesos y opcionalmente guardarlo en un archivo."""
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)
    etiquetas = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=etiquetas)

    if guardar_en_archivo:
        plt.savefig(nombre_archivo)
    plt.show()

def guardar_grafo_en_txt(G, nombre_archivo="datos_grafo.txt"):
    """Guardar los datos del grafo en un archivo de texto."""
    with open(nombre_archivo, "w") as archivo:
        # Escribir nodos
        archivo.write("Nodos:\n")
        for nodo in G.nodes:
            archivo.write(f"{nodo}\n")
        
        # Escribir aristas con pesos
        archivo.write("\nAristas (con pesos):\n")
        for arista in G.edges(data=True):
            archivo.write(f"{arista[0]} - {arista[1]} (Peso: {arista[2]['weight']})\n")

def generar_multiples_grafos(num_grafos, num_nodos, dirigido=False):
    """Generar múltiples grafos, guardar sus datos en archivos de texto e imágenes."""
    for i in range(num_grafos):
        # Crear un grafo
        G = crear_grafo_conectado(num_nodos, dirigido)

        # Guardar los datos del grafo en un archivo de texto
        nombre_txt = f"graph_data_{i}.txt"
        guardar_grafo_en_txt(G, nombre_txt)

        # Dibujar y guardar el grafo en un archivo de imagen
        nombre_img = f"grafo_{i}.png"
        dibujar_grafo(G, guardar_en_archivo=True, nombre_archivo=nombre_img)



generar_multiples_grafos(1, 100)  # Generar 1 grafo con 100 nodos
