# Agentic RAG with tests

An agentic RAG (Retrieval-Augmented Generation) system with tests(DeepEval, Security, etc).

> **📌 Notice**: This project is for personal portfolio demonstration only. Please review the full [Disclaimer](#-disclaimer) before use.

---

<details>
<summary><b>📋 Disclaimer</b> — click to expand</summary>

**This repository is intended for personal portfolio demonstration and technical exploration purposes only.**

### 1. Permitted Use & Restrictions
The entire project, including but not limited to all source code, documentation, datasets, and related materials (collectively, the "Project"), is made available for viewing, evaluation, learning, and technical reference purposes.

You are permitted to:
- View, fork, clone, and locally run the Project for non-commercial evaluation or personal study.
- Reference the Project in discussions, reviews, or technical articles, provided that you clearly attribute the original source and do not present it as your own work.

The following uses are strictly prohibited without prior written authorization:
- Any commercial use, including but not limited to integration into products or services offered for sale.
- Any unlawful use or use that violates applicable laws or regulations.
- Any misleading, deceptive, or fraudulent use, including but not limited to presenting the Project's outputs, data, or reports as official, endorsed, or factually verified information from any real manufacturer, brand, or regulatory authority.
- Any act that infringes upon the author's intellectual property rights, including removing, altering, or obscuring copyright notices, attribution, or this disclaimer.

### 2. No Warranty & Disclaimer
THE PROJECT IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND NONINFRINGEMENT.

In no event shall the author be liable for any claim, damages, or other liability, whether in an action of contract, tort, or otherwise, arising from, out of, or in connection with the Project or the use or other dealings in the Project.

### 3. Data & Report Disclaimer
The in-vehicle system survey report and any associated data contained in this Project are strictly for technical illustration purposes. They are either simulated examples, publicly available anonymized information, or purely hypothetical content. The Project does not contain, reference, or rely upon any sensitive regulatory data (including but not limited to financial, healthcare, legal, or personal identifying information).

These materials do not represent the actual stance, performance, or data of any real manufacturer, brand, or product, and must not be used as a basis for any real-world decision-making, procurement, or policy formulation. Any use of these materials in a manner that could mislead others into believing they represent verified, official, or real-world data is expressly forbidden.

### 4. Liability & Enforcement
Any use of the Project in violation of the above restrictions is at the user's own risk, and the user shall bear full legal responsibility. The author reserves the right to take legal action against any unauthorized commercial use, fraudulent/misleading use, or infringement of these terms, including but not limited to seeking injunctive relief and damages.

---
*All rights reserved. This disclaimer is subject to the exclusive jurisdiction of the author's local laws.*

</details>


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
| `chat.py` | Chatbot to accept user input and call agent to generate response |
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

5. Configure your API keys by export or a `.env` file:

```
export DEEPSEEK_API_KEY=your-deepseek-api-key
# OR in .env:
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

8. Run the tests:
- All tests scripts are under "tests/" directory, especially the deepeval_with_dataset.py(standard, boundary, negative tests) and test_security.py(direct/indirect/jailbreak tests) would be valuable.
- A basic example:
```bash
python -m tests.deepeval_normal
```
You'll get output like:
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

