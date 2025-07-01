import requests

class LLMClient:
    def __init__(self, base_url="http://localhost:11434", model="deepseek-coder:7b"):
        self.base_url = base_url
        self.model = model

    def generate_response(self, prompt: str) -> str:
        """
        Sends a prompt to the local LLM via Ollama and returns the response.
        """
        url = f"{self.base_url}/api/generate"
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }
        response = requests.post(url, json=payload)
        response.raise_for_status()
        data = response.json()
        return data.get("response", "")