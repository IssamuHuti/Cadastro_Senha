import os
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.withdraw()

def limpar():
    os.system('cls')

def cadastro():

    cadastro_login = input('Cadastre um novo usuário: ')
    while True:
        maiusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        minusculas = 'abcdefghijklmnopqrstuvwxyz'
        numerais   = '0123456789'
        especiais  = '!@#$%&*()_+=?!'
        varidacao_maiuscula = False
        varidacao_minuscula = False
        varidacao_numerais  = False
        varidacao_especiais = False

        cadastro_senha = input('Cadastre a senha: ')

        if len(cadastro_senha) < 8:
            messagebox.showinfo('Erro', 'A senha tem que ter mais de 8 dígitos, tente novamente!')
            continue

        for i in cadastro_senha:
            if i in maiusculas:
                varidacao_maiuscula = True
            elif i in minusculas:
                varidacao_minuscula = True
            elif i in numerais:
                varidacao_numerais = True
            elif i in especiais:
                varidacao_especiais = True
            
        if varidacao_maiuscula and varidacao_minuscula and varidacao_numerais and varidacao_especiais:
            return cadastro_login, cadastro_senha
        else:
            messagebox.showinfo('Erro','Senha fraca, digite novamente!')

senha_salva = []
login_salvo = []
cadastrar = 'N'

while True:
    if cadastrar == 'S':
        confirmacao = '2'
    else:
        confirmacao = input('Possui cadastro: 1 - Sim  2 - Não ')

    if confirmacao == '2':
        limpar()
        login, senha = cadastro()
        login_salvo.append(login)
        senha_salva.append(senha)    
    elif confirmacao == '1':
        if not senha_salva or not login_salvo:
            limpar()

            messagebox.showinfo('Erro', 'Nenhum usuário cadastrado! Cadastre um usuário!')
            login, senha = cadastro()
            login_salvo.append(login)
            senha_salva.append(senha)

        else:
            limpar()

            tentativa = 0 
            while tentativa < 3:
                login_informado = input('Login:')
                senha_informado = input('Senha:')

                tentativa += 1

                if login_informado in login_salvo:
                    index = login_salvo.index(login_informado)
                    if senha_informado == senha_salva[index]:
                        messagebox.showinfo('Sucesso', 'Bem Vindo!')     
                        break
                    else:
                        messagebox.showinfo('Erro', 'Senha incorreta, tente novamente!')
                else: 
                    messagebox.showinfo('Erro', 'Login inexistente, tente novamente!')

                limpar()

            if tentativa == 3:
                messagebox.showinfo('Erro', 'Limite de tentativas excedidas, tente novamente mais tarde!')
                break

    limpar()
    cadastrar = input('Deseja cadastrar mais um usuario: S (sim) ou N (não): ').upper()
    while cadastrar not in 'SN':
        messagebox.showinfo('Erro', 'Opção não cadastrada!')
        cadastrar = input('Digite somente "S" ou "N" ').upper()

    if cadastrar == 'S':
        limpar()
        continue
    else:
        break

if login_salvo:
    print("Usuários cadastrados:", login_salvo)
else:
    print("Nenhum usuário foi cadastrado.")

