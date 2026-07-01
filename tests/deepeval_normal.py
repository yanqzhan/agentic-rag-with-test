from rag import agent
from tests.ai_model import ds_model
from deepeval.test_case import LLMTestCase
from deepeval.metrics import (
        AnswerRelevancyMetric,
        ContextualPrecisionMetric,
        ContextualRecallMetric,
        FaithfulnessMetric,
        ContextualRelevancyMetric
        )
from deepeval import evaluate


query = "华为公司相关的车载系统叫什么?"
config = {
        "configurable": {"thread_id": "user1"}
    }


def extract_from_tool_output(tool_output):
    plain_texts = []
    blocks = tool_output.split("\n\n")
    for block in blocks:
        if not block.strip():
            continue
        content_marker = "Content: "
        if content_marker in block:
            content_start = block.find(content_marker) + len(content_marker)
            plain_text = block[content_start:]
            plain_texts.append(plain_text.strip())

    return plain_texts


retrieved_docs = []
for event in agent.stream(
        {"messages": [{"role": "user", "content": query}]},
        {"configurable": {"thread_id": "user1"}},
        stream_mode="values",
        ):
    last_msg = event["messages"][-1]
    if last_msg.type == "tool":
        doc_texts = extract_from_tool_output(last_msg.content)
        retrieved_docs.extend(doc_texts)
result = event["messages"][-1].content
print(f"retrieved_content:\n{retrieved_docs}")
print(f"answer:\n{result}")
print("\n\n")

test_case = LLMTestCase(
        input=query,
        actual_output=result,
        retrieval_context=retrieved_docs,
        expected_output="华为鸿蒙座舱"
)

answer_relevancy = AnswerRelevancyMetric(
        threshold=0.8,
        model=ds_model,
        include_reason=True
    )

contextual_precision = ContextualPrecisionMetric(
        threshold=0.8,
        model=ds_model,
        include_reason=True
    )  # need expected_output

faithfulness = FaithfulnessMetric(
        threshold=0.7,
        model=ds_model,
        include_reason=True
    )

contextual_relevancy = ContextualRelevancyMetric(
    threshold=0.7,
    model=ds_model,
    include_reason=True
)

contextual_recall = ContextualRecallMetric(
    threshold=0.7,
    model=ds_model,
    include_reason=True
)

evaluate([test_case], metrics=[
    answer_relevancy,
    contextual_precision,
    faithfulness,
    contextual_relevancy,
    contextual_recall
    ]
         )
