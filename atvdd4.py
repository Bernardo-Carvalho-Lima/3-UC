import pandas as pd

# 1. O que fazer: Criar o DataFrame manual
dados_licencas = {
    "Filial": ["São Paulo", "Rio de Janeiro", "Curitiba", "Belo Horizonte", "Salvador"],
    "Usuarios_Ativos": [120, 85, 40, 65, 30]
}

df_custos = pd.DataFrame(dados_licencas)

# 2. O Desafio: Cálculo automático da Função Linear
# Fórmula: Custo = (15 * Usuários) + 80
df_custos['Custo_Total_R$'] = (df_custos['Usuarios_Ativos'] * 15) + 80

# 3. Exibir a tabela final no terminal
print("--- Projeção de Custos de Licenciamento ---")
print(df_custos)

# 4. Exportar para CSV
df_custos.to_csv("custo_licenciamento.csv", index=False)

print("\nArquivo 'custo_licenciamento.csv' gerado com sucesso!")