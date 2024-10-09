from deepeval import assert_test
from deepeval.test_case import LLMTestCase
from deepeval.metrics import AnswerRelevancyMetric

from langchain_openai import AzureOpenAI
import os

endpoint = os.getenv("ENDPOINT_URL", "https://winwireazuretraining.openai.azure.com/")
deployment = os.getenv("DEPLOYMENT_NAME", "text_demo")
subscription_key = os.getenv("AZURE_OPENAI_API_KEY", "0f3ba1630da5452f87ae9186ccd4d668")

rag_model = AzureOpenAI(
    azure_endpoint=endpoint,
    azure_deployment=deployment,
    api_key=subscription_key,
    api_version = "2024-05-01-preview",
)

print(rag_model)

test_case = LLMTestCase(input='Which is better, Python or R Language', actual_output='Python')
relevancy_metric = AnswerRelevancyMetric(threshold=0.9, model=rag_model)

relevancy_metric.measure(test_case=test_case)
print(relevancy_metric.score, relevancy_metric.reason)