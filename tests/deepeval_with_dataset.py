import json

from deepeval import evaluate
from deepeval.test_case import LLMTestCase
from deepeval.metrics import (
        AnswerRelevancyMetric,
        FaithfulnessMetric,
        ContextualPrecisionMetric,
        ContextualRecallMetric
        )

from rag import agent
from tests.ai_model import ds_model


def load_test_dataset(dataset_path="data/test_dataset.json"):
    """
    Loading test dataset
    """
    with open(dataset_path, 'r') as f:
        data = json.load(f)
    return data["test_cases"]


def extract_from_tool_output(tool_output):
    """
    Extracting retrieval contents from tool message
    """
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


def create_test_case(test_item):
    """
    Creating DeepEval TestCase according to test items
    """
    question = test_item["question"]
    expected_answer = test_item["expected_answer"]

    retrieved_docs = []
    for event in agent.stream(
            {"messages": [{"role": "user", "content": question}]},
            {"configurable": {"thread_id": "user1"}},
            stream_mode="values",
            ):
        last_msg = event["messages"][-1]
        if last_msg.type == "tool":
            doc_texts = extract_from_tool_output(last_msg.content)
            retrieved_docs.extend(doc_texts)
    actual_output = event["messages"][-1].content

    retrieval_context = retrieved_docs

    return LLMTestCase(
            input=question,
            actual_output=actual_output,
            expected_output=expected_answer,
            retrieval_context=retrieval_context,
            context=retrieval_context
            )


test_cases = load_test_dataset()

standard_tests = [t for t in test_cases if t["category"] == "standard"]
boundary_tests = [t for t in test_cases if t["category"] == "boundary"]
negative_tests = [t for t in test_cases if t["category"] == "negative"]

print(f"Loading datasets: standard {len(standard_tests)},"
      f"boundary {len(boundary_tests)},"
      f"negative {len(negative_tests)}")

# For standard, boundary tests
metrics_pos = [
    AnswerRelevancyMetric(threshold=0.7, model=ds_model),
    FaithfulnessMetric(threshold=0.7, model=ds_model),
    ContextualPrecisionMetric(threshold=0.7, model=ds_model),
    ContextualRecallMetric(threshold=0.7, model=ds_model)
        ]

pos_tests = standard_tests + boundary_tests
test_cases_pos = [create_test_case(t) for t in pos_tests]
evaluate(test_cases_pos, metrics_pos)

# For negative tests
metrics_neg = [
        AnswerRelevancyMetric(threshold=0.7, model=ds_model),
        FaithfulnessMetric(threshold=0.7, model=ds_model)
        ]
test_cases_neg = [create_test_case(t) for t in negative_tests]
evaluate(test_cases_neg, metrics_neg)
