import requests
import json

class OllamaClient:
    def __init__(self, endpoint='http://localhost:11434/api/generate'):
        self.endpoint = endpoint

    def generate_test(self, code_file: str, language: str, framework: str, model: str) -> str:
        prompt = self._build_prompt(code_file, language, framework)

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


    def _build_prompt(self, code: str, language: str, framework: str) -> str:
        return f"""
        You are an expert {language} developer specialising in the {framework} testing framework. Your task is to write a single, complete, and runnable unit test for the provided code for the following {language}.
        The code should be clean, easy to understand, and follow best practices.
        Do not add any conversational text or explanation. Output only the raw, runnable code for a unit test.
        You must write the comment "#Test case n:" on a separate line directly above each assert statement,
        where n represents the test case number, starting from 1 and increasing by one for each subsequent
        test case.
        Code to test:
        ```
        {code}
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