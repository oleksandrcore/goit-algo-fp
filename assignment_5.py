import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


def generate_color_shades():
  base_color = '1296F0' # #1296F0
  num_shades = 6 # equals number of nodes

  r, g, b = int(base_color[:2], 16), int(base_color[2:4], 16), int(base_color[4:], 16)

  step_r = int(255 - r) // num_shades
  step_g = int(255 - g) // num_shades
  step_b = int(255 - b) // num_shades

  shades = []
  for i in range(num_shades):
    new_r = min(r + step_r * i, 255)
    new_g = min(g + step_g * i, 255)
    new_b = min(b + step_b * i, 255)

    shade = f"#{new_r:02x}{new_g:02x}{new_b:02x}"
    shades.append(shade)

  return shades

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

def dfs(node, colors, visited):
    if node is not None:
        visited[node.id] = True
        node.color = colors.pop(0)

        dfs(node.left, colors, visited)
        dfs(node.right, colors, visited)


def bfs(node, colors):
    queue = deque([node])
    visited = {}

    while queue:
        node = queue.popleft()

        if node.id not in visited:
            visited[node.id] = True

            node.color = colors.pop(0)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


dfs(root, generate_color_shades(), {})
draw_tree(root)

bfs(root, generate_color_shades())
draw_tree(root)
