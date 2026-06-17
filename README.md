# Agentic RAG with tests

A agentic RAG (Retrieval-Augmented Generation) chatbot with conversation memory, and tests by DeepEval.

## Architecture

- **LLM**: BigModel/ZHIPU(`glm-5.1`) via LangChain for RAG, DeepSeek('deepseek-chat') for DeepEval test.
- **Embeddings**: Ollama (`bge-m3`) running locally
- **Vector Store**: Qdrant (`localhost:6333`, collection `automotives`)
- **Evaluation Framework**: DeepEval

## Files

| File | Description |
|------|-------------|
| `preprocess.py` | Incrementally embeds `.md` doc into Qdrant |
| `rag.py` | Langchain agent with a tool to retrieve contexts from Qdrant |
| `chat.py` | Chatbot to accep user input and call agent to generate response |
| `tests` | Dir with several test program files to evaluate this agentic RAG |

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
ollama pull bge-m3
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

8. Run the tests, for example:
```bash
python -m tests.deepeval_normal
```
You'll get like:
```bash
╭───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ 🚀 DeepEval Evaluation Results                                                                                                                                        │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ ✅ test_case_0 (Passed 2 metrics)                                                                                                                                     │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ Aggregate Metrics                                                                                                                                                     │
│                                                                                                                                                                       │
│  Metric                                                          ┃ Average Score                               ┃ Pass Rate                      ┃ Total               │
│ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━ │
│  Answer Relevancy                                                │ 1.00                                        │ 100.00%                        │ 1                   │
│  Contextual Precision                                            │ 1.00                                        │ 100.00%                        │ 1                   │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

