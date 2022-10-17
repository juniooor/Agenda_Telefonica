import mysql.connector


conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='dados'
)
cursor = conexao.cursor()

nome = 'junior'
numero = '81996316701'
comando = f'INSERT INTO dados(nome, numero) VALUES ("{nome}", "{numero}")'
cursor.execute(comando)
conexao.commit()
cursor.close()
