import sqlite3


class BancoDeDados(object):
    """Classe que representa o banco de dados da aplicação"""

    def __new__(cls, nome='banco.db'):

        cls.nome, cls.conexao = nome, None
        if not hasattr(cls, 'instance'):
            cls.instance = super(BancoDeDados, cls).__new__(cls)

        return cls.instance


    def conecta(self):
        """Conecta Passando o nome do arquivo"""
        self.conexao = sqlite3.connect(self.nome)

    def desconecta(self):
        """Desconecta do banco"""
        try:
            self.conexao.close()
        except Exception as e:
            raise AttributeError('O banco não está conectado.')

    def criar_tabelas(self, nome_tabela=None):
        """Cria as tabelas do banco"""
        if not nome_tabela:
            nome_tabela='clientes'

        try:
            cursor = self.conexao.cursor()
        except Exception:
            raise AttributeError('O banco deve estar conectado antes de criar tabelas')

        cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {nome_tabela} (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            senha VARCHAR(20) NOT NULL,
            cpf VARCHAR(11) UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL
        );
        """)

    def inserir_cliente(self, nome, senha, cpf, email):
        """Insere o cliente no banco"""
        try:
            cursor = self.conexao.cursor()

            cursor.execute(
                """INSERT INTO clientes (nome, senha, cpf, email) VALUES (?,?,?,?)""", (nome, senha,  cpf, email)
            )

            self.conexao.commit()
        except AttributeError:
            print('Faça a conexão do banco antes de inserir clientes.')
        except sqlite3.IntegrityError:
            print('O cpf %s já existe' %cpf)

    def buscar_cliente(self, cpf):
        """Busca o cliente pelo cpf"""
        try:
            cursor = self.conexao.cursor()

            cursor.execute("SELECT * FROM clientes WHERE cpf=?", [(cpf)])

            cliente = cursor.fetchone()

            if cliente:
                return True
            return False

        except AttributeError:
            print('Faça a conexão do banco antes de inserir clientes.')

    def login(self, username, senha):
        try:
            cursor = self.conexao.cursor()
            sql = 'SELECT * FROM clientes WHERE nome=? and senha=?'
            cliente = cursor.execute(sql, [username,senha]).fetchone()
            if cliente:
                return True
            return False
        except AttributeError:
            print('Faça a conexão com o banco primeiro.')

    def remover_cliente(self, cpf):
        """Remover um cliente pelo cpf"""
        try:
            cursor = self.conexao.cursor()

            cursor.execute('DELETE FROM clientes WHERE cpf=?', [(cpf)])
            self.conexao.commit()
        except AttributeError:
            print('Faça a conexão do banco antes de buscar clientes.')

    def buscar_email(self, email):
        """Busca o cliente pelo email"""
        try:
            cursor = self.conexao.cursor()

            cursor.execute("SELECT * FROM clientes WHERE email=?", [(email)])

            cliente = cursor.fetchone()
        except AttributeError:
            print('Faça a conexão do banco antes de buscar clientes.')

        if cliente:
            return True
        return False
