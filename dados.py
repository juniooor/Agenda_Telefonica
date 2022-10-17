# import mysql.connector

# class dadosbd:
#     def __init__(self):
#         self.conexao = mysql.connector.connect(
#             host='localhost',
#             user='root',
#             password='',
#             database='bdagenda'
#         )
        
#     def __del__(self):
#         self.cursor.close()
#         self.conexao.close()
        
        
#     def inserir(self,nome, numero):
#         try:
#             comando = f'INSERT INTO dados(nome, numero) VALUES ("{nome}", "{numero}")'
#             self.cursor.execute(comando)
#             self.conexao.commit()
#         except TypeError as e:
#             return f'error {e} verifique sql'
        
        
import mysql.connector



class Cadastrar:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='bdagenda',
        )
        self.cursor = self.conexao.cursor()

    # def __del__(self):
    #     self.cursor.close()
    #     self.conexao.close()
        

    def criar(self, nome, numero):
        comando = f'INSERT INTO dados(nome, numero) VALUES ("{nome}", "{numero}")'
        self.cursor.execute(comando)
        self.conexao.commit()
        print('Usuario cadastrado')
        
        
        
if __name__ == "__main__" :
    
    cadastro = Cadastrar.criar()
    cadastro(nome='junior', numero='123456789')
    
      