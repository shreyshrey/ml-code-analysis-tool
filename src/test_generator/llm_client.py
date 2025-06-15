import requests
import json

class OllamaClient:
    def __init__(self, endpoint='http://localhost:11434/api/generate'):
        self.endpoint = endpoint

    def generate_test(self, code_snippet: str, framework: str, model: str) -> str:
        prompt = self._build_prompt(code_snippet, framework)

        payload = {
            "model": model,
            "prompt": prompt,
            "stream": False
        }

        try: 
            response = requests.post(self.endpoint, json=payload, timeout=60)
            response.raise_for_status()  # Raise an error for bad responses

            response_data = response.json()
            generated_code = response_data.get("response", "")
            return self._clean_output(generated_code)
        
        except requests.exceptions.ConnectionError:
            return "Connection error: Unable to reach the Ollama server. Please ensure it's running"
        except KeyError:
            return "Error: The response from the server is missing expected fields."


    def _build_prompt(self, code_snippet: str, framework: str) -> str:
        return f"""
        You are an expert software developer specialising in test generation . Your task is to write a single, complete, and runnable unit test for the provided code snippet using the {framework} framework.
        The code should be clean, easy to understand, and follow best practices.
        Do not add any conversational text, however do explain the purpose of the test in a comment at the top of the code.
        Code to test:
        ```
        {code_snippet}
        ```
        """

    def _clean_output(self, output: str) -> str:
        text = output.strip()
        if text.startswith("```python"):
            text = text[len("```python"):].strip()
        elif text.startswith("```"):
            text = text[len("```"):].strip()

        if text.endswith("```"):
            text = text[:-len("```")].strip()
        return text