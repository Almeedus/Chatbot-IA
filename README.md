# Chatbot-IA

<center>

![Logo ChatbotIA](https://raw.githubusercontent.com/Almeedus/Chatbot-IA/refs/heads/main/src/Logo.png)

</center>

> Imagem de autoria própria


<hr>

## 🌐 Visão Geral
O Chatbot IA é um sistema construído em VueJS, Python e Redis. Permite que os usuários utilizem o sistema por meio de requesições contendo dúvidas baseadas nos editais de vestibular do Instituto Federal de São Paulo.

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
- Redis instalado;
- Conhecimentos em Redis.

[`📗 Guia de Instação Python`](https://www.python.org/downloads/)
[`📙 Guia de Instação Redis`](https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/)

<hr>

## 🛠️ Stack Utilizada
A linguagem ecolhida foi TypeScript juntamente com Python e o banco de dados não relacional Redis. Entre as bibliotecas utilizadas, as principais são:

- [LangChain](https://www.langchain.com/langchain)
- [Redis](https://redis.io/docs/latest/develop/clients/redis-py/)
- [FastAPI](https://fastapi.tiangolo.com/)

![Diagrama da Stack](https://raw.githubusercontent.com/Almeedus/Chatbot-IA/refs/heads/main/src/diagrama-stack.png)
> Imagem feita utilizando o [Excalidraw](https://excalidraw.com/)

<hr>

## 🚩 Iniciando a Aplicação
Antes de tudo você deve ter o Redis e o Python instalados conforme os [pré-requisitos](#-pré-requisitos).

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
REDIS_HOST = "localhost"
REDIS_PORT = 6379
```
Substitua o `"localhost"` pelo seu banco de dados criado no Redis e `6379` pela porta que deseja rodar a aplicação.

### 🏁 Rodando a Aplicação

Use o comando `pip install -r requirements.txt` para instalar as dependências do projeto
```bash
pip install -r requirements.txt
```
Use o comando `uvicorn main:app` para iniciar a aplicação na porta indicada no [.env](#️-cofigurando-o-env)
```bash
uvicorn router:app
```
Use o comando `uvicorn main:app --reload` para iniciar a aplicação em modo desenvolvimento na porta indicada no [.env](#️-cofigurando-o-env)
```bash
uvicorn router:app --reload
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
project/
│
├── config.py         # Configurações de ambiente e Redis
├── model.py          # Configurações do LangChain
├── router.py         # Rotas da API com FastAPI
├── src/
│   └── edital_ifsp_itapetininga.pdf
└── .env              # Variáveis de ambiente
```
<hr>

## 📈 Progresso do Desenvolvimento

#### 📒 Editais
- [x] Inserir edital do processo seletivo;
- [x] Rota de pesquisa;
- [x] Ler editais;
- [ ] Utilizar modelo gpt4-o treinado;

#### 👤 Consultas
- [x] Salvar resultados pesquisa;
- [ ] Consultar as 5 pesquisas mais feitas.

<hr>
🫂 Obrigado por usar o Chatbot IA!