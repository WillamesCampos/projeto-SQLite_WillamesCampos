from database import BancoDeDados

"""Verifica se a aplicação vai ser executada pelo cmd"""
if __name__ == '__main__':
    banco = BancoDeDados()
    banco2 = BancoDeDados()

    print(f'Instancia 1: {banco} Instancia 2: {banco2}')
    banco.conecta()
    banco.criar_tabelas()
    banco.inserir_cliente(
        'WILL', 'python', '1234567891', 'will@teste.com'
    )
    banco.inserir_cliente(
        'WILLX', 'python', '1234567889', 'will@teste2.com'
    )
    banco.buscar_email(email='will@teste.com')
    banco.remover_cliente(cpf='1234567889')
    banco.login('WILL', 'python')
    banco.desconecta()