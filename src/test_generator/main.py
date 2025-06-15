import typer
from rich.console import Console
from rich.panel import Panel
from rich.spinner import Spinner
from .llm_client import OllamaClient
from pathlib import Path

app = typer.Typer()
console = Console()

@app.command()
def main(
    code: str = typer.Option(..., help="The code snippet to be tested."),
    framework: str = typer.Option("pytest", help="The testing framework to use."),
    model: str = typer.Option("codellama:7b", help="The Ollama model to use.")
):
    """
    Generates a unit test for a given code snippet using a local LLM.
    """
    client = OllamaClient()

    with console.status("[bold green]Generating test with Code Llama...", spinner="dots") as status:
        result = client.generate_test(code, framework, model)

    # Check for errors returned from the client
    if result.startswith("Error:"):
        console.print(Panel(result, title="[bold red]Error", border_style="red"))
        raise typer.Exit(code=1)

    # Display the successful result in a nice panel
    console.print(Panel(result, title="[bold green]Generated Unit Test", border_style="green", expand=True))

if __name__ == "__main__":
    app()