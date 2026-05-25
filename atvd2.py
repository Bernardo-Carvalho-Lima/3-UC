import pandas as pd

# Este bloco cria o arquivo caso ele não exista
dados = {
    "Nome": ["Douglas", "Amanda", "Lucas", "Beatriz"],
    "Cargo": ["Instrutor", "Gestora TI", "Suporte Técnico", "Analista Dados"],
    "Salario": [4500, 7500, 2800, 5200],
    "Tempo_Empresa_Anos": [2, 4, 1, 3]
}
df_inicial = pd.DataFrame(dados)
df_inicial.to_csv("funcionarios.csv", index=False)

# Agora o seu código de leitura vai funcionar:
df_funcionarios = pd.read_csv("funcionarios.csv")
print(df_funcionarios)