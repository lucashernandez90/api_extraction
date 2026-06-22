import csv
import sqlite3
import os

def import_csv():

    csv_path = os.path.join('data', 'DEINFO_AB_FEIRASLIVRES_2014.csv')
    db_path = 'feiras.db'

    if not os.path.exists(csv_path):
        print(f"Arquivo CSV nao encontrado em: {csv_path}")
        return
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    with open(csv_path, mode='r', encoding='latin-1') as arquivo_csv:
        reader = csv.DictReader(arquivo_csv)

        count = 0
        for line in reader:
            try:

                cursor.execute('''
                    INSERT OR IGNORE INTO feiras (
                        id_original, long, lat, setcens, areap, coddist, distrito,
                        codsubpref, subprefe, regiao5, regiao08, nome_feira,
                        registro, logradouro, numero, bairro, referencia
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    line.get('ID'),
                    line.get('LONG'),
                    line.get('LAT'),
                    line.get('SETCENS'),
                    line.get('AREAP'),
                    line.get('CODDIST'),
                    line.get('DISTRITO'),
                    line.get('CODSUBPREF'),
                    line.get('SUBPREFE'),
                    line.get('REGIAO5'),
                    line.get('REGIAO08'),
                    line.get('NOME_FEIRA'),
                    line.get('REGISTRO'), # Código único exigido para busca/exclusão
                    line.get('LOGRADOURO'),
                    line.get('NUMERO'),
                    line.get('BAIRRO'),
                    line.get('REFERENCIA')
                ))

                count += 1
            except Exception as e:
                print(f"Erro to insert line {count}: {e}")

    conn.commit()
    conn.close()
    print(f"{count} feiras")

if __name__ == "__main__":
    import_csv()