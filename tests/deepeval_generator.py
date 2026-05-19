from deepeval.tracing import observe, update_current_span
from deepeval.metrics import AnswerRelevancyMetric
from deepeval.dataset import EvaluationDataset, Golden
from deepeval.test_case import LLMTestCase
from tests.ai_model import ds_model
from rag import llm


answer_relevancy = AnswerRelevancyMetric(threshold=0.6, model=ds_model, include_reason=True)

context_texts = ['| 操作系统 | 官方文档入口 |\n|---------|------------|\n| BlackBerry QNX | [qnx.com](https://www.qnx.com) / [QNX BSP Library](https://qnx.software/en/developers/get-started/board-support-packages) |\n| Android Automotive OS | [Android Developers - Automotive](https://developer.android.com/training/cars) / [AOSP Automotive](https://source.android.com/docs/automotive) |\n| AGL | [docs.automotivelinux.org](https://docs.automotivelinux.org) / [AGL 官网](https://www.automotivelinux.org) |\n| **RHIVOS（红帽）** | [Official RHIVOS Data Sheet](https://www.redhat.com/en/resources/in-vehicle-operating-system-datasheet) / [AutoSD GitHub/Community](https://sigs.centos.org/automotive/) / [AutoSD Hardware Enablement](https://sigs.centos.org/automotive/autosd-10/hardware-enablement/index.html) |\n| 华为鸿蒙座舱 | [华为开发者联盟——智能座舱 OEM 文档中心](https://developer.huawei.com/consumer/cn/overview/ICS) |\n| 斑马智行 AliOS | [AliOS 官网](https://www.alios.cn) / [斑马智行官网](https://www.ebanma.com) |', '- **通用汽车**：2026 年宣布推出移除 CarPlay 的方案，全面转向自研系统 + Android Automotive 深度集成\n- **福特、雷诺、本田、Stellantis**：均在不同车型上采用或计划采用 Android Automotive OS 作为智能座舱方案']


@observe(metrics=[answer_relevancy])
def generator(query: str):
    #state = {"messages": [HumanMessage(content=query + "\\n\\n".join(context_texts))]}
    state = f"仅根据以下内容回答'{query}':{context_texts}"
    print(state)
    result = llm.invoke(state)
    print(result.content)
    update_current_span(test_case=LLMTestCase(input=query, actual_output=result.content))
    return result


# Create dataset
dataset = EvaluationDataset(goldens=[Golden(input="华为公司相关的车载系统叫什么名字？")])

# Loop through dataset
for golden in dataset.evals_iterator():
    generator(golden.input)
