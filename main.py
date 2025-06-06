import time
from ping3 import ping
from rich.live import Live
from rich.table import Table
from rich.console import Console
from rich.panel import Panel
from rich.progress import BarColumn, Progress

console = Console()
host = "google.com"
results = []


def build_table():
    table = Table(title=f"gping.py - {host}", show_header=True, header_style="bold magenta")
    table.add_column("Ping #", justify="right", style="bold")
    table.add_column("Latencia (ms)", justify="right", style="cyan")

    for i, val in enumerate(results[-30:]):
        color = "green" if val < 100 else "yellow" if val < 200 else "red"
        latency_str = f"[{color}]{val:.2f}[/{color}]" if val else "[red]Timeout[/red]"
        table.add_row(str(i + 1), latency_str)

    return table


with Live(build_table(), refresh_per_second=4, screen=False) as live:
    while True:
        latency = ping(host, unit='ms')
        latency = latency if latency is not None else 0
        results.append(latency)
        live.update(build_table())
        time.sleep(1)
