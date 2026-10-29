# Gerador de Orçamento Pro 💼

> **Descrição:** Sistema inteligente para criação de orçamentos e propostas comerciais, integrado ao Google Sheets e com geração de relatórios personalizados.

🔗 **[CLIQUE AQUI PARA ACESSAR O GERADOR ONLINE](https://gerador--orcamento-pro.streamlit.app)*

Sistema inteligente para criação, cálculo e gerenciamento de orçamentos e propostas comerciais, integrado diretamente com planilhas do Google Sheets para armazenamento seguro de dados.

## 🚀 Funcionalidades

- **Interface Web Dinâmica:** Desenvolvida para facilitar o preenchimento de dados de clientes e serviços.
- **Banco de Dados em Nuvem:** Integração nativa com o Google Sheets para salvar e consultar orçamentos gerados.
- **Visual Personalizado:** Interface otimizada através de estilizações CSS customizadas para uma melhor experiência visual.
- **Manipulação de Dados:** Uso de Pandas para processamento ágil das tabelas e cálculos internos.

## 🛠️ Tecnologias Utilizadas

- **Python**
- **Streamlit** (Construção da interface web)
- **Pandas** (Estruturação e tratamento dos dados)
- **st-gsheets-connection** (Conexão segura com a API do Google Sheets)

## 📦 Como Instalar e Executar

1. Clone o repositório em sua máquina local.
2. Certifique-se de instalar as dependências obrigatórias listadas em `requisitos.txt`:
   ```bash
   pip install -r requisitos.txt
   ```
3. Execute o servidor do Streamlit:
   ```bash
   streamlit run app.py
   ```

## 🔐 Configuração do Banco de Dados (.toml)
Para o funcionamento correto da integração com as planilhas, lembre-se de configurar suas credenciais do Google Sheets no diretório `.streamlit/secrets.toml` local ou na aba de *Secrets* do Streamlit Cloud.

