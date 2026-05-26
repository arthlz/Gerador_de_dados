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

    # Formata como um CSV simples ou JSON para facilitar a leitura pelos alunos
    return f"{mesa},{prato},{restricao},{status_cliente},{ritmo_cliente}"

# Gera 50 pedidos, simulando a chegada ao longo do tempo (ou de uma vez só)
quantidade_pedidos = 50

# O loop imprime na saída padrão (stdout)
for _ in range(quantidade_pedidos):
    pedido = gerar_pedido()
    print(pedido)
    # sys.stdout.flush() # Importante se for usar o Método 2 (Pipes)
    # time.sleep(0.5) # Descomente se quiser simular os pedidos chegando aos poucos (1 a cada meio segundo)