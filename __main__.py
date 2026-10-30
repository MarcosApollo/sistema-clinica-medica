from sistema import *
from menu import *
from rich import print

def main():

    m = Medico('Dr. João Silva', '111.111.111-11', 'CRM123', 'Cardiologia', 300.0)
    p = Paciente('Maria Santos', '222.222.222-22', 'Unimed')
    c = Consulta(m, p, '20/10/2026', '14:00')

    p.adicionar_consulta(c)

    print(m.info())
    print(p.info())
    print(c.resumo())

if __name__ == "__main__":
    main()