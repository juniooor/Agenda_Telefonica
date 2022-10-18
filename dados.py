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
        
             
        
        
    def inserir(self,nome, numero):
        try:
            comando = f'INSERT INTO agenda(nome, numero) VALUES ("{nome}", "{numero}")'
            self.cursor.execute(comando)
            self.conexao.commit()
            print('usuario cadastrado')
        except Error as e:
            return f'error {e} verifique sql'
        
        
    # def __del__(self):
    #     self.cursor.close()
    #     self.conexao.close()
# import mysql.connector




        
if __name__ == "__main__" :
    
    cadastro = Dadosbd()
    cadastro.inserir(nome='junior3', numero='12345678')
    
      