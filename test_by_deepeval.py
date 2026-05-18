import os
from rag import agent
from deepeval.test_case import LLMTestCase
from deepeval.metrics import AnswerRelevancyMetric, ContextualPrecisionMetric
from deepeval import evaluate
from deepeval.models import DeepSeekModel

query = "华为公司相关的车载系统叫什么?"
config = {
        "configurable": {"thread_id": "user1"}
    }

retrieved_docs = []
for event in agent.stream(
        {"messages": [{"role": "user", "content": query}]},
        {"configurable":{"thread_id":"user1"}},
        stream_mode="values",
        ):
        last_msg = event["messages"][-1]
        if last_msg.type == "tool":
            doc_texts = [doc.page_content for doc in last_msg.artifact]
            retrieved_docs.extend(doc_texts)
result = event["messages"][-1].content
print(f"retrieved_content:\n{doc_texts}")
print(f"answer:\n{result}")
print("\n\n")

test_case = LLMTestCase(
        input=query,
        actual_output=result,
        retrieval_context=retrieved_docs,
        expected_output="华为鸿蒙座舱"
)

ds_model = DeepSeekModel(
    model="deepseek-chat",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    temperature=0
)

answer_relevancy = AnswerRelevancyMetric(threshold=0.8, model=ds_model)
contextual_precision = ContextualPrecisionMetric(threshold=0.8, model=ds_model) # need expected_output
evaluate([test_case], metrics=[answer_relevancy, contextual_precision])
