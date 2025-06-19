import typer
from rich.console import Console
from rich.panel import Panel
import rich.spinner as spinner
from typing_extensions import Annotated
from .llm_client import OllamaClient
from pathlib import Path
from .celebrate import display_celebration_animation

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
    "Python": "pytest",
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


def analyse_source_file(filepath: Path) -> tuple[str, str, str]:
    """
    Analyzes the source file to determine its language and framework.
    Returns a tuple of (language, framework).
    """
    console.print(f"Analysing file: {filepath.name}")

    code_file = filepath.read_text()
    language = EXTENSION_TO_LANGUAGE.get(filepath.suffix)

    if not language:
        console.print(Panel(f"Error: Unknow file type '{filepath.suffix}'. Does not support test generation for this file type.", title="[bold red]Error", border_style="red"))
        raise typer.Exit(code=1)
    
    framework = LANGUAGE_TO_FRAMEWORK.get(language)
    console.print(f"Detected language: {language} | Selected framework: {framework}")

    return code_file, language, framework
    

def determine_output_path(sourcepath: Path, language: str) -> Path:
        # Create test files
    name_generator = LANGUAGE_TO_TEST_FILENAME.get(language)
    if not name_generator:
        console.print(Panel(f"Error: No test file name generator for {language}.", title="[bold red]Error", border_style="red"))
        raise typer.Exit(code=1)
    test_filename = name_generator(sourcepath.stem)

    try:
        # tries to create a path like "example_tests/example_files/test_file.py" from "example_files/test_file.py". Usually it'd be from src folder but there we have given it example_files as the root.
        # this is to ensure that the test files are created in a structured way.
        relative_path = sourcepath.relative_to("example_files")
        test_file_path = Path("example_tests") / relative_path.with_name(test_filename)
    except ValueError:
        test_file_path = Path("example_files") / test_filename

    return test_file_path

def write_test_file(output_path: Path, content: str, force: bool):
    """
    Writes the generated test content to the specified file path.
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)

    if output_path.exists() and not force:
        console.print(Panel(f"Test file already exists at [cyan]{output_path}[green]. \nUse the --force or -f flag to overwrite.", title="[bold yellow]Operation Cancelled", border_style="yellow"))
        raise typer.Exit(code=1)
    
    output_path.write_text(content)
    console.print(Panel(f"Successfully created test file:\n[green]{output_path}[/green]", title="✅ [bold green]Success", border_style="green"))
    display_celebration_animation()


@app.command()
def main(
    filepath: Annotated[Path, typer.Argument(..., exists=True, file_okay=True, dir_okay=False, readable=True, help="The path to the file to create test for.")],
    model: Annotated[str, typer.Option(help="The Ollama model to use for creating tests.")] = "qwen2.5-coder:7b",
    force: Annotated[bool, typer.Option("--force")] = False,
    endpoint:  Annotated[str, typer.Option(help="The endpoint of the Ollama server to use for creating tests.")] = "http://localhost:11434/api/chat"
):

    """
    Generates a unit test for a given code snippet using a local LLM.
    """

    client = OllamaClient(endpoint) 

    code_file, language, framework = analyse_source_file(filepath)

    with console.status("[bold green]Generating test...[/bold green]", spinner="dots"):

        result = client.generate_test(code_file, language, framework, model)

    # Check for errors returned from the client
    if result.startswith("Error:"):
        console.print(Panel(result, title="[bold red]Error", border_style="red"))
        raise typer.Exit(code=1)
    
    output_path = determine_output_path(filepath, language)

    write_test_file(output_path, result, force)
    
  
    # Display the successful result in a nice panel
    # console.print(Panel(result, title="[bold green]Generated Unit Test", border_style="green", expand=True))

if __name__ == "__main__":
    app()