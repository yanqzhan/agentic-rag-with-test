from deepeval.tracing import observe, update_current_span
from deepeval.metrics import ContextualRelevancyMetric
from deepeval.dataset import EvaluationDataset, Golden
from deepeval.test_case import LLMTestCase
from langchain_qdrant import QdrantVectorStore
from langchain_ollama import OllamaEmbeddings
from config import collect_name, Qdrant_URL
from tests.ai_model import ds_model


contextual_relevancy = ContextualRelevancyMetric(threshold=0.6, model=ds_model)

embeddings = OllamaEmbeddings(model='nomic-embed-text')
vector_store = QdrantVectorStore.from_existing_collection(
    collection_name=collect_name,
    embedding=embeddings,
    url=Qdrant_URL
)

@observe(metrics=[contextual_relevancy])
def retrieve_context(query: str):
    """Retrieve information to help answer a query."""
    artifact = vector_store.similarity_search(query, k=2)
    retrieval_context = [doc.page_content for doc in artifact]
    update_current_span(
        test_case=LLMTestCase(input=query, retrieval_context=retrieval_context)
    )
    #return content, artifact

#export CONFIDENT_TRACE_FLUSH=1

# Create dataset
dataset = EvaluationDataset(goldens=[Golden(input='RHIVOS是哪个公司的产品？')])
# Loop through dataset
for golden in dataset.evals_iterator():
    retrieve_context(golden.input)
