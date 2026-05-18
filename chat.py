from rag import agent

print("🤖 Agent 已启动，输入 'quit/exit' 退出对话。")
session_id = "user1"
while True:
    user_input = input("You: ")
    if user_input.lower() in ('quit','exit'):
        break

    response = agent.invoke(
        {"messages":[{"role":"user", "content":user_input}]},
        {"configurable":{"thread_id":session_id}}
        )

    print(f"🤖 Agent: {response["messages"][-1].content}\n")

