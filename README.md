# 📊 Web App Nomes - IBGE

Aplicação em **Python + Streamlit** que consome a [API de Nomes do IBGE](https://servicodados.ibge.gov.br/api/docs/nomes?versao=2) para mostrar a evolução da popularidade de um nome ao longo das décadas.

---

## 🚀 Tecnologias utilizadas
- [Python 3.8+](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [Requests](https://docs.python-requests.org/)

---

## ⚙️ Funcionalidades
- Consultar qualquer nome disponível na base do IBGE  
- Exibir tabela com a frequência do nome por década  
- Mostrar gráfico interativo de evolução da popularidade  

---

## 📥 Instalação e Execução

### 1. Clone este repositório:
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```
### 2. Crie e ative um ambiente virtual (opcional, mas recomendado):

Linux/Mac:

```bash

Copy
python -m venv venv
source venv/bin/activate
```
Windows:

```bash

Copy
python -m venv venv
venv\Scripts\activate
```
### 3. Instale as dependências:

```bash

Copy
pip install -r requirements.txt
```
### 4. Execute a aplicação:

```bash

Copy
streamlit run app.py
```
Após iniciar, abra o link indicado pelo Streamlit no navegador (geralmente http://localhost:8501).

### 📂 Estrutura do Projeto

### 📦 seu-repositorio
 ┣ 📜 app.py           # Código principal da aplicação
 ┣ 📜 requirements.txt # Dependências
 ┗ 📜 README.md        # Documentação
