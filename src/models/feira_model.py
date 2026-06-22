import sqlite3

def create_table():

    conn = sqlite3.connect('feiras.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS feiras (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_original INTEGER,
            long TEXT,
            lat TEXT,
            setcens TEXT,
            areap TEXT,
            coddist INTEGER,
            distrito TEXT NOT NULL,
            codsubpref INTEGER,
            subprefe TEXT,
            regiao5 TEXT NOT NULL,
            regiao08 TEXT,
            nome_feira TEXT NOT NULL,
            registro TEXT UNIQUE NOT NULL, -- Código de registro único exigido pelo teste
            logradouro TEXT,
            numero TEXT,
            bairro TEXT NOT NULL,
            referencia TEXT
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_table()
    print("Created 'feiras' table")