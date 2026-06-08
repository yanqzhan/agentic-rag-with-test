from rag import agent
from tests.ai_model import ds_model
from deepeval.test_case import ConversationalTestCase, Turn
from deepeval.metrics import TurnRelevancyMetric, TurnFaithfulnessMetric
from deepeval import evaluate

actual_turns = []
message_history = []
test_turns = []
query_1 = "BlackBerry开发的系统叫什么？"
query_2 = "有哪些其它公司的车载系统底层也授权使用了该系统？"

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

message_history = []
def get_content_context(query):
    retrieved_docs = []
    for event in agent.stream(
                #{"messages": message_history + [("user", query)]},
                {"messages":[("user", query)]},
                {"configurable":{"thread_id":"user1"}},
                stream_mode="values",
                ):
                last_msg = event["messages"][-1]
                if last_msg.type == "tool":
                    doc_texts = extract_from_tool_output(last_msg.content)
                    retrieved_docs.extend(doc_texts)
    content = last_msg.content
    message_history.append(("user", query))
    message_history.append(("assistant", content))
    return content, retrieved_docs

for query in [query_1, query_2]:
    ai_content, ai_context = get_content_context(query)
    test_turns.append(Turn(role="user", content=query))
    test_turns.append(Turn(role="assistant", content=ai_content, retrieval_context=ai_context))

#print(f"test_turns:\n{test_turns}")

test_case = ConversationalTestCase(turns=test_turns)

turn_faithfulness = TurnFaithfulnessMetric(model=ds_model)
turn_relevancy = TurnRelevancyMetric(model=ds_model)

evaluate([test_case], metrics=[turn_faithfulness, turn_relevancy])

