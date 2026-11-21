import sqlite3
from pathlib import Path

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

if __name__ == "__main__":
    create_tables()
    print("Tabelas criadas!")

    from sistema import *

    m = Medico('Dr. João', '111.111.111-11', 'CRM123', 'Cardiologia', 300.0)
    salvar_medico(m)
    print(listar_medicos())