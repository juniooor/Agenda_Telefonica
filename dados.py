import mysql.connector
from mysql.connector import Error


class Dadosbd:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='bdagenda'
        )

        self.cursor = self.conexao.cursor()

    def inserir(self, nome, numero):
        try:
            comando = f'INSERT INTO agenda(nome, numero) VALUES ("{nome}", "{numero}")'
            self.cursor.execute(comando)
            self.conexao.commit()
            print('usuario cadastrado')
        except Error as e:
            return f'error {e} verifique sql'

    
    def excluir(self, idagenda):
        comando = f'DELETE FROM agenda WHERE idagenda = "{idagenda}"'
        self.cursor.execute(comando)
        self.conexao.commit()
        print('numero apagado')
        
    def editar(self, numero, nome, idagenda):
        comando = f'UPDATE agenda SET numero = "{numero}", nome = "{nome}" WHERE idagenda = "{idagenda} LIMIT 1" '
        self.cursor.execute(comando)
        self.conexao.commit()
        print('dados atualizados')
        
    def vizualizar(self, nome):
        comando = f'SELECT * FROM agenda WHERE nome LIKE "{nome}%"'
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        return resultado

    # def __del__(self):
    #     self.cursor.close()
    #     self.conexao.close()
# import mysql.connector


if __name__ == "__main__":

    cadastro = Dadosbd()
    dados = cadastro.vizualizar(nome='junior')
    
    for i, e , a in dados:
        print(f' {i} |  {e}   |   {a}')
    
    
