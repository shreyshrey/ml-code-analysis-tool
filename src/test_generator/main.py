import typer
from rich.console import Console
from rich.panel import Panel
from rich.spinner import Spinner
from .llm_client import OllamaClient
from pathlib import Path

app = typer.Typer()
console = Console()

EXTENSION_TO_LANGUAGE = {
    ".py": "Python",
    ".js": "JavaScript",
    ".ts": "TypeScript",
    ".java": "Java",
    ".go": "Go",
    ".rs": "Rust",
    ".rb": "Ruby",
    ".cs": "C#",
}

LANGUAGE_TO_FRAMEWORK = {
    "Python": "unittest",
    "JavaScript": "Jest",
    "TypeScript": "Jest",
    "Java": "JUnit",
    "Go": "testing",
    "Rust": "cargo test",
    "Ruby": "RSpec",
    "C#": "NUnit",
}

LANGUAGE_TO_TEST_FILENAME = {
    "Python": lambda stem: f"test_{stem}.py",
    "JavaScript": lambda stem: f"{stem}.test.js",
    "TypeScript": lambda stem: f"{stem}.test.ts",
    "Java": lambda stem: f"{stem}Test.java",
    "Go": lambda stem: f"{stem}_test.go",
    "Rust": lambda stem: f"{stem}_test.rs", 
    "Ruby": lambda stem: f"{stem}_spec.rb",
    "C#": lambda stem: f"{stem}Tests.cs",
}

@app.command()
def main(
    filepath: Path = typer.Argument(..., exists=True, file_okay=True, dir_okay=False, readable=True, help="The path to the file to create test for."),
    model: str = typer.Option("codellama:7b", help="The Ollama model to use for creating tests.")
):
    """
    Generates a unit test for a given code snippet using a local LLM.
    """
    console.print(f"Analysing file: {filepath.name}")

    code_file = filepath.read_text()
    language = EXTENSION_TO_LANGUAGE.get(filepath.suffix)

    if not language:
        console.print(Panel(f"Error: Unknow file type '{filepath.suffix}'. Does not support test generation for this file type.", title="[bold red]Error", border_style="red"))
        raise typer.Exit(code=1)
    
    framework = LANGUAGE_TO_FRAMEWORK.get(language)
    console.print(f"Detected language: {language} | Selected framework: {framework}")

    client = OllamaClient()

    with console.status("[bold green]Generating test...[/bold green]", spinner="dots"):

        result = client.generate_test(code_file, language, framework, model)

    # Check for errors returned from the client
    if result.startswith("Error:"):
        console.print(Panel(result, title="[bold red]Error", border_style="red"))
        raise typer.Exit(code=1)

    # Display the successful result in a nice panel
    console.print(Panel(result, title="[bold green]Generated Unit Test", border_style="green", expand=True))

if __name__ == "__main__":
    app()