from rich.console import Console
from rich.panel import Panel
from sistema import *

console = Console()

def menu():
    console.print(Panel.fit(
        "[bold]1[/] - Cadastrar médico\n"
        "[bold]2[/] - Cadastrar paciente\n"
        "[bold]3[/] - Agendar consulta\n"
        "[bold]4[/] - Ver histórico de paciente\n"
        "[bold]5[/] - Ver info de médico\n"
        "[bold]6[/] - Sair",
        title="[bold cyan]🏥 CLÍNICA MÉDICA[/]",
        border_style="cyan"
    ))

while True:
    menu()
    try:
        op = int(input('Digite a opção: '))
        if op == 1:
            cadastrar_medico()
        elif op == 2:
            cadastrar_paciente()
        elif op == 3:
            agendar_consulta()
        elif op == 4:
            ver_historico()
        elif op == 5:
            ver_medico()
        elif op == 6:
            break
    except ValueError:
        print('[red]ERRO![/] Digite apenas números!')
        continue