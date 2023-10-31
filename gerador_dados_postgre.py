import psycopg2
from faker import Faker


# Conecta-se ao Postgresql
conn = psycopg2.connect(
    dbname='Empresa',
    user='postgres',
    password='12345'
)

cur = conn.cursor()

fake = Faker(locale='pt-br')

# Cria a tabela cargos no PostgreSQL (se ainda não existir)
create_cargos_table_query = '''
CREATE TABLE IF NOT EXISTS cargos (
    codigo INT PRIMARY KEY,
    descricao VARCHAR(255),
    salario VARCHAR(10)
);
'''
cur.execute(create_cargos_table_query)

base_sql_carg = '''    
    INSERT INTO cargos
        (codigo, descricao, salario)
    VALUES
        ('{}', '{}', '{}')
    '''

for i in range(13086332):
    descricao = fake.job()
    salario = "R$ " + str(fake.random_int(min=1320.00, max=8000.00))
    sql_dep = base_sql_carg.format(i, descricao, salario)
    cur.execute(sql_dep)

# Cria a tabela funcionarios no PostgreSQL (se ainda não existir)
create_funcionarios_table_query = '''
CREATE TABLE IF NOT EXISTS funcionarios (
    cpf VARCHAR(20) PRIMARY KEY,
    nome VARCHAR(255),
    cod_cargo INT,
    FOREIGN KEY (cod_cargo) REFERENCES cargos(codigo)
);
'''

cur.execute(create_funcionarios_table_query)

base_sql_func = '''
    INSERT INTO funcionarios
        (cpf, nome, cod_cargo)
    VALUES
        ('{}','{}','{}')
    '''

# Função para gerar um CPF formatado no padrão brasileiro
def gerar_cpf_formatado():

    while True:
        cpf = str(fake.random_int(min=00000000000, max=99999999999))
        
        # Formate o CPF no padrão brasileiro (XXX.XXX.XXX-XX)
        cpf_formatado = f"{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

        if not cpf_existe(cpf_formatado):
            return cpf_formatado

# Função para verificar se um CPF já existe no banco de dados
def cpf_existe(cpf):
    cur.execute("SELECT COUNT(*) FROM funcionarios WHERE cpf = %s", (cpf,))
    existe = cur.fetchone()[0] > 0
    return existe

# Gera dados fictícios
for i in range(9923721):
    cpf = gerar_cpf_formatado()
    nome = fake.name()
    sql_func = base_sql_func.format(cpf, nome, i)

    cur.execute(sql_func)

# Commit das alterações e fechamento da conexão
conn.commit()
conn.close()
