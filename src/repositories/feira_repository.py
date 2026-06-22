# src/repositories/feira_repository.py
import sqlite3

def obtain_connection():
    conn = sqlite3.connect('feiras.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_all():
    with obtain_connection() as conn:
        lines = conn.execute('SELECT * FROM feiras').fetchall()
        return [dict(line) for line in lines]
    

def search_for_id(id_feira):
    with obtain_connection() as conn:
        line = conn.execute('SELECT * FROM feiras WHERE id = ?', (id_feira,)).fetchone()
        return dict(line) if line else None

def search_for_distrito(distrito):
    with obtain_connection() as conn:
        lines = conn.execute('SELECT * FROM feiras WHERE LOWER(distrito) = LOWER(?)', (distrito,)).fetchall()
        return [dict(line) for line in lines]

def search_for_regiao5(regiao5):
    with obtain_connection() as conn:
        lines = conn.execute('SELECT * FROM feiras WHERE LOWER(regiao5) = LOWER(?)', (regiao5,)).fetchall()
        return [dict(line) for line in lines]

def search_for_registro(registro):
    with obtain_connection() as conn:
        line = conn.execute('SELECT * FROM feiras WHERE LOWER(registro) = LOWER(?)', (registro,)).fetchone()
        return dict(line) if line else None

def search_for_name(nome_feira):
    with obtain_connection() as conn:
        lines = conn.execute('SELECT * FROM feiras WHERE LOWER(nome_feira) = LOWER(?)', (nome_feira,)).fetchall()
        return [dict(line) for line in lines]

def search_for_bairro(bairro):
    with obtain_connection() as conn:
        lines = conn.execute('SELECT * FROM feiras WHERE LOWER(bairro) = LOWER(?)', (bairro,)).fetchall()
        return [dict(line) for line in lines]

def register_feira(data):
    with obtain_connection() as conn:

        columns = [key.lower() for key in data.keys()]
        values = list(data.values())
        placeholders = ', '.join(['?'] * len(values))
        
        query = f"INSERT INTO feiras ({', '.join(columns)}) VALUES ({placeholders})"
        cursor = conn.execute(query, values)
        conn.commit()
        return cursor.lastrowid


def update_feira(registro, data):
    with obtain_connection() as conn:
            camps = []
            values = []
            for key, valor in data.items():
                if key.lower() not in ['id', 'registro']:
                    camps.append(f"{key.lower()} = ?")
                    values.append(valor)
            
            if not camps:
                return False
                
            values.append(registro)
            query = f"UPDATE feiras SET {', '.join(camps)} WHERE LOWER(registro) = LOWER(?)"
            cursor = conn.execute(query, values)
            conn.commit()
            return cursor.rowcount > 0


def delete_feira(registro):
    with obtain_connection() as conn:
            cursor = conn.execute('DELETE FROM feiras WHERE LOWER(registro) = LOWER(?)', (registro,))
            conn.commit()
            return cursor.rowcount > 0