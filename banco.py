import sqlite3
from pathlib import Path
from rich import print

CAMINHO_DB = Path(__file__).parent / 'clinica.db'


def connect_db():
    return sqlite3.connect(CAMINHO_DB)


def create_tables():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS medicos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cpf TEXT NOT NULL UNIQUE,
    crm TEXT NOT NULL,
    especialidade TEXT NOT NULL,
    valor_consulta REAL NOT NULL)
    ''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS pacientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cpf TEXT NOT NULL UNIQUE,
    plano TEXT NOT NULL)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS consultas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    medico_id INTEGER NOT NULL,
    paciente_id INTEGER NOT NULL,
    data TEXT NOT NULL,
    hora TEXT NOT NULL,
    FOREIGN KEY (medico_id) REFERENCES medicos(id),
    FOREIGN KEY (paciente_id) REFERENCES pacientes(id)
    )''')

    conn.commit()
    conn.close()


def salvar_medico(medico):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO medicos (nome, cpf, crm, especialidade, valor_consulta) VALUES (?, ?, ?, ?, ?)',
        (medico.nome, medico.cpf, medico.crm, medico.especialidade, medico.valor_consulta)
    )
    conn.commit()
    conn.close()


def listar_medicos():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM medicos')
    resultado = cursor.fetchall()
    conn.close()
    return resultado


def salvar_paciente(paciente):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO pacientes (nome, cpf, plano) VALUES (?, ?, ?)',
        (paciente.nome, paciente.cpf, paciente.plano)
    )
    conn.commit()
    conn.close()


def listar_pacientes():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM pacientes')
    resultado = cursor.fetchall()
    conn.close()
    return resultado


def buscar_id_por_cpf(tabela, cpf):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(f'SELECT id FROM {tabela} WHERE cpf = ?', (cpf,))
    resultado = cursor.fetchone()
    conn.close()
    if resultado:
        return resultado[0]
    return None


def salvar_consulta(consulta):
    id_medico = buscar_id_por_cpf('medicos', consulta.medico.cpf)
    id_paciente = buscar_id_por_cpf('pacientes', consulta.paciente.cpf)

    if id_medico is None or id_paciente is None:
        print('[red]ERRO![/] Médico ou paciente não está cadastrado no banco.')
        return

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO consultas (medico_id, paciente_id, data, hora) VALUES (?, ?, ?, ?)',
        (id_medico, id_paciente, consulta.data, consulta.hora)
    )
    conn.commit()
    conn.close()
    print(f"[green]SUCESSO![/] Consulta agendada para {consulta.paciente.nome} "
          f"com {consulta.medico.nome} em {consulta.data} às {consulta.hora}.")


if __name__ == "__main__":
    create_tables()
    print("Tabelas criadas!")

    from sistema import Medico, Paciente, Consulta

    m = Medico('Dr. João', '111.111.111-11', 'CRM123', 'Cardiologia', 300.0)
    p = Paciente('Maria Santos', '222.222.222-22', 'Unimed')
    c = Consulta(m, p, '20/10/2026', '14:00')

    salvar_medico(m)
    salvar_paciente(p)
    salvar_consulta(c)