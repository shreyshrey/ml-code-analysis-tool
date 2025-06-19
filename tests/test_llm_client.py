import pytest
from test_generator.llm_client import OllamaClient

client = OllamaClient()

def test_build_prompt_contains_all_components():
    """
    Tests if the generated prompt correctly includes the language, framework, and code.
    """
    language = "Python"
    framework = "pytest"
    code = "def hello():\n    return 'world'"

    prompt = client._build_prompt(code, language, framework)

    assert "expert Python developer" in prompt
    assert "pytest testing framework" in prompt
    assert "def hello():" in prompt
    assert "world" in prompt
