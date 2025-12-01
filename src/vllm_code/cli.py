import typer
from rich.console import Console
from .agent import Agent

app = typer.Typer()
console = Console()


@app.command()
def chat():
    """
    Start a conversation with the coding agent (throughline for now)
    """
    agent = Agent()
    console.print("[bold green]Welcome to vLLM-code Agent![/bold green]")
    console.print("Type 'exit' or 'quit' to end the session.")

    while True:
        try:
            user_input = typer.prompt("You")
            if user_input.lower() in ["exit", "quit"]:
                console.print("[bold yellow]Goodbye![/bold yellow]")
                break

            response = agent.chat(user_input)
            console.print(f"[bold blue]Agent:[/bold blue] {response}")

        except KeyboardInterrupt:
            console.print("\n[bold yellow]Goodbye![/bold yellow]")
            break


if __name__ == "__main__":
    app()
