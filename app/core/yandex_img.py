import openai
import httpx

from app.core.config import config


client = openai.OpenAI(
    api_key=config.YANDEX_API_KEY,
    base_url="https://ai.api.cloud.yandex.net/v1",
    project=config.YANDEX_FOLDER_ID,
    http_client=httpx.Client(trust_env=False, timeout=120.0),
)

model_name = f"art://{config.YANDEX_FOLDER_ID}/{config.YANDEX_MODEL}"