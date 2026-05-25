import pandas as pd

# 1. Ler o arquivo de estoque
df_estoque = pd.read_csv("estoque.csv")

# 2. O Desafio: Filtrar componentes com Preço Unitário acima de 500
# Note que usamos o nome exato da coluna 'Preco_Unitario'
df_alto_custo = df_estoque[df_estoque['Preco_Unitario'] > 500]

# 3. Exibir o resultado no terminal para conferência
print("--- Auditoria: Itens de Alto Custo (> R$ 500) ---")
print(df_alto_custo)

# 4. Exportar a sublista para um novo arquivo CSV
df_alto_custo.to_csv("hardware_alto_custo.csv", index=False)

print("\nRelatório 'hardware_alto_custo.csv' gerado com sucesso!")