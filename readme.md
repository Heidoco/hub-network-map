# Gerador de Mapas para Localização de Concentradores

Um gerador de mapas interativo desenvolvido para visualizar  soluções de problemas de localização de concentradores em redes. Esta ferramenta auxilia na visualização e análise de diferentes configurações de rede.

## Funcionalidades Principais

coord_exctract -> Permite extrair as coordenadas de uma imagem base
map_generator -> Gera o mapa a partir dos hubs, nós, e conexões informadas no código

## Requisitos do Sistema

- Python 3.x
- Dependências:
    - numpy
    - matplotlib
    - networkx

## Instalação

```bash
git clone https://github.com/Heidoco/hub-network-map
cd hub-network-map
pip install -r requirements.txt
```

## Como Usar

- Se não tiver a localização dos nós da rede
    - Inserir a imagem_exemplo.png(Imagem de fundo da sua rede) na pasta coord_extract
    - Executar o coord_extract.py

- Se já possuir as coordenadas
    - Inserir a imagem_padrao.png(Imagem de fundo da sua rede) na pasta map_generator
    - Inserir as coordenadas no padrão do coords.txt
    - Inserir os nós, hubs e conexões no arquivo map_generator/nodes.py
    - Executar map_generator.py
