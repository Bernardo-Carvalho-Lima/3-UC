import pandas as pd

# 1. Carregar os dados (do exercício anterior)
df = pd.read_csv("funcionarios.csv")

# 2. O Desafio: Filtrar funcionários com mais de 2 anos de empresa
# Lógica: df[ df['Nome_da_Coluna'] > valor ]
df_filtrado = df[df['Tempo_Empresa_Anos'] > 2]

# 3. Exibir o resultado no terminal para conferência
print("--- Funcionários para Auditoria (Mais de 2 anos) ---")
print(df_filtrado)

# 4. Exportar a lista limpa para um novo arquivo
df_filtrado.to_csv("funcionarios_auditoria.csv", index=False)

print("\nArquivo 'funcionarios_auditoria.csv' gerado com sucesso!")
