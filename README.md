@ -0,0 +1,36 @@
# Sistema clinica medica

Sistema de linha de comando em Python para cadastro de médicos e pacientes e agendamento de consultas. Projeto de estudo focado nos quatro pilares da Programação Orientada a Objetos.

## Objetivo

Praticar os quatro pilares da programação orientada a objetos, além de organização dos cogidos em modulos, persistencia de dados com SQLite e versionamento com Git e GitHub.

## Funcionaliadades

- Cadastro de médicos (nome, CPF, CRM, especialidade e valor da consulta)
- Cadastro de pacientes (nome, CPF e plano de saúde)
- Agendamento de consultas, com histórico por paciente
- Consulta das informações de médicos e pacientes
- Menu interativo no terminal, com a biblioteca `rich`
- Persistência em SQLite (tabelas `medicos`, `pacientes` e `consultas`, com chaves estrangeiras) e verificação de horário já ocupado

## Tecnologias

- Python 3
- SQLite (`sqlite3`)
- [rich](https://github.com/Textualize/rich) para o terminal colorido

## Como executar

```bash
git clone https://github.com/MarcosApollo/sistema-clinica-medica.git
cd sistema-clinica-medica
pip install rich
python menu.py
```

## Autor 

Marcos Apollo, estudante de análise e desenvolvimento de sistemas
GitHub: [@MarcosApollo](https://github.com/MarcosApollo)