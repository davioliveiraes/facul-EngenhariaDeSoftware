import sqlite3

conn = sqlite3.connect('aulaDB.db')

ddl_create = """

CREATE TABLE IF NOT EXISTS forncedor (
   id_fornecedor INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
   nome_fornecedor TEXT NOT NULL,
   cpnj VARCHAR(18) NOT NULL,
   cidade TEXT,
   estado VARCHAR(2) NOT NULL,
   cep VARCHAR(8) NOT NULL,
   data_cadastro DATE NOT NULL
);
"""

cursor = conn.cursor()
cursor.execute(ddl_create)

print("Tabela criado com sucesso.")
print(f"Descrição do cursor: {cursor.description}")
print(f"Linhas afetadas: {cursor.rowcount}")

cursor.close()
conn.close()