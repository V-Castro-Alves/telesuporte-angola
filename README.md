# TeleSupport Angola API

Esta é uma solução inteligente para call centers que utiliza IA para transcrever, analisar e buscar informações em chamadas de voz, utilizando a tecnologia do Google Gemini.

## 🚀 Funcionalidades
- **Transcrição de Alta Precisão:** Converte áudio em texto usando o modelo Whisper (via `faster-whisper`).
- **Análise Inteligente (Gemini 1.5 Flash):** 
    - **Sumarização:** Resumo automático e conciso da chamada.
    - **Classificação:** Categorização automática (Reclamação, Dúvida, Elogio, Cancelamento).
    - **Análise de Sentimento:** Identificação do tom predominante (Positivo, Neutro, Negativo).
- **RAG (Busca Semântica):** Armazena o histórico no **ChromaDB** e permite realizar consultas inteligentes baseadas no contexto das chamadas passadas.

## 🛠️ Requisitos
- Python 3.9 ou superior.
- Chave de API do [Google AI Studio](https://aistudio.google.com/).

## 📦 Instalação

1. **Clone o repositório e acesse a pasta:**
   ```bash
   cd telesuporte_angola
   ```

2. **Crie e ative um ambiente virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

## ⚙️ Configuração

1. Crie um arquivo `.env` na raiz do projeto:
   ```bash
   cp .env .env
   ```
2. Edite o arquivo `.env` e insira sua chave de API:
   ```env
   GOOGLE_API_KEY=sua_chave_aqui
   MODEL_NAME=gemini-1.5-flash
   ```

## 🚦 Como Executar

Inicie o servidor FastAPI:
```bash
python main.py
```
A API estará disponível em `http://localhost:8000`. Acesse `http://localhost:8000/docs` para ver a documentação interativa (Swagger).

## 📡 Endpoints Principais

### 1. Processar Chamada
`POST /process-call`
Envia um arquivo de áudio para transcrição e análise.
- **Parâmetro:** `file` (Upload de arquivo .mp3, .wav, .ogg, etc.)

### 2. Busca Semântica (RAG)
`GET /search?query={pergunta}`
Realiza uma busca no histórico de chamadas.
- **Exemplo:** `/search?query=Quais foram as reclamações sobre internet?`

## 🧪 Testes Rápidos
Você pode usar o script `test_api.py`:
```bash
# Para processar um áudio
python test_api.py process caminho/do/audio.mp3

# Para fazer uma pergunta ao sistema
python test_api.py search "Qual o sentimento geral das chamadas?"
```