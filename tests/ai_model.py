import os
from deepeval.models import DeepSeekModel

ds_model = DeepSeekModel(
        model="deepseek-chat",
        api_key=os.getenv("DEEPSEEK_API_KEY"),
        temperature=0
        )
