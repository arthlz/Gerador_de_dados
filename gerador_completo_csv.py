import random
import csv
from datetime import datetime, timedelta

# Configurações do ambiente do restaurante
pratos = ["Hamachi", "Wagyu", "Dessert", "Tasting Amuse", "Cake"]
restricoes = ["Nenhuma", "Alergia a Chocolate Branco", "Alergia a Nozes", "Sem Glúten"]
status = ["Normal", "VIP (Verde)", "Fora da Cidade (Amarelo)"]
ritmo = ["Normal", "Rápido (Mesa 15)", "Lento (Mesa 23)"]

# Nome do arquivo de saída
nome_arquivo = 'pedidos_sala_de_guerra.csv'

with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    # Escreve o cabeçalho (a primeira linha com o nome das colunas)
    escritor_csv.writerow(['ID_Pedido', 'Mesa', 'Prato', 'Restricao_Alimentar', 'Status', 'Ritmo', 'Horario'])
    
    horario = datetime.now()
    
    # Gera 100 pedidos simulados
    for i in range(1, 101):
        mesa = random.randint(1, 40)
        prato = random.choice(pratos)
        restricao = random.choice(restricoes) if random.random() < 0.2 else "Nenhuma"
        status_cliente = random.choice(status) if random.random() < 0.1 else "Normal"
        ritmo_cliente = random.choice(ritmo)
        
        # Incrementa o horário em alguns minutos para simular a noite avançando
        horario += timedelta(minutes=random.randint(1, 5))
        horario_str = horario.strftime("%H:%M:%S")
        
        # Escreve os dados formatados diretamente no arquivo
        escritor_csv.writerow([f"PED_{i:03d}", mesa, prato, restricao, status_cliente, ritmo_cliente, horario_str])

print(f"Dados gerados com sucesso no arquivo '{nome_arquivo}'.")