# Chatbot-IA

<center>

![Logo AssistIF](https://raw.githubusercontent.com/Almeedus/Chatbot-IA/refs/heads/main/src/Logo.png)

</center>

> Imagem de autoria própria


<hr>

## 🌐 Visão Geral
O AssistIF é um sistema construído em VueJS, Python e MongoDB. Permite que os usuários utilizem o sistema por meio de requesições contendo dúvidas baseadas nos editais de vestibular do Instituto Federal de São Paulo.

<hr>

## 🗃️ Índice
- [`💻 Pré-Requisitos`](#-pré-requisitos)
- [`🛠️ Stack Utilizada`](#%f0%9f%9b%a0-stack-utilizada)
- [`🚩 Iniciando a Aplicação`](#-iniciando-a-aplicação)
    - [`⬇️ Clonando o Repositório`](#️-clonando-o-repositório)
    - [`⚙️ Configurando o .env`](#️-cofigurando-o-env)
    - [`🏁 Rodando a Aplicação`](#-rodando-a-aplicação)
- [`⚓ EndPoints`](#-endpoints)
- [`📁 Estrutura das Pastas`](#-estrutura-das-pastas)
- [`📈 Progresso do Desenvolvimento`](#-progresso-do-desenvolvimento)
<hr>

## 💻 Pré-Requisitos
- Python instalado;
- Conhecimentos de Python e API RESTful;
- MongoDB instalado;
- Conhecimentos em MongoDB.

[`📗 Guia de Instação Python`](https://www.python.org/downloads/)
[`📙 Guia de Instação MongoDB`](https://www.mongodb.com/pt-br/docs/manual/installation/)

<hr>

## 🛠️ Stack Utilizada
A linguagem ecolhida foi TypeScript juntamente com Python e o banco de dados não relacional MongoDB. Entre as bibliotecas utilizadas, as principais são:

- [LangChain](https://www.langchain.com/langchain)
- [PyMongo](https://mongoosejs.com/)
- [FastAPI](https://fastapi.tiangolo.com/)

![Diagrama da Stack](https://raw.githubusercontent.com/Almeedus/Chatbot-IA/refs/heads/main/src/diagrama-stack.png)
> Imagem feita utilizando o [Excalidraw](https://excalidraw.com/)

<hr>

## 🚩 Iniciando a Aplicação
Antes de tudo você deve ter o MongoDB e o Python instalados conforme os [pré-requisitos](#-pré-requisitos).

> [!NOTE]
> Sem a instalação dessas tecnologias a aplicação não irá rodar.

### ⬇️ Clonando o Repositório
Use o comando `git clone` para clonar este repositório ou faça o [download](https://github.com/Almeedus/Chatbot-IA/archive/refs/heads/main.zip) do mesmo:
```bash
git clone https://github.com/Almeedus/Chatbot-IA.git
```
### ⚙️ Cofigurando o .env
É importante criar um arquivos com variáveis a serem utilizadas pela aplicação, como porta onde a API irá rodar e o nome do DataBase e a chave da API que irá acessar, dessa forma crie um arquivo `.env` e insira as seguintes informações:
```bash
OPENAI_API_KEY = "INFORME SUA CHAVE DE API" 
MONGODB_NOME = "minhabasededados"
MONGODB_PORTA = 8080
```
Substitua o `"minhabasebasededados"` pelo seu banco de dados criado no MongoDB e `8080` pela porta que deseja rodar a aplicação.

### 🏁 Rodando a Aplicação

Use o comando `pip install -r requirements.txt` para instalar as dependências do projeto
```bash
pip install -r requirements.txt
```
Use o comando `uvicorn main:app` para iniciar a aplicação na porta indicada no [.env](#️-cofigurando-o-env)
```bash
uvicorn main:app
```
Use o comando `uvicorn main:app --reload` para iniciar a aplicação em modo desenvolvimento na porta indicada no [.env](#️-cofigurando-o-env)
```bash
uvicorn main:app --reload
```
<hr>

## ⚓ Endpoints

### 📒 Editais
| EndPoint | Método | Descrição | Corpo da Requisição |
| --- | --- | --- | --- |
| / | GET | Teste | N/A |
| /duvidas | POST| Inserir uma pergunta | `{"query": "Informe sua pergunta"}` |


<hr>

## 📁 Estrutura das Pastas

```
requirements.txt      # Bibliotecas necessárias para o funcionamento
main.py               # Início da aplicação
database.py           # Configurações de conexão do banco de dados
.env                  # Arquivo das variáveis de ambiente
src
└───edital            # Edital para consulta
```
<hr>

## 📈 Progresso do Desenvolvimento

#### 📒 Editais
- [x] Inserir edital do processo seletivo;
- [x] Rota de pesquisa;
- [x] Ler editais;
- [ ] Utilizar modelo gpt4-o treinado;
- [ ] Consultar editais relacionados a um usuário.

#### 👤 Consultas
- [ ] Salvar resultados pesquisa;
- [ ] Consultar as 5 pesquisas mais feitas.

<hr>
🫂 Obrigado por usar o AssistIF!