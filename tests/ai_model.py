import os
from deepeval.models import DeepSeekModel
from langchain_deepseek import ChatDeepSeek

ds_model = DeepSeekModel(
        model="deepseek-chat",
        api_key=os.getenv("DEEPSEEK_API_KEY"),
        temperature=0
        )

judge_model = ChatDeepSeek(
        model="deepseek-chat",
        api_key=os.getenv("DEEPSEEK_API_KEY"),
        temperature=0
    )
