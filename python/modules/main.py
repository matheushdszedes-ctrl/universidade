from modules.aluno import Aluno
from python.modules.MySQL import MySQL

banco = MySQL()
banco.connect()
aluno = Aluno(
    "Jose Maria",
    "jose.maria@email.com",
    "98765432123",
    "123456789999",
    "Rua são Domingos"   
)

query = aluno.cadastras(banco)
# print (query)

banco.execute_query(query)

banco.disconnect()