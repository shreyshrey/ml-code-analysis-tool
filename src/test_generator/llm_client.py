import requests
import json

class OllamaClient:
    def __init__(self, endpoint='http://localhost:11434/api/chat'):
        self.endpoint = endpoint

    def generate_test(self, code_file: str, language: str, framework: str, model: str) -> str:
        prompt = self._build_test_prompt(code_file, language, framework)

        payload = {
            "model": model,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "stream": False
        }

        try: 
            response = requests.post(self.endpoint, json=payload, timeout=60)
            response.raise_for_status()  # Raise an error for bad responses

            response_data = response.json()
            generated_code = response_data.get("message", {}).get("content", "")
            if not generated_code:
                return "Error: No code generated. Please check the model and prompt."
            return self._clean_output(generated_code)
        
        except requests.exceptions.ConnectionError:
            return "Connection error: Unable to reach the Ollama server. Please ensure it's running."
        except KeyError:
            return "Error: The response from the server is unexpected."


    def translate_code(self, code: str, source_language: str, target_language: str, model: str) -> str:
        prompt = self._build_translation_prompt(code, source_language, target_language)

        payload = {
            "model": model,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "stream": False
        }

        try: 
            response = requests.post(self.endpoint, json=payload, timeout=90)
            response.raise_for_status()  
            response_data = response.json()
            translated_code = response_data.get("message", {}).get("content", "")
            if not translated_code:
                return "Error: Model returned an empty response"
            return self._clean_output(translated_code)
        
        except requests.exceptions.ConnectionError:
            return "Error: Could not connect to Ollama. Please ensure it's running."
        except requests.exceptions.RequestException as e:
            return f"Error: API request failed: {e}. Is your Ollama version up to date?"
        except KeyError:
            return "Error: Unexpected response format from Ollama's /api/chat endpoint."



    def _build_translation_prompt(self, code:str, source_language: str, target_language: str) -> str:
        return f"""
        You are an expert polyglot programmer who specializes in translating code from one language to another.
        Your task is to translate the following {source_language} code snippet into idiomatic {target_language}.
        The translated code should be clean, efficient, and follow all best practices of the target language.
        Provide only the raw code for the new language, without any explanations, notes, or markdown fences.

        Translate this {source_language} code to {target_language}:
        Code to test:
        ```
        {code}
        ```
        """
    

    def _build_test_prompt(self, code: str, language: str, framework: str) -> str:
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
    
    