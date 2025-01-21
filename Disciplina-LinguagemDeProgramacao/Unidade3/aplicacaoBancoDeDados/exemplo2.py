import sqlite3

conn = sqlite3.connect('bancoaula.db')
cursor = conn.cursor()

ddl_create = """
CREATE TABLE IF NOT EXISTS COLABORADOR (
   NOME VARCHAR(255) NOT NULL,
   CARGO VARCHAR(255) NOT NULL,
   EMPRESA VARCHAR(255) NOT NULL
);
"""

cursor.execute(ddl_create)

insert_data = """

INSERT INTO COLABORADOR (NOME, CARGO, EMPRESA) VALUES (?, ?, ?)

"""

colaboradores = [
   ('DAVI', 'ENGENHEIRO DE SOFTWARE', 'FINTECH'),
   ('ARISIO', 'DESENVOLVEDOR BACK-END', 'FINTECH'),
   ('ROBERTA', 'ANALISTA FINANCEIRA', 'FINTECH'),
   ('BEATRIZ', 'DESENVOLVEDORA FRONT-END', 'FINTECH')
]

cursor.executemany(insert_data, colaboradores)

print("Dados inseridos na tabela: ")
cursor.execute('SELECT * FROM COLABORADOR')
for row in cursor.fetchall():
   print(row)

conn.commit()
cursor.close()
conn.close()