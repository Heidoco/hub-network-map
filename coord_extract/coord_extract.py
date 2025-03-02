"""Extrai as coordenadas dos nós a partir de uma imagem."""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

NUMERO_TOTAL_PONTOS = 25

def onclick(event):
    """Manipulador de eventos para cliques do mouse em uma figura Matplotlib.

    Parâmetros:
    event (matplotlib.backend_bases.MouseEvent): O evento de clique do mouse contendo
        as coordenadas x e y.

    Retorna:
    list: A lista atualizada de coordenadas.
    """
    ix, iy = event.xdata, event.ydata
    coords.append((ix, iy))
    print(f'Coordenada: ({ix}, {iy})')
    if len(coords) == NUMERO_TOTAL_PONTOS:
        fig.canvas.mpl_disconnect(cid)
        plt.close()
    return coords

# Carregar a imagem
img = mpimg.imread('./coord_extract/imagem_padrao.png')

# Exibir a imagem
fig, ax = plt.subplots()
ax.imshow(img)

# Função para capturar os cliques do mouse e armazenar as coordenadas
coords = []

# Conectar o evento de clique ao gráfico
cid = fig.canvas.mpl_connect('button_press_event', onclick)

plt.show()

# Armazenar as coordenadas em um dicionário
coords_dict = {i+1: coord for i, coord in enumerate(coords)}
print("Dicionário de coordenadas:", coords_dict)

# Salvar o dicionário em um arquivo txt
try:
    with open('coords.txt', 'w', encoding='utf-8') as f:
        for key, value in coords_dict.items():
            f.write(f'{key}: {value}\n')
    print("Coordenadas salvas em 'coords.txt'")
except IOError as e:
    print(f"Erro ao salvar coordenadas: {e}")