from types import SimpleNamespace

import openai


class LLMClient:
    """TODO"""

    def __init__(
        self,
        api_base_url: str,
        api_key: str,
        model: str,
        temperature: float,
    ):
        self._client = openai.OpenAI(
            base_url=api_base_url,
            api_key=api_key,
        )
        self.model_config = SimpleNamespace(
            model=model,
            temperature=temperature,
        )

    def chat(self, messages, **kwargs) -> str:
        """TODO"""
        completion = self._client.chat.completions.create(
            messages=messages,
            **vars(self.model_config),
            **kwargs,
        )
        return completion.choices[0].messages.content
