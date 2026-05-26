import pandas as pd

# 1. PASSO MANUAL: Criando o arquivo CSV de simulação
dados_logs = {
    "Timestamp": ["10:00:15", "10:02:40", "10:05:12", "10:06:01", "10:09:55"],
    "Nivel": ["INFO", "WARNING", "CRITICAL", "INFO", "CRITICAL"],
    "Mensagem": ["Sistema iniciado", "Uso de CPU alto", "Falha de conexão com banco", "Usuário logado", "Kernel Panic no servidor"]
}
df_logs = pd.DataFrame(dados_logs)
df_logs.to_csv("logs_sistema.csv", index=False)

# 2. O DESAFIO: Filtrar estritamente logs com nível igual a "CRITICAL"
df_auditoria = pd.read_csv("logs_sistema.csv")
df_falhas_criticas = df_auditoria[df_auditoria["Nivel"] == "CRITICAL"]

# Exibir no terminal e salvar arquivo final de auditoria
print("🚨 FALHAS GRAVES ENCONTRADAS NA AUDITORIA: 🚨")
print(df_falhas_criticas)

df_falhas_criticas.to_csv("auditoria_falhas_criticas.csv", index=False)