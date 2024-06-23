import os

def limpar():
    os.system('cls')

def cadastro():
    cadastro_login = input('Cadastre um novo usuário: ')
    cadastro_senha = int(input('Cadastre a senha: '))
    login_salvo = cadastro_login
    senha_salva = cadastro_senha

while True:
    confirmacao = int(input('Possui cadastro: 1 - Sim  2 - Não '))
    senha_salva = 0
    login_salvo = ''
    if confirmacao == 2:
        limpar()
        cadastro()
    elif confirmacao == 1:
        if senha_salva == 0 or login_salvo == '':
            limpar()
            print('Nenhum usuário cadastrado!')
            print('Cadastre um usuário!')
            print()
            cadastro()
    
    limpar()
    login = input('Login: ')
    senha = int(input('Digite a senha: '))
    login_salvo = login
    senha_salva = senha

    tentativa = 0 
    while (senha == senha_salva and login == login_salvo):
        limpar()
        if tentativa == 2:
            print('Excesso de tentativas, tente mais tarde!')
            break
        print('Login ou Senha incorreta, tente novamente!')
        tentativa += 1
        print()
        login = input('Digite a login novamente: ')
        senha = int(input('Digite a senha novamente: '))
    if tentativa == 2:
        break

    limpar()
    print('Bem Vindo!')
    redefinir = input('Deseja redefinir a senha: S (sim) ou N (não): ').upper()
    while redefinir not in 'SN':
        correcao = input('Digite somente "S" ou "N" ')
        redefinir = correcao.upper()
    print()
    if redefinir == 'S':
        nova_senha = int(input('Defina uma nova senha: '))
        senha_salva = nova_senha
    elif redefinir == 'N':
        break

# problema com recadastro de senha

'''
login_salvo = input('Login: ')
senha_salva = int(input('Digite a senha: '))

tentativa = 0
while True:
    limpar()
    login = input('Digite o login: ')
    senha = int(input('Digite a senha: '))

    if login == login_salvo and senha == senha_salva:
        print('Login realizado com sucesso!')
        break
    else:
        print('Login ou Senha incorreta, tente novamente!')
        tentativa += 1

    if tentativa >= 2:
        print('Excesso de tentativas, tente mais tarde!')
        break
'''