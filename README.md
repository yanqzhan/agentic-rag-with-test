# Agentic RAG with tests

A agentic RAG (Retrieval-Augmented Generation) chatbot with conversation memory, and tests by DeepEval.

## Architecture

- **LLM**: BigModel/ZHIPU(`glm-5.1`) via LangChain for RAG, DeepSeek('deepseek-chat') for DeepEval test.
- **Embeddings**: Ollama (`nomic-embed-text`) running locally
- **Vector Store**: Qdrant (`localhost:6333`, collection `automotives`)

## Files

| File | Description |
|------|-------------|
| `chatbot.py` | Gradio web UI that serves the chatbot |
| `ingest.py` | Incrementally embeds `.md` docs from `DOCS_PATH` into Qdrant |

## Prerequisites

- Python 3.13+
- Ollama installed and running (`ollama serve`)
- Qdrant running on `localhost:6333` (see below)
- DeepSeek and ZAI(BigModel) API key

## Setup

1. Start Qdrant (Docker):

```bash
docker run -d --name qdrant -p 6333:6333 -p 6334:6334 \
  -v qdrant_storage:/qdrant/storage \
  qdrant/qdrant
```

2. Install dependencies:

```bash
pip install -U -r requirements.txt
```

3. Install spaCy model (required by Mem0):

```bash
pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.8.0/en_core_web_sm-3.8.0-py3-none-any.whl
```

4. Pull the embedding model:

```bash
ollama pull nomic-embed-text
```

5. Clain your API keys by export or a `.env` file:

```
export DEEPSEEK_API_KEY=your-deepseek-api-key
OR in .env:
DEEPSEEK_API_KEY=your-deepseek-api-key
```

6. Preprocess documents:

```bash
python preprocess.py
```

7. Run the chatbot:

```bash
python chat.py
```
