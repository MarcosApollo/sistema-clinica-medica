from abc import ABC, abstractmethod
from rich import print

class Pessoa(ABC):

    def __init__(self, nome:str, cpf:str):
        self.__nome = nome
        self.__cpf = cpf

    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    @abstractmethod
    def info(self):
        pass

class Medico(Pessoa):

    def __init__(self, nome, cpf, crm:str, especialidade:str, valor_consulta:float):
        super().__init__(nome, cpf)
        self.__crm = crm
        self.__especialidade = especialidade
        self.__valor_consulta = valor_consulta

    @property
    def crm(self):
        return self.__crm

    @property
    def especialidade(self):
        return self.__especialidade

    def info(self):
        return (f"[bold]Médico:[/] {self.nome}\n"
                f"[bold]CRM:[/] {self.__crm}\n"
                f"[bold]Especialidade:[/] {self.__especialidade}\n"
                f"[bold]Valor consulta:[/] R${self.__valor_consulta:,.2f}")

class Paciente(Pessoa):

    def __init__(self, nome, cpf, plano:str):
        super().__init__(nome, cpf)
        self.__historico = []
        self.__plano = plano

    @property
    def historico(self):
        return self.__historico

    @property
    def plano(self):
        return self.__plano

    def adicionar_consulta(self, c):
        self.__historico.append(c)
        print(f"[green]Consulta adicionada ao histórico de {self.nome}![/]")

    def info(self):
        return (f"[bold]Paciente:[/] {self.nome}\n"
                f"[bold]Historico:[/] {self.historico}\n"
                f"[bold]Plano:[/] {self.plano}")

class Consulta:

    def __init__(self, medico:Medico, paciente:Paciente, data:str, hora:str):
        self.__medico = medico
        self.__paciente = paciente
        self.__data = data
        self.__hora = hora

    @property
    def medico(self):
        return self.__medico

    @property
    def paciente(self):
        return self.__paciente

    @property
    def data(self):
        return self.__data

    @property
    def hora(self):
        return self.__hora

    def resumo(self):
        return (f"[bold]Paciente:[/] {self.__paciente.nome}\n"
                f"[bold]Médico:[/] {self.__medico.nome}\n"
                f"[bold]Data:[/] {self.data}\n"
                f"[bold]Hora:[/] {self.hora}")

    def __str__(self):
        return self.resumo()

    def __repr__(self):
        return self.resumo()

medicos = []
pacientes = []

def cadastrar_medico():

    nome = str(input("Digite o nome do medico: "))
    while nome == "":
        print("[yellow]AVISO[/]\nO campo 'nome' está vazio, para continuar digite o nome corretamente.")
        nome = str(input("Digite o nome do medico: "))
        
    cpf = str(input("Digite o cpf do medico: "))
    while cpf == "":
        print("[yellow]AVISO[/]\nO campo 'cpf' está vazio, para continuar digite o cpf corretamente.")
        cpf = str(input("Digite o cpf do medico: "))
        
    crm = str(input("Digite o crm do medico: "))
    while crm == "":
        print("[yellow]AVISO[/]\nO campo 'crm' está vazio, para continuar digite o crm corretamente.")
        crm = str(input("Digite o crm do medico: "))

    especialidade = str(input("Digite a especialidade do medico: "))
    while especialidade == "":
        print("[yellow]AVISO[/]\nO campo 'especialidade' está vazio, para continuar digite a especialidade corretamente.")
        especialidade = str(input("Digite a especialidade do medico: "))

    try:
        valor_consulta = float(input("Digite o valor da consulta: "))
    except ValueError:
        print("[red]ERRO[/]\nOcorreu um erro na digitação do valor.")
        return

    medico = Medico(nome, cpf, crm, especialidade, valor_consulta)
    medicos.append(medico)
    print(f"[green]SUCESSO![/] Médico {nome} cadastrado!")

def cadastrar_paciente():

    nome = str(input("Digite o nome do paciente: "))
    while nome == "":
        print("[yellow]AVISO[/]\nO campo 'nome' está vazio, para continuar digite o nome corretamente.")
        nome = str(input("Digite o nome do paciente: "))
        
    cpf = str(input("Digite o cpf do paciente: "))
    while cpf == "":
        print("[yellow]AVISO[/]\nO campo 'cpf' está vazio, para continuar digite o cpf corretamente.")
        cpf = str(input("Digite o cpf do paciente: "))

    plano = str(input("Digite o plano do paciente: HapVida/Unimed: "))
    while plano == "":
        print("[yellow]AVISO[/]\nO campo 'plano' está vazio, para continuar digite o plano corretamente.")
        plano = str(input("Digite o plano do paciente: "))

    paciente = Paciente(nome, cpf, plano)
    pacientes.append(paciente)
    print(f"[green]SUCESSO![/] Paciente {nome} cadastrado!")

def agendar_consulta():

    print("Lista de medicos disponiveis")
    print(medicos)
    nome_medico = str(input("Digite o nome do medico que deseja marcar um horario : "))
    medico_encontrado = None
    for medico in medicos:
        if medico.nome == nome_medico:
            medico_encontrado = medico
            break
    if not medico_encontrado:
        print("[red]Médico não encontrado![/]")
        return

    print("Lista de pacientes")
    print(pacientes)
    nome_paciente = str(input("Digite o nome do paciente que deseja marcar uma consulta: "))
    paciente_encontrado = None
    for paciente in pacientes:
        if paciente.nome == nome_paciente:
            paciente_encontrado = paciente
    if not paciente_encontrado:
        print("[red]Paciente não encontrado![/]")
        return

    print("Data e horario de agendamento")
    data = str(input("Didite a data 'dia/mes/ano': "))
    while data == "":
        print("[yellow]AVISO[/]\nO campo 'data' está vazio, para continuar digite o data corretamente.")
        data = str(input("Didite a data dia/mes/ano: "))
    horario = str(input("Didite o horario 'hh:mm': "))
    while horario == "":
        print("[yellow]AVISO[/]\nO campo 'data' está vazio, para continuar digite o data corretamente.")
        horario = str(input("Didite o horario 'hh:mm': "))

    consulta = Consulta(medico_encontrado, paciente_encontrado, data, horario)
    paciente_encontrado.adicionar_consulta(consulta)

def ver_historico():

    print("Lista de pacientes")
    print(pacientes)
    nome_paciente = str(input("Digite o nome do paciente que deseja marcar uma consulta: "))
    paciente_encontrado = None
    for paciente in pacientes:
        if paciente.nome == nome_paciente:
            paciente_encontrado = paciente
    if not paciente_encontrado:
        print("[red]Paciente não encontrado![/]")
        return

    print(paciente_encontrado.info())

def ver_medico():

    print("Lista de medicos para buscar informações")
    print(medicos)
    nome_medico = str(input("Digite o nome do medico que deseja marcar um horario : "))
    medico_encontrado = None
    for medico in medicos:
        if medico.nome == nome_medico:
            medico_encontrado = medico
            break
    if not medico_encontrado:
        print("[red]Médico não encontrado![/]")
        return

    print(medico_encontrado.info())