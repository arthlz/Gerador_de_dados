import random
import time
import sys

# Listas de possibilidades baseadas no contexto do vídeo
pratos = ["Hamachi", "Wagyu", "Dessert", "Tasting Amuse", "Cake"]
restricoes = ["None", "White Chocolate Allergy", "Nut Allergy", "Gluten Free"]
status = ["Normal", "VIP (Green)", "Out of Town (Yellow)"]
ritmo = ["Normal", "Fast (Table 15)", "Slow (Table 23)"]

def gerar_pedido():
    mesa = random.randint(1, 40)
    prato = random.choice(pratos)
    restricao = random.choice(restricoes) if random.random() < 0.2 else "None" # 20% de chance de restrição
    status_cliente = random.choice(status) if random.random() < 0.1 else "Normal" # 10% de chance de ser VIP/Out of Town
    ritmo_cliente = random.choice(ritmo)

    # Sai como um input para os alunos
    return f"{mesa},{prato},{restricao},{status_cliente},{ritmo_cliente}"


quantidade_pedidos = 50

# O loop imprime na saída padrão (stdout)
for _ in range(quantidade_pedidos):
    pedido = gerar_pedido()
    print(pedido)
    time.sleep(0.5) # Isso é para que o print não saia todos de uma vez, mas pode descomentar para ser instantâneo