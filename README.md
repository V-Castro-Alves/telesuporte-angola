# TeleSupport Angola API

Esta é uma solução inteligente para call centers que utiliza IA para transcrever, analisar e buscar informações em chamadas de voz.

## Funcionalidades
- **Transcrição:** Converte áudio em texto usando Whisper.
- **Análise Inteligente:** Sumarização, classificação e análise de sentimento via Grok (xAI).
- **RAG (Busca Semântica):** Armazena transcrições no ChromaDB e permite buscas inteligentes baseadas no histórico de chamadas.

## Como Executar

### 1. Requisitos
- Python 3.9+
- Chave de API da xAI (Grok)

### 2. Instalação
```bash
pip install -r requirements.txt
```

### 3. Configuração
Edite o arquivo `.env` e insira sua `XAI_API_KEY`.

### 4. Iniciar a API
```bash
python main.py
```
A API estará disponível em `http://localhost:8000`. Você pode acessar a documentação interativa em `http://localhost:8000/docs`.

## Endpoints Principais
- `POST /process-call`: Envie um arquivo de áudio para transcrição e análise.
- `GET /search?query=pergunta`: Faça uma busca semântica no banco de chamadas processadas.

## Exemplo de Teste
Você pode usar o script `test_api.py` (se fornecido) ou usar `curl`:

```bash
curl -X POST "http://localhost:8000/process-call" -F "file=@caminho/para/seu/audio.mp3"
```
