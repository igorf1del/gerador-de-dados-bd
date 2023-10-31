
import pymongo
from faker import Faker

# Conecta-se ao servidor MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Cria um banco de dados ou usa um existente
db = client["Empresa"]

# Cria uma coleção para os cargos
cargos_collection = db["cargos"]

fake = Faker(locale='pt-br')

# Insere dados fictícios na coleção de cargos 
for i in range(28725490):
    descricao = fake.job()
    salario = "R$ " + str(fake.random_int(min=1320.00, max=8000.00))
    cargo = {
        "codigo": i,
        "descricao": descricao,
        "salario": salario
    }
    cargos_collection.insert_one(cargo)

# Cria uma coleção para os funcionários
funcionarios_collection = db["funcionarios"]

# Função para gerar um CPF formatado no padrão brasileiro
def gerar_cpf_formatado():

    while True:
        cpf = str(fake.random_int(min=00000000000, max=99999999999))
        
        # Formata o CPF no padrão brasileiro (XXX.XXX.XXX-XX)
        cpf_formatado = f"{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

        if not cpf_existe(cpf_formatado):
            return cpf_formatado

# Função para verificar se um CPF já existe na coleção de funcionários
def cpf_existe(cpf):
    existing_cpf = funcionarios_collection.find_one({"cpf": cpf})
    return existing_cpf is not None

# Insere dados fictícios na coleção de funcionários 
for i in range(23772692):
    cpf = str(fake.random_int(min=00000000000, max=99999999999))
    cpf_formatado = f"{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

    nome = fake.name()
    funcionario = {
        "cpf": cpf_formatado,
        "nome": nome,
        "cod_cargo": i
    }
    funcionarios_collection.insert_one(funcionario)