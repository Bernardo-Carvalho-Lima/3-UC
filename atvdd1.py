import pandas as pd 
#Inventário de Equipamentos de TI

dados_equipamentos = {
    "ID_Equipamento":[101, 102, 103, 104, 105],
     "Processador": ["Intel i5", "Intel i7", "AMD Ryzen 5", "Intel i9", "AMD Ryzen 7"], 
      "Memória_RAM_GB": [8, 16, 8, 32, 16], 
      "Setor": ["Financeiro", "TI", "RH", "Engenharia", "Marketing"]}

df = pd.DataFrame(dados_equipamentos)

# Exibe o DataFrame no ecrã para conferência
print("DataFrame criado com sucesso:")
print(df)

# 3. Exportar para um arquivo CSV (O Desafio - Parte 2)
# O parâmetro index=False remove a coluna de índices numérica automática
df.to_csv("inventario_ti.csv", index=False)

print("\nFicheiro 'inventario_ti.csv' gerado com sucesso!")


