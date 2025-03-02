"""Gera a imagem com as conexooes entre os nós da rede"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import networkx as nx
from nodes import EDGES_DIRECT, EDGES_ARC, EDGES_NORMAL, HUBS

# # Coordenadas dos nós, pode ser obtido com arquvo coord_extract.py
# coordinates = {
#     1: (1043.6258741258741, 558.6928071928071),
#     2: (1216.548951048951, 366.68081918081907),
#     3: (1315.3621378621378, 244.28721278721275),
#     4: (916.7407592407592, 334.11738261738253),
#     5: (1032.397102897103, 402.61288711288705),
#     6: (1078.435064935065, 329.625874125874),
#     7: (722.483016983017, 604.7307692307692),
#     8: (523.7337662337662, 395.8756243756243),
#     9: (1033.51998001998, 310.536963036963),
#     10: (765.1523476523475, 691.1923076923076),
#     11: (767.3981018981019, 422.82467532467524),
#     12: (175.64185814185817, 510.4090909090908),
#     13: (889.7917082917083, 526.1293706293706),
#     14: (1179.4940059940059, 757.4420579420579),
#     15: (803.3301698301698, 254.39310689310685),
#     16: (907.7577422577422, 674.3491508491508),
#     17: (1243.4980019980019, 295.9395604395604),
#     18: (1233.3921078921078, 337.486013986014),
#     19: (330.59890109890114, 558.6928071928071),
#     20: (1128.9645354645354, 348.71478521478514),
#     21: (871.8256743256743, 432.93056943056934),
#     22: (116.12937062937061, 412.71878121878115),
#     23: (176.76473526473524, 112.91058941058941),
#     24: (1122.2272727272727, 709.1583416583416),
#     25: (1194.0914085914085, 391.3841158841158),
# }

def load_coordinates(file_path):
    """Carrega as coordenadas dos nós a partir de um arquivo txt."""
    coord = {}
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                key, value = line.strip().split(': ')
                key = int(key)
                value = tuple(map(float, value.strip('()').split(', ')))
                coord[key] = value
    except (IOError, ValueError) as e:
        print(f"Erro ao carregar coordenadas: {e}")
    return coord

# Carregar as coordenadas dos nós a partir do arquivo coords.txt
coordinates = load_coordinates('./coords.txt')

G = nx.Graph()
G.add_nodes_from(coordinates.keys())

# Adiciona as conexões ao gráfico
G.add_edges_from(EDGES_DIRECT + EDGES_ARC + EDGES_NORMAL)

# Carrega a imagem de fundo
background_img = mpimg.imread("./map_generator/imagem_padrao.png")

# Define a figura e o eixo
fig, ax = plt.subplots()
ax.imshow(background_img, aspect="auto")


# Determina os nós normais como todos os nós que não são hubs
normals = set(coordinates.keys()) - HUBS

# Define as coordenadas dos nós
pos = coordinates

# Desenha os nós

# Hubs em triângulos
nx.draw_networkx_nodes(
    G, pos, nodelist=HUBS, node_size=300, node_color="#f58634", node_shape="^", ax=ax
)

# Normais em círculos
nx.draw_networkx_nodes(
    G, pos, nodelist=normals, node_size=300, node_color="#00afef", node_shape="o", ax=ax
)

# Desenha as conexões diretas (nó para nó)
nx.draw_networkx_edges(
    G, pos, edgelist=EDGES_DIRECT, edge_color="#00a859", style="dashed", width=1, ax=ax
)

# Desenha os arcos (hub para hub)
nx.draw_networkx_edges(
    G, pos, edgelist=EDGES_ARC, edge_color="#ed3d42", style="solid", width=2, ax=ax
)

# Desenha as conexões normais (hub para nó)
nx.draw_networkx_edges(
    G, pos, edgelist=EDGES_NORMAL, edge_color="#403d3e", style="solid", width=1, ax=ax
)

# Desenha os rótulos dos nós
nx.draw_networkx_labels(G, pos, font_size=10, font_family="sans-serif", ax=ax)

plt.axis("off")  # Desativa o eixo
plt.show()
